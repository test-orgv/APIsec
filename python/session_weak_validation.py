# VULNERABLE CODE
def get_current_user():
    session_token = request.headers.get('Authorization')
    # No validation of token expiry, signature, etc.
    user_data = decode_token(session_token)  # Trusts any token
    return user_data['user_id']