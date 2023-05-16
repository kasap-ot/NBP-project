<!DOCTYPE html>
<html>
<head>
	<title>All companies</title>
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
		<h1>All companies</h1>
		<table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Phone Number</th>
                    <th>Email</th>
                    <th>Address</th>
                    <th>Country</th>
                    <th>Number of Employees</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Company A</td>
                    <td>123-456-7890</td>
                    <td>companya@example.com</td>
                    <td>123 Main St</td>
                    <td>USA</td>
                    <td>100</td>
                </tr>
                <tr>
                    <td>Company B</td>
                    <td>987-654-3210</td>
                    <td>companyb@example.com</td>
                    <td>456 Elm St</td>
                    <td>Canada</td>
                    <td>50</td>
                </tr>
                <tr>
                    <td>Company C</td>
                    <td>555-123-4567</td>
                    <td>companyc@example.com</td>
                    <td>789 Oak St</td>
                    <td>Australia</td>
                    <td>200</td>
                </tr>
                <tr>
                    <td>Company A</td>
                    <td>123-456-7890</td>
                    <td>companya@example.com</td>
                    <td>123 Main St</td>
                    <td>USA</td>
                    <td>100</td>
                </tr>
                <tr>
                    <td>Company B</td>
                    <td>987-654-3210</td>
                    <td>companyb@example.com</td>
                    <td>456 Elm St</td>
                    <td>Canada</td>
                    <td>50</td>
                </tr>
                <tr>
                    <td>Company C</td>
                    <td>555-123-4567</td>
                    <td>companyc@example.com</td>
                    <td>789 Oak St</td>
                    <td>Australia</td>
                    <td>200</td>
                </tr>
                <tr>
                    <td>Company A</td>
                    <td>123-456-7890</td>
                    <td>companya@example.com</td>
                    <td>123 Main St</td>
                    <td>USA</td>
                    <td>100</td>
                </tr>
                <tr>
                    <td>Company B</td>
                    <td>987-654-3210</td>
                    <td>companyb@example.com</td>
                    <td>456 Elm St</td>
                    <td>Canada</td>
                    <td>50</td>
                </tr>
                <tr>
                    <td>Company C</td>
                    <td>555-123-4567</td>
                    <td>companyc@example.com</td>
                    <td>789 Oak St</td>
                    <td>Australia</td>
                    <td>200</td>
                </tr>
            </tbody>
        </table>

	</div>
</body>
</html>

