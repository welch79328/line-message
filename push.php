<?php

$groupId = $_GET["groupId"];
$content = $_GET["content"];
 
$channelAccessToken = 'FLPX90FqeLauLpLsrMY/hVE/B6RYCRKk6zjXDPIFa/NgMOMLLOAzf/3DcFFHLi9muxpK7qKgnUCb7XnSeaqOHGAdvPp1I+2ZxpmJnZosQ2AOXU4zWqQAkNORUgQnHOZX7DL8RjBvM+lgrbLOs+NLlwdB04t89/1O/w1cDnyilFU=';
$userIds = [];
$message = !empty($content) ? $content : 'Hello!';

include("file.php");
 
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
    'Authorization: Bearer ' . $channelAccessToken
]);
$result = curl_exec($ch);
echo $result;
curl_close($ch);
