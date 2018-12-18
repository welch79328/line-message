<?php

$dbFilePath = __DIR__ . '/line-db.json';  // user info database file path

// open json database
if (!file_exists($dbFilePath)) {
    file_put_contents($dbFilePath, json_encode(['user' => []]));
}
$db = json_decode(file_get_contents($dbFilePath), true);

?>
