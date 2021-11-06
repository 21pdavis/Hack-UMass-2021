import React from "react";
import './MainContents.css'

class MainContents extends React.Component{
    constructor(){
        super()
        this.initContents();
    }

    initContents(){
        this.contentText="Default Contents"
        this.contents = (
            <p>{this.contentText}</p>
        )
    }

    render(){

        return (
            <div className='main'>
                {this.contents}
            </div>
        )
    }
}

export default MainContents