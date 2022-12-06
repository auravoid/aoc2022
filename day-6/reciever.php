<?php
$input = str_replace("\r", '', file_get_contents('input.txt'));
$p1 = '';

$data = str_split($input);

for ($i = 0; $i < sizeof($data); $i++) {
    $s = array_slice($data, $i, 4);
    $u = array_unique($s);
    if (sizeof($u) == 4) {
        $p1 = $i + 4;
        break;
    }
}

echo "Starts at: $p1\n";
