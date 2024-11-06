# app.py

from flask import Flask, render_template, request, redirect, flash
from payment import *
from agreement import *
from utils import *
from globals import *
from config import Config

app = Flask(__name__)
app.secret_key = Config.FLASK_KEY

product = None

@app.route('/')
def index():
    # global tokenized_flag
    # global cancel_ag_flag
    tokenized_flag=get_tokenized_flag()
    cancel_ag_flag=get_cancel_flag()

    print(f"THe value of tokenized flag is {tokenized_flag}")
    print(f"THe value of cancel flag is {cancel_ag_flag}")
    status = request.args.get('status')
    payment_id = request.args.get('paymentID')

    if cancel_ag_flag == 1:
        flash("Agreement was cancelled!", "success")
        # cancel_ag_flag = 0
        set_cancel_flag(0)
        return render_template('index.html')

    if tokenized_flag == 1:
        agreement_data = execute_agreement(payment_id)
        if agreement_data:
            save_agreement(agreement_data)
            # tokenized_flag = 0
            set_tokenized_flag(0)
            message = agreement_data.get("statusMessage")
            if agreement_data.get("statusCode") == "0000":
                flash("Agreement was successful!", "success")
                return render_template('index.html')
            else:
                flash(f"Agreement failed: {message} Please try again.", "danger")
                return render_template('index.html')
        else:
            # flash("Agreement execution failed. Please try again.", "danger")
            return render_template('index.html')

    if status and payment_id and tokenized_flag == 0:
        data = execute_payment(payment_id)
        if data:
            save_purchase(data, product)
            message = data.get("statusMessage")
            if data.get("statusCode") == "0000":
                flash("Payment was successful!", "success")
                return render_template('index.html')
            else:
                flash(f"Payment failed: {message} Please try again.", "danger")
                return render_template('index.html')
    
    return render_template('index.html')

@app.route('/pay', methods=['POST'])
def pay():
    global product
    product = request.form.get('product')
    price = request.form.get('price')
    callback_url = url_for('index', _external=True)
    bkash_url = create_payment(price, callback_url)
    if bkash_url:
        return redirect(bkash_url)
    return jsonify({'status': 'error', 'message': 'Payment creation failed.'}), 400

@app.route('/purchases')
def purchases():
    purchases = load_purchases()
    return render_template('purchases.html', purchases=purchases)

@app.route('/search', methods=['POST'])
def search():
    """
    Process the search form for a transaction by ID and render the search results.

    Request Form Args:
        transaction_id (str): The transaction ID to search.

    Returns:
        Response: Rendered template for search.html with transaction data.
    """
    transaction_id = request.form.get('transaction_id')
    transaction_data = search_payment(transaction_id)
    return render_template('search.html', transaction_data=transaction_data)

@app.route('/query', methods=['POST'])
def query():
    """
    Process the query form to get the payment status by payment ID and render the query results.

    Request Form Args:
        payment_id (str): The payment ID to query.

    Returns:
        Response: Rendered template for query.html with query data.
    """
    payment_id = request.form.get('payment_id')
    query_data = query_payment(payment_id)
    return render_template('query.html', query_data=query_data)

@app.route('/refund', methods=['POST'])
def refund():
    """
    Process the refund form to initiate a refund for a specific transaction and render the refund results.

    Request Form Args:
        payment_id (str): The ID of the payment to refund.
        refund_amount (str): The amount to refund.
        transaction_id (str): The transaction ID associated with the payment.
        sku (str): The SKU of the item being refunded.
        reason (str): Reason for issuing the refund.

    Returns:
        Response: Rendered template for refund.html with refund details.
    """
    payment_id = request.form.get('payment_id')
    refund_amount = request.form.get('refund_amount')
    transaction_id = request.form.get('transaction_id')
    sku = request.form.get('sku')
    reason = request.form.get('reason')

    refund_details = refund_payment(payment_id, refund_amount, transaction_id, sku, reason)
    return render_template('refund.html', refund_data=refund_details)

@app.route('/bind_bkash', methods=['POST'])
def bind_bkash():
    return create_agreement()


@app.route('/queryUnbind',methods=['POST'])
def query_bind():
    agreements=load_agreement()
    print(agreements)
    return render_template('bind.html',agreements=agreements)

@app.route('/cancel_bind', methods=['POST'])
def cancel_bind():
    # Cancel agreement logic
    return cancel_agreement()

@app.route('/qarg', methods=['POST'])
def queryarg():
    """
    Process the query form to get the agreement id and render the query results.

    Request Form Args:
        agreement_id (str): The agreement ID to query.

    Returns:
        Response: Rendered template for queryag.html with query data.
    """
    agreement_id = request.form.get('agreement_id')
    query_data = query_agreement(agreement_id)
    return render_template('queryag.html', agreement_data=query_data)

if __name__ == "__main__":
    app.run(debug=True)
