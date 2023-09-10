<?php
$output=array();
$start_date = '2019-02-05';
$end_date = '2019-02-07';
//Dates in number
$st_dt = substr($start_date, 8,2);
$en_dt = substr($end_date, 8,2);
$st_mn = substr($start_date, 5,2);
$en_mn = substr($end_date, 5,2);
$st_yr = date('Y', strtotime($start_date));
$en_yr = date('Y', strtotime($end_date));
//month in fullname
$st_mn_s = date('F', strtotime($start_date));
$en_mn_s = date('F', strtotime($end_date));
//month in shortname
$st_mn_f = date('M', strtotime($start_date));
$en_mn_f = date('M', strtotime($end_date));
//Day in fullname
$st_day_s = date('l', strtotime($start_date));
$en_day_s = date('l', strtotime($end_date));
//Day in shortname
$st_day_f = date('D', strtotime($start_date));
$en_day_f = date('D', strtotime($end_date));
//Ordinary date format
$st_OrdDt = date('S', strtotime($start_date));
$en_OrdDt = date('S', strtotime($end_date));
$format1 = $st_day_f.",".$st_mn_f." ".$st_dt.", ".$st_yr;array_push($output,$format1);
$format2 = $st_mn_f." ".$st_dt.", ".$st_yr;array_push($output,$format2);
$format3 = $st_dt." ".$st_mn_s." - ".$en_dt." ".$st_mn_s." ".$st_yr;array_push($output,$format3);
$format4 = $st_mn_s.".".$st_dt." - ".$en_dt." ".$st_mn_s." ".$st_yr;array_push($output,$format4);
$format5 = $st_mn_s." ".$st_dt.", ".$st_yr." - ".$en_mn_s." ".$en_dt.", ".$en_yr;array_push($output,$format5);
$format6 = $st_mn_f." ".$st_dt."-".$en_dt.", ".$en_yr;array_push($output,$format6);
$format7 = $st_mn_f." ".$st_dt." - ".$en_dt.", ".$en_yr;array_push($output,$format7);
$format8 = $st_dt."-".$en_dt." ".$en_mn_f."'".substr($en_yr,2,2);array_push($output,$format8);
$format9 = $st_mn_f." ".$st_OrdDt." & ".$en_OrdDt;array_push($output,$format9);
$format10 = $st_dt." - ".$en_dt." ".$en_mn_f." ".$en_yr;array_push($output,$format10);
$format11 = $st_dt.".".$st_mn.".".$st_yr."-".$en_dt.".".$en_mn.".".$en_yr;array_push($output,$format11);
$format12 = $st_mn_f." ".$st_dt."-".$en_dt.", ".$en_yr;array_push($output,$format12);
$format13 = $st_day_s." ".$st_mn_s." ".$st_OrdDt." - ".$en_day_s." ".$en_mn_s." ".$en_OrdDt;array_push($output,$format13);
$format14 = $st_day_f.", ".$st_mn_f." ".$st_OrdDt.", ".$en_yr;array_push($output,$format14);
$format15 = $st_day_s." ".$st_mn_s." ".$st_OrdDt." - ".$en_day_s." ".$en_mn_s." ".$en_OrdDt;array_push($output,$format14);
$format14 = $st_day_s." ".$st_mn_s." ".$st_OrdDt." - ".$en_day_s." ".$en_mn_s." ".$en_OrdDt;array_push($output,$format14);
$format14 = $st_day_s." ".$st_mn_s." ".$st_OrdDt." - ".$en_day_s." ".$en_mn_s." ".$en_OrdDt;array_push($output,$format14);
$format14 = $st_day_s." ".$st_mn_s." ".$st_OrdDt." - ".$en_day_s." ".$en_mn_s." ".$en_OrdDt;array_push($output,$format14);
$format14 = $st_day_s." ".$st_mn_s." ".$st_OrdDt." - ".$en_day_s." ".$en_mn_s." ".$en_OrdDt;array_push($output,$format14);
$format14 = $st_day_s." ".$st_mn_s." ".$st_OrdDt." - ".$en_day_s." ".$en_mn_s." ".$en_OrdDt;array_push($output,$format14);
print_r($output);
?>