// VULNERABLE CODE
function sellGold(userId, amount) {
    // Direct database query without validation
    const query = `UPDATE accounts SET gold_balance = gold_balance - ${amount} WHERE user_id = ${userId}`;
    database.execute(query);
}