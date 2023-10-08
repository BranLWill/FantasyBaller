import React from 'react';

class Card extends React.Component {
  render() {
    const { name, headshot } = this.props;
    return (
      <div className="card" style={{ width: "31%", height: "300px" }}>
        <img src={headshot} alt={"Missing Image"}/>
        <div className="card-body">
          <h2>{name}</h2>
        </div>
      </div>
    );
  }
}

export default Card;