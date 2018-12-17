<?php

$dbFilePath = dirname(dirname(__FILE__)) . '/spiderweather.json';  // user info database file path


$weatherdb = json_decode(file_get_contents($dbFilePath), true);


$citys = ['臺北市','新北市','桃園市','臺中市','臺南市','高雄市','基隆市','新竹市','新竹縣','苗栗縣','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','屏東縣','宜蘭縣','花蓮縣','臺東縣','澎湖縣'];


?>

