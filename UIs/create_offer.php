<!DOCTYPE html>
<html>
<head>
	<title>Multiple Input Fields Form</title>
	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<link rel="stylesheet" href="navbar-style.css">
</head>
<body>
	<?php include('navbar.php'); ?>
	<br>
	<h1 class="text-center">Create an offer</h1>
	<div class="container">
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
			<div class="form-group">
				<label for="field1">Field of study:</label>
				<input type="text" id="field1" name="field1" class="form-control">
			</div>
			
			<div class="form-group">
				<label for="field2">Requirements:</label>
				<input type="text" id="field2" name="field2" class="form-control">
			</div>
			
			<div class="form-group">
				<label for="field3">Responsibilities:</label>
				<input type="text" id="field3" name="field3" class="form-control">
			</div>
			
			<div class="form-group">
				<label for="field4">Benefits:</label>
				<input type="text" id="field4" name="field4" class="form-control">
			</div>
			
			<div class="form-group">
				<label for="field5">Salary:</label>
				<input type="text" id="field5" name="field5" class="form-control">
			</div>
			
			<div class="form-group">
				<label for="field6">Start date:</label>
				<input type="text" id="field6" name="field6" class="form-control">
			</div>
			
			<div class="form-group">
				<label for="field7">Duration (in weeks):</label>
				<input type="text" id="field7" name="field7" class="form-control">
			</div>
			
			<div class="form-group">
				<label for="field8">Select company:</label>
				<input type="text" id="field8" name="field8" class="form-control">
			</div>
			
			<button type="submit" class="btn btn-primary">Create</button>
		</form>
	</div>

</body>
</html>
