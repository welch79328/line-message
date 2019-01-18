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

    if ($event['message']['text'] == '捷運路線') {

        $payload = [
            'replyToken' => $event['replyToken'],
            'messages' => [
                [
                    "type"=> "image",
                    "originalContentUrl"=> "https://adot.com.tw/message/images/mrt.jpg",
                    "previewImageUrl"=>"https://adot.com.tw/message/images/mrt.jpg"
                ]
            ]
        ];
        $sedMessage = true;
    }


	if ($event['message']['text'] == '抽') {
		$beautyRand = array_rand($beautydb['beauty'],1);
		$payload = [
            'replyToken' => $event['replyToken'],
            'messages' => [
				[
          			"type"=> "image",
					"originalContentUrl"=> FILE_URL."file/".$beautydb['beauty'][$beautyRand],
					"previewImageUrl"=> FILE_URL."file/".$beautydb['beauty'][$beautyRand]
       			] 
			]
        ];	
		$sedMessage = true;
	}

	if ($event['message']['text'] == '抽帥哥') {
        $handsomeRand = array_rand($handsomedb['handsome'],1);
        $payload = [
            'replyToken' => $event['replyToken'],
            'messages' => [
                [
                    "type"=> "image",
                    "originalContentUrl"=> FILE_URL."handsomefile/".$handsomedb['handsome'][$handsomeRand],
                    "previewImageUrl"=> FILE_URL."handsomefile/".$handsomedb['handsome'][$handsomeRand]
                ]
            ]
        ];
        $sedMessage = true;
    }

	if ($event['message']['text'] == '抽狗狗') {
        $dogRand = array_rand($dogdb['dog'],1);
        $payload = [
            'replyToken' => $event['replyToken'],
            'messages' => [
                [
                    "type"=> "image",
                    "originalContentUrl"=> FILE_URL."dogfile/".$dogdb['dog'][$dogRand],
                    "previewImageUrl"=> FILE_URL."dogfile/".$dogdb['dog'][$dogRand]
                ]
            ]
        ];
        $sedMessage = true;
    }
	

	foreach ($citys as $city) {
		if ($event['message']['text'] == $city.' 天氣') {
			$weatherContent = '';
			foreach ($weatherdb['weather'][$city] as $v=>$k){
				$weathertitle = explode(" ",$v);
				$weathertitle2 = explode("~",$weathertitle[2]);
				$weatherContent .= $weathertitle[0].'                                     ';
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


    foreach ($constellation_name as $cname) {
        if ($event['message']['text'] == $cname) {
            $constellationContent = '';
            $constellationContent .= $constellationdb['constellation'][$cname]['title'].'                                     ';
            $constellationContent .= $constellationdb['constellation'][$cname]['content0'].'                                     ';
            $constellationContent .= $constellationdb['constellation'][$cname]['content1'].'                                     ';
	        $constellationContent .= $constellationdb['constellation'][$cname]['content2'].'                                     ';
	        $constellationContent .= $constellationdb['constellation'][$cname]['content3'].'                                     ';
	        $constellationContent .= $constellationdb['constellation'][$cname]['content4'].'                                     ';
	        $constellationContent .= $constellationdb['constellation'][$cname]['content5'].'                                     ';
	        $constellationContent .= $constellationdb['constellation'][$cname]['content6'].'                                     ';
	        $constellationContent .= $constellationdb['constellation'][$cname]['content7'].'                                     ';          

            $payload = [
                'replyToken' => $event['replyToken'],
                'messages' => [
                    [
                        'type' => 'text',
                        'text' => $constellationContent
                    ]
                ]
            ];
        	$sedMessage = true;
        }
    }

	if ($event['message']['text'] == '測試新聞') {
        $payload = [
            'replyToken' => $event['replyToken'],
            'messages' => [
                [
                    "type" => "template",
                    "altText" => "this is a carousel template",
                    "template" => [
                        "type" => "carousel",
                        "columns" => [
                            [
                                "thumbnailImageUrl" => "https://example.com/bot/images/item1.jpg",
                                "imageBackgroundColor" => "#FFFFFF",
                                "title" => "this is menu",
                                "text" => "description",
                                "defaultAction" => [
                                    "type" => "uri",
                                    "label" => "View detail",
                                    "uri" => "http://example.com/page/123"
                                ],
                                "actions" => [
                                    [
                                        "type" => "postback",
                                        "label" => "Buy",
                                        "data" => "action=buy&itemid=111"
                                    ],
                                    [
                                        "type" => "postback",
                                        "label" => "Add to cart",
                                        "data" => "action=add&itemid=111"
                                    ],
                                    [
                                        "type" => "uri",
                                        "label" => "View detail",
                                        "uri" => "http://example.com/page/111"
                                    ]
                                ]
                            ],
                            [
                                "thumbnailImageUrl" => "https://example.com/bot/images/item2.jpg",
                                "imageBackgroundColor" => "#000000",
                                "title" => "this is menu",
                                "text" => "description",
                                "defaultAction" => [
                                    "type" => "uri",
                                    "label" => "View detail",
                                    "uri" => "http://example.com/page/222"
                                ],
                                "actions" => [
                                    [
                                        "type" => "postback",
                                        "label" => "Buy",
                                        "data" => "action=buy&itemid=222"
                                    ],
                                    [
                                        "type" => "postback",
                                        "label" => "Add to cart",
                                        "data" => "action=add&itemid=222"
                                    ],
                                    [
                                        "type" => "uri",
                                        "label" => "View detail",
                                        "uri" => "http://example.com/page/222"
                                    ]
                                ]
                            ]
                        ],
                        "imageAspectRatio" => "rectangle",
                        "imageSize" => "cover"
                    ]
                ]
            ]
        ];
        $sedMessage = true;
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
