
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Insufficient Authentication/Authorization ---
@app.route('/api/sell-gold', methods=['POST'])
def sell_gold():
    user_id = request.json.get('user_id')
    amount = request.json.get('amount')
    # Missing: No verification if authenticated user owns this account
    return process_gold_sale(user_id, amount)

def process_gold_sale(user_id, amount):
    return jsonify({"message": f"Gold sale for user {user_id} processed: {amount}g"})


# --- Weak Session Validation ---
@app.route('/api/get-user', methods=['GET'])
def get_current_user():
    session_token = request.headers.get('Authorization')
    # No validation of token expiry, signature, etc.
    user_data = decode_token(session_token)  # Trusts any token
    return jsonify({"user_id": user_data['user_id']})

def decode_token(token):
    return {'user_id': 'admin'}


# --- SQL Injection ---
@app.route('/api/update-gold', methods=['GET'])
def update_gold():
    user_input = request.args.get('user_id')
    query = f"UPDATE accounts SET gold_balance = 0 WHERE user_id = {user_input}"
    return jsonify({"query": query})


# --- Race Condition OTP ---
otp_cache = {"123": "999999"}

@app.route('/api/validate-otp', methods=['POST'])
def validate_otp():
    user_id = request.json.get('user_id')
    otp = request.json.get('otp')
    stored_otp = otp_cache.get(user_id)
    if stored_otp == otp:
        del otp_cache[user_id]
        return jsonify({"status": "success"})
    return jsonify({"status": "failure"}), 403


if __name__ == '__main__':
    app.run(debug=True)
