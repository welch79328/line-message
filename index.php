<?php include( __DIR__ . "/config/file.php");?>
<!DOCTYPE html>
<html lang="tw">
    <head>
        <title></title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
    </head>
    <body>
        <div>
            <?php foreach ($db['user'] as  $v) { ?>
                <p>user name:  <?php echo $v['groupId']; ?></p>
                <p>Send line message: </p>
                <textarea id="<?php echo $v['groupId']; ?>"></textarea>
                <button onclick="oAuth2('<?php echo $v['groupId']; ?>');"> send  </button><br>
            <?php } ?>
        </div>
    </body>
    <script>
        function oAuth2(user) {
            var content = $("#"+user).val();
            var URL = 'https://adot.com.tw/message/push.php?';
            URL += 'groupId='+user;
            URL += '&content='+content;

            $.get( URL, function(result){
                alert(success);
            });
        }
    </script>
</html>
        
