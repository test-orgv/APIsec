<?php

header('Content-Type: application/json; charset=utf-8');
header('Server: Fulcrum-API Beta');

// Disable external entity loading (safe setting)
libxml_disable_entity_loader(true);

// Load XML securely (no dangerous flags)
$xmlfile = file_get_contents('php://input');
$dom = new DOMDocument();

// Don't use LIBXML_NOENT or LIBXML_DTDLOAD
if (@$dom->loadXML($xmlfile, LIBXML_NONET)) {
    $input = simplexml_import_dom($dom);
    $output = $input->Ping;

    // check if ok
    if ($output == "Ping") {
        // no response
    } else {
        $data = array('Heartbeat' => array('Ping' => "Pong"));
        echo json_encode($data);
    }
} else {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid XML']);
}

?>
