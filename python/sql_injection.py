# VULNERABLE CODE
user_input = "1 OR 1=1"  # Example input
query = f"UPDATE accounts SET gold_balance = 0 WHERE user_id = {user_input}"
# Results in: UPDATE accounts SET gold_balance = 0 WHERE user_id = 1 OR 1=1