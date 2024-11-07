# RocketMAN
A no-database Flask based payment gateaway implmeneted using bKash Tokenized Checkout.

## Description:
bKash's tokenized checkout provides the customers a more convenient way of payment. Using this product, the customers can create an agreement in merchant websites/apps that for further payment using bKash, they will only use bkash wallet PIN. In this case the merchant system needs to store these agreements against different user accounts. This provides a faster and convenient payment opportunity for both the merchant and the customer.

## Installation:
1. Create virtual environment.
2. Clone/Download the project file.
3. Install requirements.txt <pre> pip install -r /path/to/requirements.txt <pre>

## File Tree
<pre> ``` 
  project/
├── app.py
├── agreement.py
├── auth.py
├── config.py
├── globals.py
├── payment.py
├── utils.py
├── Static/
│   ├── r1.jpg
│   ├── r2.jpg
│   ├── rocket.png
│   └── style.css
└── Templates/
    ├── index.html
    ├── bind.html
    ├── purchases.html
    ├── query.html
    ├── queryag.html
    ├── refund.html
    └── search.html
``` </pre>

## Config.py
Details of these placeholders are to be requested from bKash P&T devloper's team.
<pre>
    """Place holder for your values."""
    USERNAME = "<your_username>"
    PASSWORD = "<your_password>"
    APP_KEY = "<your_app_key>"
    APP_SECRET = "<your_app_secret>"
    X_APP_KEY = "<your_x_app_key>"
    FLASK_KEY = "<your_flask_key>"
    """Path to your json files."""
    purchase_data_file = "<path_to_purchases_file>"
    agreement_data_file = "<path_to_agreement_file>"
</pre>
