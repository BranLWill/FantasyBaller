import { React, Component } from "react";

export default class PlayerView extends Component {

    constructor(props){
        super(props);
        this.state={
            value:this.props.location.state,
        }
    }

    render() {
        return (

            <>
                <div className="card" style={{ width: "20%", height: "275px", background: "white" }}>
                    <img src={this.props.location.state.headshot_url} alt={"Missing Image"}/>
                    <div className="card-body">
                        <h3>{this.props.location.state.name}</h3>
                    </div>
                </div>
            </>
        )
    }
};
