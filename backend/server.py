"""Python Flask API Auth0 integration example
"""
from flask import Flask
import datetime
import pandas as pd
import nfl_data_py as nfl

from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from authlib.integrations.flask_oauth2 import ResourceProtector
from validator import Auth0JWTBearerTokenValidator

x = datetime.datetime.now()

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    "access-auth.us.auth0.com",
    "mind"
)
require_auth.register_token_validator(validator)

APP = Flask(__name__)
CORS(APP, resources={r"/*": {"origins": "http://localhost:3000"}})

@APP.route("/api/private-scoped")
@require_auth("read:messages")
def private_scoped():
    """A valid access token and scope are required."""
    response = (
        "Hello from a private endpoint! You need to be"
        " authenticated and have a scope of read:messages to see"
        " this."
    )
    return jsonify(message=response)

# Route for seeing data
@APP.route('/api/data')
@require_auth(None)
def get_time():
    return {
        "geek": {
            'Name': "geek",
            'Age': "22",
            'Date': x,
            'Programming': "Python",
            "TEST": "IDK"
        },
    }

# GET all team info
@APP.route('/api/teams/<string:team_code>', methods=['GET'])
@require_auth(None)
def get_all_current_teams(team_code: str):
    try:
        result = None

        if team_code.lower() == "all":
            result = nfl.import_team_desc()
            result = result.to_dict()
        else:
            result = nfl.import_team_desc()
            result = result[result['team_abbr'] == team_code]
            result = result.to_dict()

        if result is None:
            abort(404)

        return jsonify({
            'success': True,
            'teams': result
        })

    except:
        abort(400)

# GET all players
@APP.route('/api/players/<string:data_type>')
@require_auth(None)
def get_all_current_players_stats(data_type: str):
    try:
        result = None

        if data_type.lower() == "stats":
            result = get_all_current_players()
        elif data_type.lower() == "cards":
            result = get_all_current_player_cards()

        if result is None:
            abort(404)

        return result

    except Exception as ex:
        print(ex)
        abort(400)

# GET player by name for a stat type and a certain year
@APP.route('/api/players/<string:player_name>/<string:year>/<string:stat_type>', methods=['GET'])
@require_auth(None)
def get_player_stats(player_name: str, year: str, stat_type: str):
    try:
        result = None

        if year.lower() == "all":
            years = get_all_years()
        else:
            years = [year]

        if stat_type.lower() == "weekly":
            result = get_player_weekly_stats(player_name, years)
        elif stat_type.lower() == "season":
            result = get_player_season_stats(player_name, years)

        if result is None:
            abort(404)

        return jsonify({
            'success': True,
            'player': result
        })

    except:
        abort(400)

@APP.route('/api/players/<string:team_code>/<string:year>/<string:stat_type>', methods=['GET'])
@require_auth(None)
def get_team_weekly_stats(team_code: str, year: str, stat_type: str):
    try:
        result = None

        if year.lower() == "all":
            years = get_all_years()
        else:
            years = [year]

        if stat_type.lower() == "weekly":
            result = get_team_weekly(team_code, years)

        if result is None:
            abort(404)

        return jsonify({
            'success': True,
            'player': result
        })

    except:
        abort(400)

def get_all_years() -> list:
    results = []
    for i in range(1999, get_this_year() + 1):
        results.append(i)

    return results

def get_this_year() -> int:
    return int(datetime.datetime.now().date().strftime("%Y"))

def get_player_season_stats(player_name: str, years: list):
    
    if len(years) == 0:
        years = get_this_year()
    
    season_stats = nfl.import_seasonal_data(years=years)
    player_info = nfl.import_players()
    player_info = player_info[player_info['display_name'] == player_name]
    result = season_stats[season_stats['player_id']
                            == player_info['gsis_id'].tolist()[0]]
    result.insert(loc=1, column='player_name',
                    value=[player_name]*len(result))
    
    return result.to_dict()

def get_player_weekly_stats(player_name: str, years: list):

    if len(years) == 0:
        years = get_this_year()

    result = nfl.import_weekly_data(years)
    result.fillna(0.0, inplace=True)

    return result.query(f"player_display_name=='{player_name}'").to_dict()

def get_team_weekly(team_code: str, years: list):
    
    if len(years) == 0:
        years = get_this_year()

    result = nfl.import_weekly_data(years)
    result.fillna(0.0, inplace=True)
    return result.query(f"recent_team=='{team_code}'").to_dict()

def get_all_current_players() -> dict:
    player_headshots = nfl.import_weekly_data(years=[get_this_year()])[['player_display_name', 'headshot_url']]
    season_data = nfl.import_seasonal_data(years=[get_this_year()])
    player_info = nfl.import_players()
    player_info.rename(columns={'gsis_id': 'player_id'}, inplace=True)

    #list(player_info[player_info['status'] != 'RET']['display_name'])
    players_df = player_info.query("status=='ACT' | status=='RES'")

    result = pd.merge(season_data, players_df[['player_id', 'display_name', 'status_short_description']], on = "player_id")

    column_to_move = result.pop("display_name")
    result.insert(1, "display_name", column_to_move)
    result = result.head(6)

    final = {}
    for _, row in result.iterrows():
        data = row.copy()
        headshot_url = get_player_headshot(row['display_name'], player_headshots)
        data['headshot_url'] = headshot_url
        final.update({
            row['display_name']: data.to_dict()
        })

    return final #{"Justin Fields": final.get("Justin Fields")}

def get_all_current_player_cards() -> dict:
    player_headshots = nfl.import_weekly_rosters(years=[get_this_year()])[['player_name', 'headshot_url']]
    player_info = nfl.import_players()
    player_info.rename(columns={'gsis_id': 'player_id'}, inplace=True)
    player_info = player_info[['player_id', 'display_name', 'status_short_description', 'status']]

    #list(player_info[player_info['status'] != 'RET']['display_name'])
    players_df = player_info.query("status=='ACT' | status=='RES'")
    # players_df = players_df.head(9)

    final = {}
    for _, row in players_df.iterrows():
        data = row.copy()
        headshot_url = get_player_headshot(row['display_name'], player_headshots)
        data['headshot_url'] = headshot_url
        final.update({
            row['display_name']: data.to_dict()
        })

    return final

def get_player_headshot(player_name: str, player_headshots):
    player_info = player_headshots[player_headshots['player_name'] == player_name]

    if player_info.empty:
        return "https://a.espncdn.com/combiner/i?img=/games/lm-static/ffl/images/nomug.png&w=426&h=320&cb=1"

    return list(player_info['headshot_url'])[-1]

@APP.errorhandler(400)
def bad_request_error(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400

@APP.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@APP.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed'
    }), 405

@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

@APP.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 422

# Running app
if __name__ == '__main__':
    APP.run(debug=True)