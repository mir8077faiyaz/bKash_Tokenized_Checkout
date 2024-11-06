# Description:
bKash's tokenized checkout provides the customers a more convenient way of payment. Using this product, the customers can create an agreement in merchant websites/apps that for further payment using bKash, they will only use bkash wallet PIN. In this case the merchant system needs to store these agreements against different user accounts. This provides a faster and convenient payment opportunity for both the merchant and the customer.

# Installation:
1. Create virtual environment.
2. Clone/Download the project file.
3. Install requirements.txt

# File Tree
project/ ├── app.py # Main application file where the core logic resides ├── agreement.py # Handles the agreement-related functionalities ├── auth.py # Authentication and user login logic ├── config.py # Configuration file for settings and constants ├── globals.py # Global variables or constants shared across modules ├── payment.py # Payment processing functionality ├── utils.py # Utility functions and helpers ├── Static/ # Directory for static files │ ├── r1.jpg # Image file used in the app │ ├── r2.jpg # Image file used in the app │ ├── rocket.png # Another image file used in the app │ └── style.css # CSS file for styling the front-end └── Templates/ # Directory for HTML templates ├── index.html # Homepage template ├── bind.html # Template for binding user actions ├── purchases.html # Template to display purchases ├── query.html # Template for querying information ├── queryag.html # Template for querying agreements ├── refund.html # Template for processing refunds └── search.html # Template for search functionality
  
