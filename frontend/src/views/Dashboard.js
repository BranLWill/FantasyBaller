import React, { useState, useEffect  } from "react";
import { Button, Alert } from "reactstrap";
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";
import { getConfig } from "../config";
import Loading from "../components/Loading";
import Card from "../components/Card";

export const DashboardComponent = () => {
  const { apiOrigin = "http://127.0.0.1:5000", audience } = getConfig();

  const [state, setState] = useState({
    showResult: false,
    apiMessage: "",
    error: null,
  });

  useEffect(() => {
    // Call your function here
    callApi();
  }, []);

  const {
    getAccessTokenSilently,
    loginWithPopup,
    getAccessTokenWithPopup,
  } = useAuth0();

  const handleConsent = async () => {
    try {
      await getAccessTokenWithPopup();
      setState({
        ...state,
        error: null,
      });
    } catch (error) {
      setState({
        ...state,
        error: error.error,
      });
    }

    await callApi();
  };

  const handleLoginAgain = async () => {
    try {
      await loginWithPopup();
      setState({
        ...state,
        error: null,
      });
    } catch (error) {
      setState({
        ...state,
        error: error.error,
      });
    }

    await callApi();
  };

  const callApi = async () => {
    console.log("PRESSED DA BUTTON")
    let random_page_num = Math.floor(Math.random() * 324) + 1;

    try {
      const token = await getAccessTokenSilently();

      const response = await fetch(
        `${apiOrigin}/api/players/cards?page_num=${random_page_num}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      console.log(response.ok)
      const responseData = await response.json();
      console.log(responseData)

      setState({
        ...state,
        showResult: true,
        apiMessage: responseData,
      });
    } catch (error) {
      setState({
        ...state,
        error: error.error,
      });
    }
  };

  const handle = (e, fn) => {
    e.preventDefault();
    fn();
  };

  return (
    <>
      <div className="mb-5">
        {state.error === "consent_required" && (
          <Alert color="warning">
            You need to{" "}
            <a
              href="#/"
              class="alert-link"
              onClick={(e) => handle(e, handleConsent)}
            >
              consent to get access to users api
            </a>
          </Alert>
        )}

        {state.error === "login_required" && (
          <Alert color="warning">
            You need to{" "}
            <a
              href="#/"
              class="alert-link"
              onClick={(e) => handle(e, handleLoginAgain)}
            >
              log in again
            </a>
          </Alert>
        )}

        <h1>Player Portal</h1>

        {!audience && (
          <Alert color="warning">
            <p>
              You can't call the API at the moment because your application does
              not have any configuration for <code>audience</code>, or it is
              using the default value of <code>YOUR_API_IDENTIFIER</code>. You
              might get this default value if you used the "Download Sample"
              feature of{" "}
              <a href="https://auth0.com/docs/quickstart/spa/react">
                the quickstart guide
              </a>
              , but have not set an API up in your Auth0 Tenant. You can find
              out more information on{" "}
              <a href="https://auth0.com/docs/api">setting up APIs</a> in the
              Auth0 Docs.
            </p>
            <p>
              The audience is the identifier of the API that you want to call
              (see{" "}
              <a href="https://auth0.com/docs/get-started/dashboard/tenant-settings#api-authorization-settings">
                API Authorization Settings
              </a>{" "}
              for more info).
            </p>

            <p>
              In this sample, you can configure the audience in a couple of
              ways:
            </p>
            <ul>
              <li>
                in the <code>src/index.js</code> file
              </li>
              <li>
                by specifying it in the <code>auth_config.json</code> file (see
                the <code>auth_config.json.example</code> file for an example of
                where it should go)
              </li>
            </ul>
            <p>
              Once you have configured the value for <code>audience</code>,
              please restart the app and try to use the "Ping API" button below.
            </p>
          </Alert>
        )}

        <Button
          color="primary"
          className="mt-5"
          onClick={callApi}
          disabled={!audience}
        >
          Get Cards
        </Button>
      </div>

      <div className="card-area" style={{ display: "flex", flexWrap: "wrap", gap: "25px", paddingTop: "50px", paddingRight: "50px", paddingBottom: "50px", paddingLeft: "50px" }}>
        {Object.entries(state.apiMessage).map(([key, value]) => {
          return (
            <Card
              name={value.display_name}
              headshot={value.headshot_url}
              // borderColor={"red"}
            />
          );
        })}
      </div>
    </>
  );
};

export default withAuthenticationRequired(DashboardComponent, {
  onRedirecting: () => <Loading />,
});
