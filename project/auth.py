# auth.py

import requests
from config import Config
from datetime import datetime, timedelta

id_token = None
td, td_refresh = None, None
refresh_token_expiry = None 
refresh_token = None


def grant_token():
    """
    Grant a new authentication token or return the existing valid token.

    Returns:
        str: An ID token if authentication is successful; otherwise None.
    """
    global td, id_token, refresh_token, td_refresh
    if td is not None:
        elapsed=(td - datetime.now()).total_seconds() 
        print(f"Time elapsed: {elapsed}")

    # Check if `id_token` is expiring soon (less than 5 minutes left)
    if td is None or (td - datetime.now()).total_seconds() < 300:
        print("ID token expired or about to expire. Checking refresh token...")

        # Check if `refresh_token` is still valid within the 28-day window and has more than 5 minutes remaining
        # Simpler: If refresh is still valid, it is more than 28 days and has more than 5 mins remaining, go for refresh token. Otherwise grant new token.
        if refresh_token and td_refresh > datetime.now() and td_refresh - datetime.now() > timedelta(seconds=300):
            print(f"Time elapsed for refreshed: {td_refresh - datetime.now()}")
            print("Refresh token is still valid. Using refresh_token_flow.")
            return refresh_token_flow()
        
        # Grant a new token if no valid `refresh_token` or if refresh expired after 28 days
        print("Refresh token expired or about to expire. Requesting new grant token.")
        grant_url = Config.GRANT_URL
        grant_headers = {
            "username": Config.USERNAME,
            "password": Config.PASSWORD,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        grant_body = {
            "app_key": Config.APP_KEY,
            "app_secret": Config.APP_SECRET
        }

        response = requests.post(grant_url, json=grant_body, headers=grant_headers)
        if response.status_code == 200:
            data = response.json()
            id_token = data.get("id_token")
            expires_in = data.get("expires_in")
            refresh_token = data.get("refresh_token")
            td = datetime.now() + timedelta(seconds=expires_in)
            td_refresh = datetime.now() + timedelta(days=28)  # 28-day validity for refresh_token
            print("New ID token and refresh token granted.")
            return id_token
        else:
            print("Failed to grant new ID token.")
    else:
        print("ID token is still valid. Returning existing token.")
    return id_token

def refresh_token_flow():
    """
    Use the existing refresh token to get a new ID token.

    Returns:
        str: A new ID token if the refresh operation is successful; otherwise None.
    """
    global id_token, td, refresh_token, td_refresh

    refresh_url = Config.REFRESH_URL
    refresh_headers = {
        "username": Config.USERNAME,
        "password": Config.PASSWORD,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    refresh_body = {
        "app_key": Config.APP_KEY,
        "app_secret": Config.APP_SECRET,
        "refresh_token": refresh_token
    }

    response = requests.post(refresh_url, json=refresh_body, headers=refresh_headers)
    if response.status_code == 200:
        data = response.json()
        id_token = data.get("id_token")
        expires_in = data.get("expires_in")
        refresh_token = data.get("refresh_token")
        td = datetime.now() + timedelta(seconds=expires_in)
        td_refresh = datetime.now() + timedelta(days=28)  # Reset 28-day validity for new refresh_token
        print("New ID token obtained using refresh token.")
        return id_token
    else:
        # Handle cases where the refresh token may have expired after 28 days
        print("Refresh token invalid or expired. Falling back to grant_token.")
        return grant_token()
