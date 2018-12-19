<?php

//user db
$dbFilePath = PROJECT_PATH . '/line-db.json';  // user info database file path
// open json database
if (!file_exists($dbFilePath)) {
    file_put_contents($dbFilePath, json_encode(['user' => []]));
}
$db = json_decode(file_get_contents($dbFilePath), true);

//beauty gril db
$beauty_dbFilePath = PROJECT_PATH . '/spiderbeauty.json';  // user info database file path
$beautydb = json_decode(file_get_contents($beauty_dbFilePath), true);

//handsome man db
$handsome_dbFilePath = PROJECT_PATH . '/spiderhandsome.json';  // user info database file path
$handsomedb = json_decode(file_get_contents($handsome_dbFilePath), true);

//weather db
$weather_dbFilePath = PROJECT_PATH . '/spiderweather.json';  // user info database file path
$weatherdb = json_decode(file_get_contents($weather_dbFilePath), true);
$citys = ['臺北市','新北市','桃園市','臺中市','臺南市','高雄市','基隆市','新竹市','新竹縣','苗栗縣','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','屏東縣','宜蘭縣','花蓮縣','臺東縣','澎湖縣'];

//dog db
$dog_dbFilePath = PROJECT_PATH . '/spiderdog.json';  // user info database file path
$dogdb = json_decode(file_get_contents($dog_dbFilePath), true);

//constellation db
$constellation_dbFilePath = PROJECT_PATH . '/spiderconstellation.json';  // user info database file path
$constellationdb = json_decode(file_get_contents($constellation_dbFilePath), true);
$constellation_name = ['牡羊座','金牛座','雙子座','巨蟹座','獅子座','處女座','天秤座','天蠍座','射手座','摩羯座','水瓶座','雙魚座'];

?>
