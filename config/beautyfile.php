<?php

$dbFilePath = dirname(dirname(__FILE__)) . '/spiderbeauty.json';  // user info database file path


$beautydb = json_decode(file_get_contents($dbFilePath), true);

?>
