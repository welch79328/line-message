<?php

$dbFilePath = dirname(dirname(__FILE__)) . '/spiderhandsome.json';  // user info database file path


$handsomedb = json_decode(file_get_contents($dbFilePath), true);

?>
