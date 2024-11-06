# config.py

class Config:
    """Store sensitive configuration values."""
    USERNAME = "<your_username>"
    PASSWORD = "<your_password>"
    APP_KEY = "<your_app_key>"
    APP_SECRET = "<your_app_secret>"
    X_APP_KEY = "<your_x_app_key>"
    FLASK_KEY = "<your_flask_key>"
    
    # API URLs
    GRANT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/token/grant"
    REFRESH_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/token/refresh"
    CREATE_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/create"
    EXEC_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/execute"
    QUERY_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/payment/status"
    SEARCH_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/general/searchTransaction"
    REFUND_PAYMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/payment/refund"
    CREATE_AGREEMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/create"
    EXEC_AGREEMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/execute"
    QUERY_AGREEMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/agreement/status"
    CANCEL_AGREEMENT_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/agreement/cancel"
    
    # Data file paths
    purchase_data_file = "<path_to_purchases_file>"
    agreement_data_file = "<path_to_agreement_file>"
