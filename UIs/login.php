<!DOCTYPE html>
<html>
<head>
	<title>Login Form</title>
	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<link rel="stylesheet" href="navbar-style.css">
</head>
<body>
	<?php include('navbar.php'); ?>
	<div class="container">
		<form>
			<br>
			<h2 class="text-center">Login Form</h2>
			<div class="form-group">
				<label for="username">Username</label>
				<input type="text" id="username" name="username" class="form-control" required>
			</div>

			<div class="form-group">
				<label for="password">Password</label>
				<input type="password" id="password" name="password" class="form-control" required>
			</div>

			<button type="submit" class="btn btn-primary">Login</button>
		</form>
	</div>
</body>
</html>
