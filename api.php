<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

if (!isset($_GET['url'])) {
    echo json_encode(["success" => false, "message" => "URL is required"]);
    exit;
}

$url = $_GET['url'];
$apiUrl = "https://www.tikwm.com/api/?url=" . urlencode($url);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);

if (isset($data['code']) && $data['code'] == 0) {
    $vid = $data['data'];
    $author = $vid['author'];
    
    // চেক করা হচ্ছে এটা কি ইমেজ পোস্ট কিনা
    $is_image = isset($vid['images']) && is_array($vid['images']);
    
    echo json_encode([
        "success" => true,
        "is_image" => $is_image,
        "title" => isset($vid['title']) ? $vid['title'] : "TikTok Media",
        "video_url" => isset($vid['play']) ? $vid['play'] : null,
        "images" => $is_image ? $vid['images'] : [], // সব ছবির লিঙ্ক
        "cover" => $vid['cover'],
        "author_name" => $author['nickname'],
        "author_username" => $author['unique_id'],
        "author_avatar" => $author['avatar'],
        "views" => $vid['play_count'] ?? 0,
        "likes" => $vid['digg_count'] ?? 0,
        "comments" => $vid['comment_count'] ?? 0,
        "shares" => $vid['share_count'] ?? 0
    ]);
} else {
    echo json_encode(["success" => false, "message" => "Invalid TikTok URL or Video not found!"]);
}
?>
// minor update at 2026-05-16 16:23:22 - iteration 2

// minor update at 2026-05-16 16:23:39 - iteration 4
