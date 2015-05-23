<?php
$senderAddress = $_POST['email'];
$subject = $_POST['type'];
$message = $_POST['message'];
$recipient = 'enquiries@villamaremma.co.uk';

$headers = 'From: ' . $senderAddress . "\r\n";
$headers .= 'Reply-To: ' . $senderAddress . "\r\n";
$headers .= 'Content-type: text/text; charset=iso-8859-1' . "\r\n";

if (mail($recipient, $subject, $message, $headers)) {

	header("Location: http://www.villamaremma.co.uk/thankYou.html");
} else {
	echo ('mail failure');
}
?>