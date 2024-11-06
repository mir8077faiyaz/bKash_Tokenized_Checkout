# payment.py

import requests
from utils import *
from auth import *
from config import Config

def create_payment(price, callback_url):
    """
    Create a new tokenzied payment with price.

    Args:
        price (str): The amount to be paid.
        callback_url (str): The URL for payment status callback.

    Returns:
        str: URL for bKash payment if successful; otherwise an error message.
    """
    agreement_id=None
    id_token = grant_token()
    if id_token:
        agreements=load_agreement()
        for agreement in agreements:
            if agreement["payerReference"]=="01619777283" or agreement["payerReference"]=="01619777282":
                agreement_id=agreement["agreementID"]
        
        if agreement_id:
            create_url = Config.CREATE_PAYMENT_URL
            create_headers = {
                "authorization": id_token,
                "x-app-key": Config.X_APP_KEY,
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            create_body = {
                "mode": "0001",
                "payerReference": "01619777283",
                "callbackURL": callback_url,
                "merchantAssociationInfo": "MI05MID54RF09123456One",
                "agreementID":agreement_id,
                "amount": price,
                "currency": "BDT",
                "intent": "sale",
                "merchantInvoiceNumber": "Inv0124"
            }
            response = requests.post(create_url, json=create_body, headers=create_headers)
            if response.status_code == 200:
                data = response.json()
                return data.get("bkashURL")
        else:
            create_url = Config.CREATE_PAYMENT_URL
            create_headers = {
                "authorization": id_token,
                "x-app-key": Config.X_APP_KEY,
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            create_body = {
                "mode": "0011",
                "payerReference": "01619777283",
                "callbackURL": callback_url,
                "merchantAssociationInfo": "MI05MID54RF09123456One",
                "amount": price,
                "currency": "BDT",
                "intent": "sale",
                "merchantInvoiceNumber": "Inv0124"
            }
            response = requests.post(create_url, json=create_body, headers=create_headers)
            if response.status_code == 200:
                data = response.json()
                return data.get("bkashURL")

    return None

def execute_payment(payment_id):
    """
    Execute a payment using its ID.

    Args:
        payment_id (str): The payment ID to be executed.

    Returns:
        dict: Payment execution details if successful; otherwise None.
    """
    id_token = grant_token()
    exec_url = Config.EXEC_PAYMENT_URL
    exec_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "authorization": id_token,
        "x-app-key": Config.X_APP_KEY
    }
    exec_body = {"paymentID": payment_id}
    response = requests.post(exec_url, json=exec_body, headers=exec_headers)
    if response.status_code == 200:
        return response.json()
    return None

def query_payment(payment_id):
    """
    Query the status of a payment.

    Args:
        payment_id (str): The payment ID to query.

    Returns:
        dict: Payment status details if successful; otherwise None.
    """
    id_token = grant_token()
    query_url = Config.QUERY_PAYMENT_URL
    query_headers = {
        "authorization": id_token,
        "x-app-key": Config.X_APP_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    query_body = {"paymentID": payment_id}
    response = requests.post(query_url, json=query_body, headers=query_headers)
    if response.status_code == 200:
        return response.json()
    return None

def search_payment(transaction_id):
    """
    Search for a transaction by ID.

    Args:
        transaction_id (str): The transaction ID to search.

    Returns:
        dict: Transaction details if found; otherwise None.
    """
    id_token = grant_token()
    search_url = Config.SEARCH_PAYMENT_URL
    search_headers = {
        "authorization": id_token,
        "x-app-key": Config.X_APP_KEY,
        "Accept": "application/json",
    }
    search_body = {"trxID": transaction_id}
    response = requests.post(search_url, json=search_body, headers=search_headers)
    if response.status_code == 200:
        return response.json()
    return None

def refund_payment(payment_id, refund_amount, transaction_id, sku, reason):
    """
    Refund a payment.

    Args:
        payment_id (str): The payment ID to refund.
        refund_amount (str): The amount to refund.
        transaction_id (str): The transaction ID associated with the payment.
        sku (str): SKU of the item being refunded.
        reason (str): Reason for refund.

    Returns:
        dict: Refund details if successful; otherwise None.
    """
    id_token = grant_token()
    refund_url = Config.REFUND_PAYMENT_URL
    refund_headers = {
        "authorization": id_token,
        "x-app-key":Config.X_APP_KEY,
        "Accept": "application/json",
    }
    refund_body = {
        "paymentID": payment_id,
        "amount": refund_amount,
        "trxID": transaction_id,
        "sku": sku,
        "reason": reason
    }
    response = requests.post(refund_url, json=refund_body, headers=refund_headers)
    if response.status_code == 200:
        return response.json()
    return None
