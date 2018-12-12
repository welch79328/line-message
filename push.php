<?php

include( __DIR__ . "/config/setting.php");

$groupId = $_GET["groupId"];
$content = $_GET["content"];

$userIds = [];
$message = !empty($content) ? $content : 'Hello!';

include( __DIR__ . "/config/file.php");
 
if (count($db['user']) === 0) {
    echo 'No user.';
    exit(1);
} else {
    foreach ($db['user'] as $userInfo) {
        if ($userInfo['groupId'] == $groupId) {
            $userIds = $userInfo['groupId'];
        }
    }
}
 
// make payload
$payload = [
    'to' => $userIds,
    'messages' => [
        [
            'type' => 'text',
            'text' => $message
        ]
    ],
];

// Send Request by CURL
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.line.me/v2/bot/message/push');
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
