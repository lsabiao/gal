<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Gal</title>
    <style>
      body{
        margin:0px;
        background-color: black;
        overflow-y:hidden;
      }
      #img{
        background-image: url('/static/{{file}}');
        background-repeat: no-repeat;
        background-position: center;
        background-size: contain;
        height: 100vh;
      }
      video{
        width:100%;
        height:100vh;
        object-fit: contain;
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
