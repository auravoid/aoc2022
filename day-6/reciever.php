<?php
$input = str_replace("\r", '', file_get_contents('input.txt'));
$p1 = '';
$p2 = '';

function getStartPkg($data)
{
    for ($i = 0; $i < sizeof($data); $i++) {
        $s = array_slice($data, $i, 4);
        $u = array_unique($s);
        if (sizeof($u) == 4) {
            $p1 = $i + 4;
            break;
        }
    }
    echo "Pkg starts at: $p1\n";
}

function getStartMsg($data)
{
    for ($i = 0; $i < sizeof($data); $i++) {
        $s = array_slice($data, $i, 14);
        $u = array_unique($s);
        if (sizeof($u) == 14) {
            $p2 = $i + 14;
            break;
        }
    }
    echo "Msg starts at: $p2\n";
}

getStartPkg(str_split($input));
getStartMsg(str_split($input));
