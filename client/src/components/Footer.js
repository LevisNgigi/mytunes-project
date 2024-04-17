import React from "react";
import '../stylesheets/Footer.scss';

function Footer() {
    const today = new Date().getFullYear();

    return (
        <footer id="footer">
            Made by Group 2 
            <br />
            © 2024 Group 2. All rights reserved.{today} 
        </footer>
    )
}

export default Footer;