import React from "react";

class Footer extends React.Component{
    constructor(){
        super()
        this.initFooter()
    }

    initFooter(){
        this.text = "Default Footer"
        this.contents = (
            <footer>{this.text}</footer>
        )
    }

    render(){

        return (
            <div className="footer">
                {this.contents}
            </div>
        )
    }
}

export default Footer