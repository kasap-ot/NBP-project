<!DOCTYPE html>
<html>
<head>
	<title>Multiple Input Fields Form</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			padding: 20px;
		}
		form {
			display: flex;
			flex-wrap: wrap;
			justify-content: space-between;
			align-items: center;
			text-align: center;
			max-width: 800px;
			margin: 0 auto;
		}
		label {
			display: block;
			width: 100%;
			margin-bottom: 10px;
			text-align: left;
			font-weight: bold;
		}
		input[type=text], select {
			width: 100%;
			padding: 12px 20px;
			margin: 8px 0;
			box-sizing: border-box;
			border: 2px solid #ccc;
			border-radius: 4px;
			font-size: 16px;
		}
		textarea {
			width: 100%;
			height: 100px;
			padding: 12px 20px;
			margin: 8px 0;
			box-sizing: border-box;
			border: 2px solid #ccc;
			border-radius: 4px;
			font-size: 16px;
		}
		button[type=submit] {
			background-color: #4CAF50;
			color: white;
			padding: 14px 20px;
			margin: 8px 0;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			font-size: 20px;
		}
		button[type=submit]:hover {
			background-color: #45a049;
		}
		h1 {
			margin-top: 50px;
			text-align: center;
		}
	</style>
	<link rel="stylesheet" href="navbar-style.css">
</head>
<body>
	<?php include('navbar.php'); ?>
	<h1>Create an offer</h1>
	<form>
		<!-- 
			Form for offer should have:
			- field
			- requirements
			- responsibilities
			- benefits
			- salary
			- start date
			- duration in weeks
			- select company
		 -->
		<label for="field1">Field of study:</label>
		<input type="text" id="field1" name="field1">
				
		<label for="field2">Requirements:</label>
		<input type="text" id="field2" name="field2">
				
		<label for="field3">Responsibilities:</label>
		<input type="text" id="field3" name="field3">
				
		<label for="field4">Benefits:</label>
		<input type="text" id="field4" name="field4">
				
		<label for="field5">Salary:</label>
		<input type="text" id="field5" name="field5">
				
		<label for="field6">Start date:</label>
		<input type="text" id="field6" name="field6">
				
		<label for="field7">Duration (in weeks):</label>
		<input type="text" id="field7" name="field7">
				
		<label for="field8">Select company:</label>
		<input type="text" id="field8" name="field8">
				

		<button type="submit">Create</button>
	</form>
</body>
</html>
