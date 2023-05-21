<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <link rel="stylesheet" href="navbar-style.css">
</head>
<body>
	<?php include('navbar.php'); ?>
    <div class="container">
        <br><br>
        <h1>Edit Profile</h1>
        <!-- 
            The users (students) should be able to edit their profiles
            and basically be able to change their credentials. The fields
            in the form are:
            - username
            - password
            - address
            - phone number
            - email
            - country
            - studies at (add/remove/edit, multiple fields)
            - experience (add/remove/edit, multiple fields)
            - certificate (add/remove/edit, multiple fields)
            - project (add/remove/edit, multiple fields)
            - language knowledge (add/remove/edit, multiple fields)
        -->
        <form>
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" placeholder="Enter your username">
        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" placeholder="Enter your password">
        </div>
        <div class="form-group">
            <label for="address">Address</label>
            <input type="text" class="form-control" id="address" placeholder="Enter your address">
        </div>
        <div class="form-group">
            <label for="phone-number">Phone number</label>
            <input type="text" class="form-control" id="phone-number" placeholder="Enter your phone number">
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" placeholder="Enter your email">
        </div>
        <div class="form-group">
            <label for="country">Country</label>
            <input type="text" class="form-control" id="country" placeholder="Enter your country">
        </div>
        <br>
        <button type="submit" class="btn btn-primary">Save</button>
        </form>
    </div>
</body>
</html>
