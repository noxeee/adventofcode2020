<?php

// F front
// B back
// L left
// R right

function parse_row($bcode) {
    
    $rcodes = substr($bcode, 0, 7);

    var_dump($rcodes);

    $range = array(0,127);

    foreach (str_split($rcodes) as $char) {
        if($char == 'F') {
            $range[1] = floor(($range[0]+$range[1])/2);
        } else {
            $range[0] = ceil(($range[0]+$range[1])/2);
        }
    }
    return $range[0];
}

var_dump(parse_row("FBFBBFFRLR"));

function parse_column($bcode) {
    
    $ccodes = substr($bcode, 7);

    var_dump($ccodes);

    $range = array(0,7);

    foreach (str_split($ccodes) as $char) {
        if($char == 'L') {
            $range[1] = floor(($range[0]+$range[1])/2);
        } else {
            $range[0] = ceil(($range[0]+$range[1])/2);
        }
    }
    return $range[0];
}

var_dump(parse_column("FBFBBFFRLR"));

$myfile = fopen("input.txt", "r") or die("Unable to open file!");
$lines = fread($myfile, filesize("input.txt"));
fclose($myfile);

$bcodes = explode("\n", $lines);

//var_dump($bcodes);

$seat_ids = array();

foreach ($bcodes as $bcode) {
    $row = parse_row($bcode);
    $column = parse_column($bcode);

    $seat_id = $row*8 + $column;
    array_push($seat_ids, $seat_id);
}

echo max($seat_ids);