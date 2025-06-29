// VULNERABLE CODE
<?php
$user_id = $_POST['user_id']; // Hacker can manipulate this
$sql = "SELECT * FROM gold_accounts WHERE user_id = " . $user_id;
?>