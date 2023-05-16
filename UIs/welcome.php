<!DOCTYPE html>
<html>
<head>
	<title>Welcome to My Website</title>
	<style>
		body {
			font-family: Arial, sans-serif;
		}
		h1 {
			margin-top: 50px;
		}
		button {
			background-color: #4CAF50;
			color: white;
			padding: 14px 20px;
			margin: 8px 0;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			width: 200px;
			font-size: 20px;
		}
		button:hover {
			background-color: #45a049;
		}
	</style>
	<link rel="stylesheet" href="navbar-style.css">
</head>
<body>
	<?php include('navbar.php'); ?>
	<h1>Welcome to APLIPRAKSA!</h1>
	<p>Please select an option below to continue:</p>
	<button onclick="window.location.href='register.html'">Register</button>
	<button onclick="window.location.href='login.html'">Login</button>
</body>
</html>
