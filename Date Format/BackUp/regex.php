<?php
$my_url = "www.guru99.com";
$filename ="formatlist.txt";
$fp = @fopen($filename, 'r'); 
$array = array();
$formats = array();
$array = explode("\n", fread($fp, filesize($filename)));
$cnt=count($array);
for($idx=0; $idx < $cnt; $idx++ )
{
	if (preg_match("/(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}/", $array[$idx]))
		{
			echo $array[$idx];
		}
		else
		{
			echo "NO";
		}
		echo "\n";
}
		
?>
