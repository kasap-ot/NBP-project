<!DOCTYPE html>
<html>
<head>
	<title>All users</title>
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
	<br>
	<div class="container">
		<!-- <div class="navbar">
			<ul>
				<li><a href="#insertpagename">Availble offers</a></li>
				<li><a href="#insertpagename">Waiting for response</a></li>
				<li><a href="#insertpagename">Accepted</a></li>
				<li><a href="#insertpagename">Ongoing</a></li>
				<li><a href="#insertpagename">Completed</a></li>
			</ul>
		</div> -->
		<h1>All users</h1>
		<table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Surname</th>
                    <th>Date of birth</th>
                    <th>Country</th>
                    <th>Faculty</th>
                    <th>Study level</th>
                    
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>John</td>
                    <td>Doe</td>
                    <td>1995-08-10</td>
                    <td>USA</td>
                    <td>Computer Science</td>
                    <td>Bachelor</td>
                </tr>
                <tr>
                    <td>Jane</td>
                    <td>Smith</td>
                    <td>1998-03-15</td>
                    <td>Canada</td>
                    <td>Business Administration</td>
                    <td>Master</td>
                </tr>
                <tr>
                    <td>David</td>
                    <td>Johnson</td>
                    <td>1992-11-25</td>
                    <td>UK</td>
                    <td>Engineering</td>
                    <td>Doctorate</td>
                </tr>
                <tr>
                    <td>John</td>
                    <td>Doe</td>
                    <td>1995-08-10</td>
                    <td>USA</td>
                    <td>Computer Science</td>
                    <td>Bachelor</td>
                </tr>
                <tr>
                    <td>Jane</td>
                    <td>Smith</td>
                    <td>1998-03-15</td>
                    <td>Canada</td>
                    <td>Business Administration</td>
                    <td>Master</td>
                </tr>
                <tr>
                    <td>David</td>
                    <td>Johnson</td>
                    <td>1992-11-25</td>
                    <td>UK</td>
                    <td>Engineering</td>
                    <td>Doctorate</td>
                </tr>
                <tr>
                    <td>John</td>
                    <td>Doe</td>
                    <td>1995-08-10</td>
                    <td>USA</td>
                    <td>Computer Science</td>
                    <td>Bachelor</td>
                </tr>
                <tr>
                    <td>Jane</td>
                    <td>Smith</td>
                    <td>1998-03-15</td>
                    <td>Canada</td>
                    <td>Business Administration</td>
                    <td>Master</td>
                </tr>
                <tr>
                    <td>David</td>
                    <td>Johnson</td>
                    <td>1992-11-25</td>
                    <td>UK</td>
                    <td>Engineering</td>
                    <td>Doctorate</td>
                </tr>
            </tbody>
        </table>

	</div>
</body>
</html>

