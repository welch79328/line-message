<?php


$dbFilePath = dirname(__FILE__) . '/spiderhandsome.json';  // user info database file path

echo $dbFilePath;
$db = json_decode(file_get_contents($dbFilePath), true);
echo count($db);

//$handsomeRand = array_rand($db['handsome'],1);
//echo "https://adot.com.tw/message/spider/handsomefile/".$db['handsome'][$handsomeRand];
//foreach ($aa as $userInfo) {
//	echo $userInfo;
//}

//include( __DIR__ . "/config/handsomefile.php");
//$handsomeRand = array_rand($handsomedb['handsome'],1);
//echo "https://adot.com.tw/message/spider/handsomefile/".$handsomedb['handsome'][$handsomeRand];

/*include( __DIR__ . "/config/beautyfile.php");
print_r($beautydb);exit;
$beautyRand = array_rand($beautydb['beauty'],1);
echo "https://adot.com.tw/message/spider/file/".$beautydb['beauty'][$beautyRand];
*/

include( __DIR__ . "/config/file.php");
/*$groupId = 'qqqqqqqqqqqqq';

if (!isset($db['user'][$groupId])) {

	$db['user'][$groupId] = [
        	'groupId' => $groupId,
        	'timestamp' => 'wwwwww'
        ];
        file_put_contents($dbFilePath, json_encode($db));
    }
*/

include( __DIR__ . "/config/weatherfile.php");

foreach ($citys as $city) {
     
                $weatherContent = '';
               	foreach ($weatherdb['weather'][$city] as $v=>$k){
			print_r($k['rain']);
                       /*$weatherContent .= $v;
                       $weatherContent .= $v['temperature'];
                       $weatherContent .= $v['situation'];
                       $weatherContent .= $v['comfortable'];
                       $weatherContent .= $v['rain'];*/
                  }
                
	                 
      echo $weatherContent;       
      
 }


?>
