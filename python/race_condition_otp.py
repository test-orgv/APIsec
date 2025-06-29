# VULNERABLE CODE
def validate_otp(user_id, otp):
    stored_otp = get_otp_from_cache(user_id)
    if stored_otp == otp:
        delete_otp_from_cache(user_id)  # Race condition here
        return True
    return False
# Multiple requests could use same OTP before deletion