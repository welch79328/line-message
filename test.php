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
               	foreach ($weatherdb['weather'][$city] as $v=>$k) {
                       $weatherContent .= $v;
                       $weatherContent .= $k['temperature'];
                       $weatherContent .= $k['situation'];
                       $weatherContent .= $k['comfortable'];
                       $weatherContent .= $k['rain'];
                  }
                
	                 
      echo $weatherContent;       
      
 }


/*
  include( __DIR__ . "/config/constellationfile.php");

        foreach ($constellation_name as $cname) {
			echo $cname;               
                        $constellationContent = '';
                        //foreach ($constellationdb['constellation'][$cname] as $v=>$k){
				$constellationContent .= $constellationdb['constellation'][$cname]['title'].'                                     ';
                                $constellationContent .= $constellationdb['constellation'][$cname]['content0'].'                                     ';
                                $constellationContent .= $constellationdb['constellation'][$cname]['content1'].'                                     ';
                                $constellationContent .= $constellationdb['constellation'][$cname]['content2'].'                                     ';
                                $constellationContent .= $constellationdb['constellation'][$cname]['content3'].'                                     ';
                                $constellationContent .= $constellationdb['constellation'][$cname]['content4'].'                                     ';
                                $constellationContent .= $constellationdb['constellation'][$cname]['content5'].'                                     ';
                                $constellationContent .= $constellationdb['constellation'][$cname]['content6'].'                                     ';
                                $constellationContent .= $constellationdb['constellation'][$cname]['content7'].'                                     ';
							
				//print_r($v);
			//}
	echo $constellationContent;
	}
*/

?>
