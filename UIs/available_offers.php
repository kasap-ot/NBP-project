<!DOCTYPE html>
<html>
<head>
	<title>Internship Offers</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			padding: 20px;
		}
		.container {
			max-width: 800px;
			margin: 0 auto;
		}
		.navbar {
			background-color: #f5f5f5;
			padding: 10px;
		}
		.navbar ul {
			list-style-type: none;
			margin: 0;
			padding: 0;
			display: flex;
		}
		.navbar li {
			margin-right: 10px;
		}
		.navbar li a {
			text-decoration: none;
			color: #333;
			padding: 5px 10px;
			border-radius: 5px;
		}
		.navbar li a:hover {
			background-color: #ddd;
		}
		table {
			border-collapse: collapse;
			width: 100%;
			margin-top: 50px;
		}
		th, td {
			text-align: left;
			padding: 8px;
			border-bottom: 1px solid #ddd;
		}
		tr:hover {
			background-color: #f5f5f5;
		}
		th {
			background-color: #4CAF50;
			color: white;
		}
		h1 {
			margin-top: 50px;
		}
	</style>
	<link rel="stylesheet" href="navbar-style.css">
</head>
<body>
	<?php include('navbar.php'); ?>
	<div class="container">
		<div class="navbar">
			<ul>
				<li><a href="available_offers.html">Availble offers</a></li>
				<li><a href="#insertpagename">Waiting for response</a></li>
				<li><a href="accepted.html">Accepted</a></li>
				<li><a href="ongoing.html">Ongoing</a></li>
				<li><a href="completed.html">Completed</a></li>
			</ul>
		</div>
		<h1>Internship Offers</h1>
		<table id="offers">
			<thead>
				<tr>
					<th>Country</th>
					<th>Field of Study</th>
					<th>Starting Date</th>
					<th>Length (in weeks)</th>
					<th>Company Name</th>
				</tr>
			</thead>
			<tbody>
				<!-- Offer rows -->
				<tr>
					<td>France</td>
					<td>Business Administration</td>
					<td>July 15, 2023</td>
					<td>8</td>
					<td>XYZ Corporation</td>
				</tr>
				<tr>
					<td>Japan</td>
					<td>Engineering</td>
					<td>August 1, 2023</td>
					<td>12</td>
					<td>DEF Inc.</td>
				</tr>
				<tr>
					<td>USA</td>
					<td>Computer Science</td>
					<td>June 1, 2023</td>
					<td>10</td>
					<td>ABC Company</td>
				</tr>
				<tr>
					<td>France</td>
					<td>Business Administration</td>
					<td>July 15, 2023</td>
					<td>8</td>
					<td>XYZ Corporation</td>
				</tr>
				<tr>
					<td>France</td>
					<td>Business Administration</td>
					<td>July 15, 2023</td>
					<td>8</td>
					<td>XYZ Corporation</td>
				</tr>
				<tr>
					<td>Japan</td>
					<td>Engineering</td>
					<td>August 1, 2023</td>
					<td>12</td>
					<td>DEF Inc.</td>
				</tr>
			</tbody>
		</table>
	</div>
</body>
</html>

