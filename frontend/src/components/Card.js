import React from 'react';
import { Button } from 'reactstrap';
import { Link } from 'react-router-dom';

class Card extends React.Component {
  render() {
    const { name, headshot } = this.props;
    const data = {
      'name': name,
      'headshot_url': headshot
    }

    return (
      <div className="card" style={{ width: "18%", height: "300px", background: "white" }}>
        <img src={headshot} alt={"Missing Image"}/>
        <div className="card-body">
          <h5>{name}</h5>
          <Button
            color="primary"
            className="m-2"
            // onClick={callApi}
            // disabled={!audience}
          >
            Add
          </Button>
          <Button
            color="secondary"
            className="m-1"
            // onClick={callApi}
            // disabled={!audience}
          >
            <Link
              to={{
                pathname: "/player",
                state: data // your data array of objects
              }}
            >
              View
            </Link>
          </Button>
        </div>
      </div>
    );
  }
}

export default Card;