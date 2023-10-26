import React from "react";

import { useAuth0 } from "@auth0/auth0-react";
import logo from "../assets/logo.svg";

const Hero = () => {
  const {
    user,
    isAuthenticated,
    loginWithRedirect,
    logout,
  } = useAuth0();

  return (
    <div className="text-center hero my-5">
      {isAuthenticated ? (
        <>
          Get NFL stats here!
        </>
      ) : (
        <>
          <img className="mb-3 app-logo" src={logo} alt="React logo" width="120" />
          <h1 className="mb-4">Welcome to Fantasy Ballers!</h1>
      
          <p className="lead">
            We provide the most accurate and advanced analytical tools for your fantasy players.
          </p>
        </>
      )}
    </div>
  )
};

export default Hero;
