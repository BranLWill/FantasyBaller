"""Python Flask API Auth0 integration example
"""
import os
import datetime
import pandas as pd
import nfl_data_py as nfl

from flask import Flask, Response, request, abort, jsonify, send_file
from flask_cors import CORS
from authlib.integrations.flask_oauth2 import ResourceProtector
from validator import Auth0JWTBearerTokenValidator

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    "access-auth.us.auth0.com",
    "mind"
)
require_auth.register_token_validator(validator)

class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        self.action()
        return self.response


class RestAPI(object):
    app = None

    def __init__(self, name):
        self.max_card_count = 25
        self.current_time = datetime.datetime.now()
        self.player_headshots = nfl.import_weekly_rosters(years=[self.get_this_year()])[['player_name', 'headshot_url']]
        self.player_card_df = self.get_all_current_player_cards_df()

        self.app = Flask(name)
        CORS(self.app, resources={r"/*": {"origins": os.getenv('APP_ORIGIN')}})

        self.add_endpoint(
            endpoint='/api/teams/<string:team_code>',
            endpoint_name='get_team',
            handler=self.get_team
        )
        self.add_endpoint(
            endpoint='/api/players/stats',
            endpoint_name='get_all_players_stats',
            handler=self.get_all_players_stats
        )
        self.add_endpoint(
            endpoint='/api/players/cards',
            endpoint_name='get_all_player_cards',
            handler=self.get_all_player_cards
        )
        self.add_endpoint(
            endpoint='/api/players/<string:player_name>/<string:year>/<string:stat_type>',
            endpoint_name='get_player_stats',
            handler=self.get_player_stats
        )
        self.add_endpoint(
            endpoint='/api/players/<string:team_code>/<string:year>/<string:stat_type>',
            endpoint_name='get_team_weekly_stats',
            handler=self.get_team_weekly_stats
        )
        self.add_endpoint(
            endpoint='/api/images/logo',
            endpoint_name='get_logo',
            handler=self.get_logo
        )
        self.add_endpoint(
            endpoint='/api/metadata/totalPages',
            endpoint_name='get_total_pages',
            handler=self.get_total_pages
        )

    def run(self, **kwargs):
        self.app.run(**kwargs)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, view_func=handler)

    # GET all team info
    @require_auth(None)
    def get_team(self, team_code: str):
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

    # GET all players stats
    @require_auth(None)
    def get_all_players_stats(self):
        try:
            result = self.get_all_current_players()

            if result is None:
                abort(404)

            return result
        
        except Exception as ex:
            print(ex)
            abort(400)
        
    # GET all players cards
    @require_auth(None)
    def get_all_player_cards(self):
        try:
            result = None
            page_num = int(request.args.get("page_num", "1"))
            result = self.get_all_current_player_cards(page_num-1)

            if result is None:
                abort(404)

            return result

        except Exception as ex:
            print(ex)
            abort(400)

    # GET player by name for a stat type and a certain year
    @require_auth(None)
    def get_player_stats(self, player_name: str, year: str, stat_type: str):
        try:
            result = None

            if year.lower() == "all":
                years = self.get_all_years()
            else:
                years = [year]

            if stat_type.lower() == "weekly":
                result = self.get_player_weekly_stats(player_name, years)
            elif stat_type.lower() == "season":
                result = self.get_player_season_stats(player_name, years)

            if result is None:
                abort(404)

            return jsonify({
                'success': True,
                'player': result
            })

        except:
            abort(400)

    @require_auth(None)
    def get_team_weekly_stats(self, team_code: str, year: str, stat_type: str):
        try:
            result = None

            if year.lower() == "all":
                years = self.get_all_years()
            else:
                years = [year]

            if stat_type.lower() == "weekly":
                result = self.get_team_weekly(team_code, years)

            if result is None:
                abort(404)

            return jsonify({
                'success': True,
                'player': result
            })

        except:
            abort(400)

    def get_logo(self):
        try:
            filename = "../frontend/src/assets/brand_logo.svg"
            return send_file(filename, mimetype='image/svg+xml')

        except:
            abort(400)

    @require_auth(None)
    def get_total_pages(self) -> dict:
        try:
            return {'totalPages': self.get_max_pages()}
        except:
            abort(400)

    def get_all_years(self) -> list:
        results = []
        for i in range(1999, self.get_this_year() + 1):
            results.append(i)

        return results

    def get_this_year(self) -> int:
        return int(self.current_time.date().strftime("%Y"))

    def get_player_season_stats(self, player_name: str, years: list):
        
        if len(years) == 0:
            years = self.get_this_year()
        
        season_stats = nfl.import_seasonal_data(years=years)
        player_info = nfl.import_players()
        player_info = player_info[player_info['display_name'] == player_name]
        result = season_stats[season_stats['player_id']
                                == player_info['gsis_id'].tolist()[0]]
        result.insert(loc=1, column='player_name',
                        value=[player_name]*len(result))
        
        return result.to_dict()

    def get_player_weekly_stats(self, player_name: str, years: list):

        if len(years) == 0:
            years = self.get_this_year()

        result = nfl.import_weekly_data(years)
        result.fillna(0.0, inplace=True)

        return result.query(f"player_display_name=='{player_name}'").to_dict()

    def get_team_weekly(self, team_code: str, years: list):
        
        if len(years) == 0:
            years = self.get_this_year()

        result = nfl.import_weekly_data(years)
        result.fillna(0.0, inplace=True)
        return result.query(f"recent_team=='{team_code}'").to_dict()

    def get_all_current_players(self) -> dict:
        season_data = nfl.import_seasonal_data(years=[self.get_this_year()])
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
            headshot_url = self.get_player_headshot(row['display_name'])
            data['headshot_url'] = headshot_url
            final.update({
                row['display_name']: data.to_dict()
            })

        return final #{"Justin Fields": final.get("Justin Fields")}

    def get_all_current_player_cards_df(self) -> pd.DataFrame:
        player_info = nfl.import_players()
        player_info.rename(columns={'gsis_id': 'player_id'}, inplace=True)
        player_info = player_info[['player_id', 'display_name', 'status_short_description', 'status']]

        #list(player_info[player_info['status'] != 'RET']['display_name'])
        players_df = player_info.query("status=='ACT' | status=='RES'")

        for index, row in players_df.iterrows():
            headshot_url = self.get_player_headshot(row['display_name'])
            players_df.loc[index, 'headshot_url'] = headshot_url

        return players_df

    def get_all_current_player_cards(self, page_num: int = 0) -> dict:
        player_info = self.player_card_df

        #list(player_info[player_info['status'] != 'RET']['display_name'])
        players_df = player_info.query("status=='ACT' | status=='RES'")
        start_index = self.max_card_count * page_num
        last_index = start_index + self.max_card_count if start_index else self.max_card_count
        players_df = players_df.iloc[start_index:last_index]

        final = {}
        for _, row in players_df.iterrows():
            data = row.copy()
            final.update({
                row['display_name']: data.to_dict()
            })

        return final

    def get_player_headshot(self, player_name: str):
        player_info = self.player_headshots[self.player_headshots['player_name'] == player_name]

        if player_info.empty:
            return "https://a.espncdn.com/combiner/i?img=/games/lm-static/ffl/images/nomug.png&w=426&h=320&cb=1"

        return list(player_info['headshot_url'])[-1]
    
    def get_max_pages(self) -> int:
        player_info = nfl.import_players()
        player_info.rename(columns={'gsis_id': 'player_id'}, inplace=True)
        player_info = player_info[['player_id', 'display_name', 'status_short_description', 'status']]

        #list(player_info[player_info['status'] != 'RET']['display_name'])
        players_df = player_info.query("status=='ACT' | status=='RES'")
        return int(len(players_df['display_name'].unique().tolist()) / self.max_card_count) + 2

# Running app
if __name__ == '__main__':
    APP = RestAPI(__name__)
    APP.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)