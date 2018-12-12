<?php
 
$channelAccessToken = 'FLPX90FqeLauLpLsrMY/hVE/B6RYCRKk6zjXDPIFa/NgMOMLLOAzf/3DcFFHLi9muxpK7qKgnUCb7XnSeaqOHGAdvPp1I+2ZxpmJnZosQ2AOXU4zWqQAkNORUgQnHOZX7DL8RjBvM+lgrbLOs+NLlwdB04t89/1O/w1cDnyilFU=';
 
include("file.php"); 

$bodyMsg = file_get_contents('php://input');
 
$obj = json_decode($bodyMsg, true);
 
foreach ($obj['events'] as $event) {
 
	//$userId = $event['source']['userId'];
	$groupId = $event['source']['groupId']; 
	// bot dirty logic
	/*if (!isset($db['user'][$userId])) {

		$message = 'Please link from the background.';

	} else {
		if($db['user'][$userId]['ststus'] == 'login'){
			*/$db['user'][$groupId] = [
				'groupId' => $groupId,
               			'timestamp' => $event['timestamp']
           		];
			file_put_contents($dbFilePath, json_encode($db));/*
			$message = 'Wellcome! '.$db['user'][$userId]['userName'].'You can enter the "tool" check features';
		} elseif (strtolower($event['message']['text']) === 'tool') {	
			$message = 'Construction';
		}else{
			$message = 'You can enter the "tool" check features';
		}
		
	}
 
	// Make payload
	$payload = [
		'replyToken' => $event['replyToken'],
		'messages' => [
			[
				'type' => 'text',
				'text' => $message
			]
		]
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
		'Authorization: Bearer ' . $channelAccessToken
	]);
	$result = curl_exec($ch);
	curl_close($ch);*/
}
