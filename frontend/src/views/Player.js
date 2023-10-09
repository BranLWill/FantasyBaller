import { React, Component } from "react";

export default class PlayerView extends Component {

    constructor(props){
        super(props);
        this.state={
            value:this.props.location.state,
        }
    }

    alertMessage(){
       console.log(this.props.location.state.name);
    }

    render() {
        return (

            <>
                {/* the below is the id we are accessing */}
                <h1>{this.props.location.state.name}</h1>
            </>

        )
    }
};
