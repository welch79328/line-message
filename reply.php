<?php
 
include( __DIR__ . "/config/setting.php"); 
 
include( __DIR__ . "/config/file.php"); 

$bodyMsg = file_get_contents('php://input');
 
$obj = json_decode($bodyMsg, true);

$sedMessage = false;
 
foreach ($obj['events'] as $event) {
 
	$groupId = $event['source']['groupId']; 

	if (!isset($db['user'][$userId])) {
       
        $db['user'][$groupId] = [
			'groupId' => $groupId,
            'timestamp' => $event['timestamp']
        ];
        file_put_contents($dbFilePath, json_encode($db));
	}

	if ($event['message']['text'] == '###@@@') {

		$message = [
               'type' => 'text',
               'text' => '內容'
        ];
        $sedMessage = true;
	}


	if ($event['message']['text'] == KEYWORD_BEAUTY) {
		
		$message = [
		  "type"=> "image",
		  "originalContentUrl"=> "圖片網址",
		  "previewImageUrl"=> "縮圖網址"
		];
		$sedMessage = true;
	}



	if ($sedMessage) {
		// Make payload
		$payload = [
			'replyToken' => $event['replyToken'],
			'messages' => $message
		];
	 	
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
