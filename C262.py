<html>
<head>
<style>

    body {
        text-align: center;
        margin-top: 50px;
        font-size: 25px;
    }

    h1 {
         color: red;
    }

</style>
</head>


<body>
    <h1>Covid Stats!</h1><br>
    <form method="POST">
        <label >Enter a Country Code</label><br><br>
    <input placeholder="Country Code" name="text">
    <input type="submit">
</form>
    <img src="{{image }}">


    <p>You have {{ count }} Visitors.</p>
</body>
</html>