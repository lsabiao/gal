<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Gal</title>
    <style>
      body{margin:0px;background-color: black;}
      #img{
        background-image: url('/static/{{file}}');
        background-repeat: no-repeat;
        background-position: center;
        background-size: contain;
        height: 100vh;
      }
      video{
        object-fit: cover;
    }

    </style>
  </head>
  <body>
    {{!content}}

    <script>
      document.body.addEventListener('keypress', next);
      document.body.addEventListener('click', next);

      function next(){
        location.reload();
      }
    </script>
  </body>
</html>