# AUTOGENERATED! DO NOT EDIT! File to edit: ../../notebooks/API_Client.ipynb.

# %% auto 0
__all__ = ['Client']

# %% ../../notebooks/API_Client.ipynb 4
from typing import *

# %% ../../notebooks/API_Client.ipynb 5
import os
import importlib
import urllib.parse
import json
import secrets

from fastcore.foundation import patch
import pandas as pd

import airt
from airt.logger import get_logger, set_level
from airt.helper import get_data, post_data, delete_data, get_base_url
from airt.constant import (
    SERVICE_USERNAME,
    SERVICE_PASSWORD,
    SERVER_URL,
    CLIENT_NAME,
    SERVICE_TOKEN,
)

# %% ../../notebooks/API_Client.ipynb 7
logger = get_logger(__name__)

# %% ../../notebooks/API_Client.ipynb 10
def _get_credentials(
    username: Optional[str] = None, password: Optional[str] = None
) -> Tuple[(str, str)]:
    """Returns the value for username and password.

    If username is **None**, retrive the value from AIRT_SERVICE_USERNAME environment variable.
    If password is **None**, retrive the value from AIRT_SERVICE_PASSWORD environment variable.

    Args:
        username: Username for your developer account.
        password: Password for your developer account.

    Returns:
        The values for username and password as a tuple.

    Raises:
        Key Error, if the environment variables are not set.
    """

    username = username if username is not None else os.environ.get(SERVICE_USERNAME)

    password = password if password is not None else os.environ.get(SERVICE_PASSWORD)

    if not username and not password:
        raise KeyError(
            f"The username and password are neither passed as parameters nor set in the environment variables "
            f"`{SERVICE_USERNAME}` and `{SERVICE_PASSWORD}`."
        )

    elif not username:
        raise KeyError(
            f"The username is neither passed as parameter nor set in the environment variable {SERVICE_USERNAME}."
        )

    elif not password:
        raise KeyError(
            f"The password is neither passed as parameter nor set in the environment variable {SERVICE_PASSWORD}."
        )

    return (username, password)

# %% ../../notebooks/API_Client.ipynb 15
class Client:
    """A class for authenticating and accessing the airt service.

    To access the airt service, you must first create a developer account. To obtain one, please contact us at [info@airt.ai](mailto:info@airt.ai).

    After successful verification, you will receive an email with the username and password for the developer account.

    Once you have the credentials, use them to get an access token by calling `get_token` method. It is necessary to get
    an access token; otherwise, you won't be able to access all of the airt service's APIs. You can either pass the username, password, and server
    address as parameters to the `get_token` method or store them in the environment variables **AIRT_SERVICE_USERNAME**,
    **AIRT_SERVICE_PASSWORD**, and **AIRT_SERVER_URL**.

    In addition to the regular authentication with credentials, you can also enable multi-factor authentication (MFA) and single sign-on (SSO)
    for generating tokens.

    To help protect your account, we recommend that you enable multi-factor authentication (MFA). MFA provides additional security by requiring
    you to provide unique verification code (OTP) in addition to your regular sign-in credentials when performing critical operations.

    Your account can be configured for MFA in just two easy steps:

    1. To begin, you need to enable MFA for your account by calling the `User.enable_mfa` method, which will generate a QR code. You can then
    scan the QR code with an authenticator app, such as Google Authenticator and follow the on-device instructions to finish the setup in your smartphone.

    2. Finally, activate MFA for your account by calling `User.activate_mfa` and passing the dynamically generated six-digit verification code from your
    smartphone's authenticator app.

    After activating MFA for your account, you must pass the dynamically generated six-digit verification code, along with your username and password,
    to the `get_token` method to generate new tokens.

    Single sign-on (SSO) can be enabled for your account in three simple steps:

    1. Enable the SSO for a provider by calling the `User.enable_sso` method with the SSO provider name and an email address. At the moment,
    we only support **"google"** and **"github"** as SSO providers. We intend to support additional SSO providers in future releases.

    2. Before you can start generating new tokens with SSO, you must first authenticate with the SSO provider. Call the `get_token` with
    the same SSO provider you have enabled in the step above to generate an SSO authorization URL. Please copy and paste it into your
    preferred browser and complete the authentication process with the SSO provider.

    3. After successfully authenticating with the SSO provider, call the `set_sso_token` method to generate a new token and use it automatically
    in all future interactions with the airt server.

    Here's an example of how to use the Client class to authenticate and display the details of the currently logged-in user.

    Example:
        ```python
        # Importing necessary libraries
        from  airt.client import Client, User

        # Authenticate
        # MFA enabled users must pass the OTP along with the username and password
        # to the get_token method.
        Client.get_token(username="{fill in username}", password="{fill in password}")

        # Print the logged-in user details
        print(User.details())
        ```
    """

    server: Optional[str] = None
    auth_token: Optional[str] = None
    sso_authorization_url: Optional[str] = None

    def __init__(
        self,
        server: str,
        auth_token: str,
        sso_authorization_url: Optional[str] = None,
    ):
        Client.server = server
        Client.auth_token = auth_token
        Client.sso_authorization_url = sso_authorization_url

    @classmethod
    def get_token(  # type: ignore
        cls,
        *,
        username: Optional[str] = None,
        password: Optional[str] = None,
        server: Optional[str] = None,
        sso_provider: Optional[str] = None,
        otp: Optional[str] = None,
    ) -> Optional[str]:
        """Get application token for airt service from a username/password pair.

        This methods validates the developer credentials and returns an auth token. The returned auth
        token is implicitly used in all the interactions with the server.

        If you've already enabled multi-factor authentication (MFA) for your account, you'll need to
        pass the dynamically generated six-digit verification code along with your username and
        password to generate new tokens.

        If the token is requested using Single sign-on (SSO), an authorization URL will be returned.
        Please copy and paste it into your preferred browser and complete the SSO provider
        authentication within 10 minutes. Otherwise, the SSO login will time out and you will need
        to re-request the token.

        Args:
            username: Username for the developer account. If None (default value), then the value from
                **AIRT_SERVICE_USERNAME** environment variable is used.
            password: Password for the developer account. If None (default value), then the value from
                **AIRT_SERVICE_PASSWORD** environment variable is used.
            server: The airt server uri. If None (default value), then the value from **AIRT_SERVER_URL** environment variable
                is used. If the variable is not set as well, then the default public server will be used. Please leave this
                setting to default unless you are running the service in your own server (please email us to info@airt.ai
                for that possibility).
            sso_provider: Name of the Single sign-on (SSO) provider. Please pass this parameter only if you have successfully
                enabled SSO for this provider. At present, the API only supports "google" and "github" as valid SSO providers.
            otp: Dynamically generated six-digit verification code from the authenticator app or the OTP you have received via SMS.

        Returns:
            The authorization url if the token is requested using Single sign-on (SSO).

        Raises:
            ValueError: If the username/password pair does not match.
            ConnectionError: If the server address is invalid or not reachable.
            KeyError: If username/password is neither passed as parameters nor stored in environment variables.

        Here's an example of a non-MFA user authenticating and generating a new token

        Example:
            ```python
            # Importing necessary libraries
            from  airt.client import User, Client

            # Authenticate
            Client.get_token(username="{fill in username}", password="{fill in password}")

            # Print the logged-in user details
            print(User.details())
            ```

        Here's an example of a MFA user authenticating using SMS OTP and generating a new token

        Example:
            ```python
            # Importing necessary libraries
            from  airt.client import Client, User

            # Request OTP via SMS to authenticate
            # If you want to use the OTP from the authenticator app, skip this step and
            # don't generate an SMS OTP; instead, pass the OTP from the authenticator
            # app to the get_token method below
            username="{fill in username}"
            User.send_sms_otp(
                username=username,
                message_template_name="get_token" # Don't change the message_template_name
            )

            # Authenticate using SMS OTP
            # The send_sms_otp method will send the OTP via SMS to the registered
            # phone number, which you must fill below
            password="{fill in password}"
            otp="{fill in otp}"
            Client.get_token(username=username, password=password, otp=otp)

            # Print the logged-in user details
            print(User.details())
            ```
        """
        cls.server = get_base_url(server)

        username, password = _get_credentials(username, password)

        if otp is not None:
            password = json.dumps({"password": password, "user_otp": otp})

        if sso_provider is None:
            response = post_data(
                url=f"{cls.server}/token",
                data=dict(username=username, password=password),
                token=None,
            )

            cls.auth_token = response["access_token"]
        else:
            response = post_data(
                url=f"{cls.server}/sso/initiate",
                data=json.dumps(  # type: ignore
                    dict(
                        username=username, password=password, sso_provider=sso_provider
                    )
                ),
                token=None,
            )

            cls.sso_authorization_url = response["authorization_url"]
            return cls.sso_authorization_url

    @classmethod
    def set_sso_token(cls):
        """Set the application token generated using Single sign-on (SSO).

        The token set using this method will be implicitly used in all the interactions with the server.

        Please call this method only if you successfully enabled and completed the login with the Single
        sign-on (SSO) provider. If not, please call the `get_token` method with an appropriate
        sso_provider to initiate the SSO authentication.

        Here's an example of authenticating with Single sign-on (SSO) using google and setting the
        newly generated token to interact with the airt service.

        Example:
            ```python
            # Importing necessary libraries
            from  airt.client import Client, User

            # Authenticate
            Client.get_token(username="{fill in username}", password="{fill in password}")

            # Enable single sign-on (SSO) and use google as the provider
            sso_provider="google"
            sso_email="{fill in sso_email}"
            User.enable_sso(sso_provider=sso_provider, sso_email=sso_email)

            # Authenticate using Single sign-on (SSO)
            # To generate a token using SSO, you must first authenticate with the provider.
            # The command below will generate an authorization URL for you.
            # Please copy and paste it into your preferred browser and complete the
            # SSO provider authentication within 10 minutes. Otherwise, the SSO login
            # will time out and you will need to call the get_token method again.
            sso_url = Client.get_token(sso_provider=sso_provider)
            print(sso_url)

            # Once the provider authentication is successful, call the below method to
            # set the generated token
            Client.set_sso_token()

            # If set_sso_token fails, the line below will throw an error.
            print(User.details())
            ```
        """
        quoted_authorization_url = urllib.parse.quote(cls.sso_authorization_url)
        response = get_data(
            url=f"{cls.server}/sso/token/?authorization_url={quoted_authorization_url}",
            token=None,
        )

        cls.auth_token = response["access_token"]

    @classmethod
    def set_token(cls, token: Optional[str] = None, server: Optional[str] = None):
        """Set application token for airt service.

        If you already have a valid token, you can call this method to set it and use it in all
        subsequent interactions with the airt server.

        Please call this method only if you already have a token. If not, please call the `get_token` method to generate one.

        Args:
            token: The application token obtained by calling the `get_token` method, or an APIKey obtained by calling
                the `APIKey.create` method. If None (default value), then the value from **AIRT_SERVICE_TOKEN** environment variable is used.
            server: The airt server uri. If None (default value), then the value from **AIRT_SERVER_URL** environment variable
                is used. If the variable is not set as well, then the default public server will be used. Please leave this
                setting to default unless you are running the service in your own server (please email us to info@airt.ai
                for that possibility).

        An example to set an existing token:

        Example:
            ```python
            # Importing necessary libraries
            from  airt.client import Client, User

            # Optional Step: For demonstration purpose, generate a new token
            # When you generate a new token with the get_token method, you do not
            # need to explicitly call set_token. It is shown here for demo purposes only.
            # Skip this step if you already have a valid token and pass it directly to
            # the set_token method below
            Client.get_token(username="{fill in username}", password="{fill in password}")

            # Setting a valid token
            Client.set_token(token=Client.auth_token)

            # If set_token fails, the line below will throw an error.
            print(User.details())
            ```
        """

        auth_token = token if token is not None else os.environ.get(SERVICE_TOKEN)

        if not auth_token:
            raise KeyError(
                f"The token is neither passed as parameter nor set in the environment variable {SERVICE_TOKEN}."
            )

        cls.auth_token = auth_token
        cls.server = get_base_url(server)

    @staticmethod
    def version() -> dict:
        """Return the client and server versions.

        Returns:
            A dict containing the client and server versions.

        Raises:
            ConnectionError: If the server address is invalid or not reachable.

        An example to get the client and server versions:

        Example:
            ```python
            # Importing necessary libraries
            from  airt.client import Client

            # Get the client and server versions
            print(Client.version())
            ```
        """

        response = Client._get_data(relative_url=f"/version")

        version = {
            # nosemgrep: python.lang.security.audit.non-literal-import.non-literal-import
            "client": importlib.import_module(CLIENT_NAME).__version__,
            "server": response["airt_service"],
        }

        return version

    @classmethod
    def _get_server_url_and_token(cls) -> Tuple[Optional[str], Optional[str]]:
        """Fetch the server URL and the auth token.

        Returns:
            A tuple containing server URL and auth token.
        """

        cls.server = get_base_url(cls.server)

        return cls.server, cls.auth_token

    @classmethod
    def _post_data(
        cls,
        relative_url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a POST request.

        This method will implicitly add the server base URL and the token for every request.

        Args:
            relative_url: The relative URL of the server's API endpoint.
            data: A Dictionary object to send in the body of the POST request. The data sent in this param will automatically be form-encoded by the request library.
            json: A Dictionary object to send in the body of the POST request. The data sent in this param will automatically be JSON-encoded by the request library.

        Returns:
            Response body as a dictionary.

        Raises:
            ConnectionError: If the server is not reachable.
            ValueError: If the response code is not in range of 200 - 399.
        """

        server, auth_token = Client._get_server_url_and_token()

        return post_data(
            url=f"{server}{relative_url}",
            data=data,
            json=json,
            token=auth_token,
        )

    @classmethod
    def _get_data(cls, relative_url: str) -> Any:
        """Make a GET request.

        This method will implicitly add the server base URL and the token for every request.

        Args:
            relative_url: The relative URL of the API endpoint.

        Returns:
            A dictionary that encapsulates the response body.

        Raises:
            ConnectionError: If the server is not reachable.
            ValueError: If the response code is not in range of 200 - 399.
        """

        server, auth_token = Client._get_server_url_and_token()

        return get_data(url=f"{server}{relative_url}", token=auth_token)

    @classmethod
    def _delete_data(cls, relative_url: str) -> Dict[str, Any]:
        """Make a DELETE request.

        This method will implicitly add the server base URL and the token for every request.

        Args:
            relative_url: The relative URL of the API endpoint.

        Returns:
            A dictionary that encapsulates the response body.

        Raises:
            ConnectionError: If the server is not reachable.
            ValueError: If the response code is not in range of 200 - 399.
        """

        server, auth_token = Client._get_server_url_and_token()

        return delete_data(url=f"{server}{relative_url}", token=auth_token)
