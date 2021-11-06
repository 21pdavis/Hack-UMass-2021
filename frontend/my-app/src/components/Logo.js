import React from "react";


class Logo extends React.Component{
    constructor(){
        super()
    }

    render(){

        return (
            <div>
                <img src={this.props.link}></img>
            </div>
        )
    }
}

export default Logo