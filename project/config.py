# config.py

class Config:
    """Store sensitive configuration values."""
    USERNAME = "01770618567"
    PASSWORD = "D7DaC<*E*eG"
    APP_KEY = "0vWQuCRGiUX7EPVjQDr0EUAYtc"
    APP_SECRET = "jcUNPBgbcqEDedNKdvE4G1cAK7D3hCjmJccNPZZBq96QIxxwAMEx"
    X_APP_KEY="0vWQuCRGiUX7EPVjQDr0EUAYtc"
    FLASK_KEY='s1o2m3e4t5h6i7n8g9'
    GRANT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/token/grant"
    REFRESH_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/token/refresh"
    CREATE_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/create"
    EXEC_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/execute"
    QUERY_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/payment/status"
    SEARCH_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/general/searchTransaction"
    REFUND_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/payment/refund"
    CREATE_AGREEMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/create"
    EXEC_AGREEMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/execute"
    QUERY_AGREEMENT_URL="https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/agreement/status"
    CANCEL_AGREEMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/agreement/cancel"

    purchase_data_file = 'purchases.json'
    agreement_data_file= 'agreement.json'
