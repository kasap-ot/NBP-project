<!DOCTYPE html>
<html lang="en">
	
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Welcome to My Website</title>
	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>

<body>
	<?php include('navbar.php'); ?>
	<div class="container text-center">
		<br>	
		<h1>Welcome to My Website</h1>
		<p class="lead">Thank you for visiting!</p>
		<div class="d-grid gap-2 col-6 mx-auto">
		<a href="register.php" class="btn btn-primary">Register</a>
		<a href="login.php" class="btn btn-success">Login</a>
		</div>
	</div>
</body>

</html>
