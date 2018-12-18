<?php

$dbFilePath = dirname(dirname(__FILE__)) . '/spiderconstellation.json';  // user info database file path


$constellationdb = json_decode(file_get_contents($dbFilePath), true);

$constellation_name = ['牡羊座','金牛座','雙子座','巨蟹座','獅子座','處女座','天秤座','天蠍座','射手座','摩羯座','水瓶座','雙魚座'];

?>

