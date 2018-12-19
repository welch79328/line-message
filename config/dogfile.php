<?php

$dbFilePath = dirname(dirname(__FILE__)) . '/spiderdog.json';  // user info database file path


$dogdb = json_decode(file_get_contents($dbFilePath), true);



?>

