import React from "react";
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// import { faEnvelope } from '@fortawesome/free-solid-svg-icons'

const Footer = () => (
  <footer className="bg-light p-3 text-center">
    <div className="logo" />
    {/* <div>
      <FontAwesomeIcon icon={faEnvelope} />
    </div> */}
    <p>
      User authentication provided by <a href="https://auth0.com">Auth0</a>
    </p>
  </footer>
);

export default Footer;
