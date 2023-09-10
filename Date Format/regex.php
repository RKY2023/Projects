<?php
$my_url = "www.guru99.com";
$filename ="formatlist.txt";
$fp = @fopen($filename, 'r'); 

$array = array();
$formats = array();
$array = explode("\n", fread($fp, filesize($filename)));
$cnt=count($array);






// 	# Pattern Section
// Start - End Date

// Start Date
$patt[0] = "/(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}/";

// // For Browser:
// $append=array();
// $append = "<html><body><table>";
// for($idx=0; $idx < $cnt; $idx++ )
// {
// 	$append .= "<tr><td>".$array[$idx]."</td><td>";
// 	foreach ($patt as $key => $value) 
// 	{
// 		if (preg_match($patt, $array[$idx]))
// 		{
// 			$append .= "1 ";break;
// 		}
// 		else
// 		{
// 			$append .= "";
// 		}
// 	}
// 	$append .= "</td></tr>";
// }
// $append .= "</table></body></html>";
// echo $append;
// // For Browser ends

// For Terminal:
for($idx=0; $idx < $cnt; $idx++ )
{
	echo $array[$idx]."\t\t\t\t";
	foreach ($patt as $key => $value) 
	{
		if (preg_match($value, $array[$idx]))
		{
			echo "1";break;
		}
		else
		{
			echo "";
		}
	}
	echo "\n";
}	
// echo($cnt);
// For Terminal ends
?>
