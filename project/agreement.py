# agreement.py

import requests
from flask import jsonify, url_for, redirect,request
from utils import *
from auth import *
from globals import *
from config import Config


def create_agreement():
    # global tokenized_flag
    callback_url = url_for('index', _external=True)
    id_token=grant_token()
    cr_agreement_url = Config.CREATE_AGREEMENT_URL
    cr_agreement_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "authorization": id_token,
        "x-app-key": Config.X_APP_KEY
    }
    cr_agreement_body = {
        "mode": "0000",
        "callbackURL": callback_url,
        "payerReference": "01619777282",
    }
    response = requests.post(cr_agreement_url, json=cr_agreement_body, headers=cr_agreement_headers)
    if response.status_code == 200:
        data = response.json()
        bkash_url=data.get("bkashURL")
        set_tokenized_flag(1)
        print(f"I have set tokenized flag to {get_tokenized_flag()}")
        return redirect(bkash_url)
    
    return jsonify({'status': 'error', 'message': 'Agreement creation failed.'}), 400

def execute_agreement(payment_id):
    """
    Execute an agreement using its payment ID.

    Args:
        payment_id (str): The payment ID to execute the agreement.

    Returns:
        dict: Agreement execution details if successful; otherwise None.
    """
    id_token = grant_token()
    exec_agreement_url = Config.EXEC_AGREEMENT_URL
    exec_agreement_headers = {
        "Accept": "application/json",
        "authorization": id_token,
        "x-app-key": Config.X_APP_KEY
    }
    exec_agreement_body = {
        "paymentID": payment_id,
    }
    response = requests.post(exec_agreement_url, json=exec_agreement_body, headers=exec_agreement_headers)
    if response.status_code == 200:
        return response.json()
    
    # Return None or an empty dictionary if execution fails
    return None

def cancel_agreement():
    # global cancel_ag_flag
    callback_url = url_for('index', _external=True)
    # might need changing since multiple users can bind.
    agreement_id=request.form.get('agreement_id')
    id_token=grant_token()
    cancel_agreement_url = Config.CANCEL_AGREEMENT_URL
    cancel_agreement_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "authorization": id_token,
        "x-app-key": Config.X_APP_KEY
    }
    cancel_agreement_body = {
        "agreementID": agreement_id,
    }
    response = requests.post(cancel_agreement_url, json=cancel_agreement_body, headers=cancel_agreement_headers)
    if response.status_code == 200:
        set_cancel_flag(1)
        remove_agreement(agreement_id)
        return redirect(callback_url) 
    return jsonify({'status': 'error', 'message': 'Agreement cancellation failed.'}), 400

def query_agreement(agreement_id):
    """
    Query the status of a agreement.

    Args:
        payment_id (str): The agreement ID to query.

    Returns:
        dict: agreement status details if successful; otherwise None.
    """
    id_token = grant_token()
    query_url = Config.QUERY_AGREEMENT_URL
    query_headers = {
        "authorization": id_token,
        "x-app-key": Config.X_APP_KEY,
        "Accept": "application/json",
    }
    query_body = {"agreementID": agreement_id}
    response = requests.post(query_url, json=query_body, headers=query_headers)
    if response.status_code == 200:
        return response.json()
    return None
