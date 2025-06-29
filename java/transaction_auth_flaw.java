// VULNERABLE CODE
public void sellGold(String userId, double amount) {
    // No check if current user can access this userId's account
    GoldAccount account = database.getAccount(userId);
    account.sellGold(amount);
    transferFunds(amount, targetAccount);
}