import React from 'react';
import { Button } from 'reactstrap';
import { Link } from 'react-router-dom';

class Card extends React.Component {
  render() {
    const { name, headshot } = this.props;
    const data = {'name': name}

    return (
      <div className="card" style={{ width: "31%", height: "400px", background: "white" }}>
        <img src={headshot} alt={"Missing Image"}/>
        <div className="card-body">
          <h2>{name}</h2>
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
            className="m-2"
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