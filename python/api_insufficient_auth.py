# VULNERABLE CODE
from flask import Flask, request
app = Flask(__name__)

@app.route('/api/sell-gold', methods=['POST'])
def sell_gold():
    user_id = request.json.get('user_id')
    amount = request.json.get('amount')
    # Missing: No verification if authenticated user owns this account
    return process_gold_sale(user_id, amount)