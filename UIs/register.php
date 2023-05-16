<!DOCTYPE html>
<html>
<head>
	<title>User Registration Form</title>
	<style>
		body {
			font-family: Arial, sans-serif;
		}
		form {
			max-width: 500px;
			margin: auto;
		}
		input[type=text], input[type=password], input[type=email] {
			width: 100%;
			padding: 12px 20px;
			margin: 8px 0;
			display: inline-block;
			border: 1px solid #ccc;
			border-radius: 4px;
			box-sizing: border-box;
		}
		button {
			background-color: #4CAF50;
			color: white;
			padding: 14px 20px;
			margin: 8px 0;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			width: 100%;
		}
		button:hover {
			background-color: #45a049;
		}
	</style>
	<link rel="stylesheet" href="navbar-style.css">
</head>
<body>
	<?php include('navbar.php'); ?>
	<form>
		<h2>User Registration Form</h2>
		<label for="username">Username</label>
		<input type="text" id="username" name="username" required>

		<label for="email">Email</label>
		<input type="email" id="email" name="email" required>

		<label for="password">Password</label>
		<input type="password" id="password" name="password" required>

		<button type="submit">Register</button>
	</form>
</body>
</html>
