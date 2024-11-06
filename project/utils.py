# utils.py

import json
import os
from config import Config



def load_purchases():
    """Load purchases from JSON file if it exists."""
    if os.path.exists(Config.purchase_data_file):
        with open(Config.purchase_data_file, 'r') as file:
            return json.load(file)
    return []

def save_purchase(purchase, product):
    """Save a new purchase to the JSON file with product name."""
    purchases = load_purchases()
    purchase['product'] = product
    purchases.append(purchase)
    with open(Config.purchase_data_file, 'w') as file:
        json.dump(purchases, file, indent=4)

def load_agreement():
    """Load agreements from JSON file if it exists."""
    if os.path.exists(Config.agreement_data_file):
        with open(Config.agreement_data_file, 'r') as file:
            return json.load(file)
    return []

def save_agreement(agreement):
    """Save a new agreement to the JSON file."""
    agreements = load_agreement()
    agreements.append(agreement)
    with open(Config.agreement_data_file, 'w') as file:
        json.dump(agreements, file, indent=4)

def remove_agreement(agreement_id):
    """Remove an agreement by its ID."""
    agreements = load_agreement()
    
    # Filter out the agreement with the specified ID, skipping entries without 'agreementID'
    updated_agreements = [
        agreement for agreement in agreements 
        if agreement.get('agreementID') != agreement_id
    ]

    # Only save if there are changes
    if len(agreements) != len(updated_agreements):
        # Since save_agreement appends, we will save the entire updated list
        with open(Config.agreement_data_file, 'w') as file:
            json.dump(updated_agreements, file, indent=4)
        print(f"Agreement with ID {agreement_id} has been removed.")
    else:
        print(f"No agreement found with ID {agreement_id}.")