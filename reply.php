<?php
 
include( __DIR__ . "/config/setting.php"); 
 
include( __DIR__ . "/config/file.php"); 

$bodyMsg = file_get_contents('php://input');
 
$obj = json_decode($bodyMsg, true);

$sedMessage = false;
 
foreach ($obj['events'] as $event) {
 
	$groupId = $event['source']['groupId']; 

	if (!isset($db['user'][$groupId])) {
       
        	$db['user'][$groupId] = [
			'groupId' => $groupId,
            		'timestamp' => $event['timestamp']
        	];
        	file_put_contents($dbFilePath, json_encode($db));
	}

	if ($event['message']['text'] == '###@@@') {

		$payload = [
       			'replyToken' => $event['replyToken'],
       			'messages' => [
           			[
               				'type' => 'text',
               				'text' => 'www'
           			]
      			 ]
   		];
        	$sedMessage = true;
	}

	if ($event['message']['stickerId'] == 13) {

                $payload = [
                        'replyToken' => $event['replyToken'],
                        'messages' => [
                                [
                                        "type"=> "image",
                                        "originalContentUrl"=> "https://adot.com.tw/message/images/13.jpg",
                                        "previewImageUrl"=>"https://adot.com.tw/message/images/13.jpg"
                                ]
                        ]
                ];
                $sedMessage = true;
        }


	if ($event['message']['text'] == '抽') {
		include( __DIR__ . "/config/beautyfile.php");
		$beautyRand = array_rand($beautydb['beauty'],1);
		$payload = [
                        'replyToken' => $event['replyToken'],
                        'messages' => [
				[
                  			"type"=> "image",
					"originalContentUrl"=> "https://adot.com.tw/message/spider/file/".$beautydb['beauty'][$beautyRand],
					"previewImageUrl"=>"https://adot.com.tw/message/spider/file/".$beautydb['beauty'][$beautyRand]
               			] 
			]
                ];	
		$sedMessage = true;
	}

	if ($event['message']['text'] == '抽帥哥') {
                include( __DIR__ . "/config/handsomefile.php");
                $handsomeRand = array_rand($handsomedb['handsome'],1);
                $payload = [
                        'replyToken' => $event['replyToken'],
                        'messages' => [
                                [
                                        "type"=> "image",
                                        "originalContentUrl"=> "https://adot.com.tw/message/spider/handsomefile/".$handsomedb['handsome'][$handsomeRand],
                                        "previewImageUrl"=>"https://adot.com.tw/message/spider/handsomefile/".$handsomedb['handsome'][$handsomeRand]
                                ]
                        ]
                ];
                $sedMessage = true;
        }

	include( __DIR__ . "/config/weatherfile.php");

	foreach ($citys as $city) {
		if ($event['message']['text'] == $city.' 天氣') {
			$weatherContent = '';
			foreach ($weatherdb['weather'][$city] as $v=>$k){
				$weathertitle = explode(" ",$v);
				$weathertitle2 = explode("~",$weathertitle[2]);
				$weatherContent .= $weathertitle[0].'                                     ';
				//$weatherContent .= '時間:                                                             ';
				$weatherContent .= $weathertitle[1].' '.$weathertitle2[0].'~'.$weathertitle2[1].' '.$weathertitle[3].'                             '; 
				$weatherContent .= '溫度: '.$k['temperature'].'                                     ';
				$weatherContent .= '天氣狀況: '.$k['situation'].'                       ';
				$weatherContent .= '舒適度: '.$k['comfortable'].'                          ';
				$weatherContent .= '降雨機率: '.$k['rain'].'                             ';
				$weatherContent .= '---------------------------            ';
			}
				
			$payload = [
				'replyToken' => $event['replyToken'],
				'messages' => [
					[
						'type' => 'text',
						'text' => $weatherContent
					]
				]

			];
		$sedMessage = true;
		}
	}	



	if ($sedMessage) {
		// Make payload
		
	 	
		// Send reply API
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, 'https://api.line.me/v2/bot/message/reply');
		curl_setopt($ch, CURLOPT_POST, true);
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
		curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
		curl_setopt($ch, CURLOPT_HTTPHEADER, [
			'Content-Type: application/json',
			'Authorization: Bearer ' . CHANNEL_ACCESS_TOKEN
		]);
		$result = curl_exec($ch);
		curl_close($ch);
	}
 
}
?>
