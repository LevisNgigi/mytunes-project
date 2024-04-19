import React from "react";
import '../stylesheets/Footer.scss';

function Footer() {
    const today = new Date().getFullYear();

    return (
        <footer id="footer">
            Made with ❤️ & 🍺
            <br />
            © Group 2{today} 
        </footer>
    )
}

export default Footer;