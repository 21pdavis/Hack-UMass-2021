import React from "react";
import Logo from './Logo'
import './Navbar.css'

class Navbar extends React.Component{
    constructor(){
        super()
        this.initNavbar()
    }
    initNavbar(){
        this.navHeading="Default Navbar Heading"
        this.navText="Deafult Navbar Text"
        this.logoLink="https://media.discordapp.net/attachments/818160573023518742/896078237371883550/paimon.png"
        this.contents = (
            <div className="navbar">
                <table>
                    <tr>
                        <td>
                            <Logo className='navbar-logo' link={this.logoLink}/>
                        </td>
                        <td>
                            <div className='navbar-contents'>
                                <h1 className="navbar-heading">{this.navHeading}</h1>
                                <p className="navbar-text">{this.navText}</p>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>
        )
    }
    render(){
        return this.contents
    }
}

export default Navbar