
<?php
$user_id = $_POST['user_id'];
$sql = "SELECT * FROM gold_accounts WHERE user_id = " . $user_id;
echo "Query: " . $sql;
?>
