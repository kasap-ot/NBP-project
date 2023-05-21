<!DOCTYPE html>
<html>
	<head>
		<title>Internship Offers</title>
		<!-- Bootstrap CSS -->
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
		<link rel="stylesheet" href="navbar-style.css">
	</head>
	<body>
		<?php include('navbar.php'); ?>
		<div class="container">
			<div class="navbar">
				<ul class="nav">
					<li class="nav-item">
						<a class="nav-link" href="available_offers.php">Available offers</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="waiting_for_response.html">Waiting for response</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="accepted.html">Accepted</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="ongoing.html">Ongoing</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="completed.html">Completed</a>
					</li>
				</ul>
			</div>
			<h1>Internship Offers</h1>
			<table class="table" id="offers">
				<thead class="thead-dark">
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
						<td>FRANCE GREAT</td>
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

