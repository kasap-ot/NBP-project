<!DOCTYPE html>
<html>
<head>
	<title>Internship Offer</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			padding: 20px;
		}
		.container {
			max-width: 800px;
			margin: 0 auto;
			display: flex;
			flex-wrap: wrap;
			justify-content: space-between;
			align-items: center;
			text-align: center;
		}
		.offer-info {
			width: 100%;
			margin-bottom: 20px;
			border: 2px solid #ccc;
			border-radius: 5px;
			padding: 20px;
			box-sizing: border-box;
		}
		.offer-info h2 {
			margin-top: 0;
			margin-bottom: 10px;
			font-size: 24px;
		}
		.offer-info p {
			margin: 0;
			margin-bottom: 15px;
			font-size: 18px;
			font-weight: bold;
			text-align: left;
			padding: 5px;
			border-bottom: 1px solid #ccc;
			box-sizing: border-box;
		}
		.offer-info p:last-of-type {
			border-bottom: none;
			margin-bottom: 0;
		}
		.offer-info span {
			font-weight: normal;
			margin-left: 10px;
		}
		.offer-info a {
			text-decoration: none;
			color: #4CAF50;
		}
	</style>
	<link rel="stylesheet" href="navbar-style.css">
</head>
<body>
	<?php include('navbar.php'); ?>
	<div class="container">
		<div class="offer-info">
			<h2>Internship Offer</h2>
				<p>Field of study: <span>Computer Science</span></p>
				<p>Company Name: <span>XYZ Corporation</span></p>
				<p>Address of Company: <span>123 Main St, Anytown, USA</span></p>
				<p>Link to Company Website: <span><a href="https://www.xyzcorp.com" target="_blank">www.xyzcorp.com</a></span></p>
				<p>Work Offered: <span>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span></p>
				<p>Requirements: <span>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span></p>
				<p>Salary: <span>$50,000</span></p>
				<p>Start Date: <span>June 1, 2023</span></p>
				<p>Length in Weeks: <span>12</span></p>
				<p>Accommodation Type: <span>Shared Apartment</span></p>
				<p>Accommodation Address: <span>456 Elm St, Anytown, USA</span></p>
				<p>Deadline for Application: <span>May 15, 2023</span></p>
		</div>
	</div>
</body>
</html>
