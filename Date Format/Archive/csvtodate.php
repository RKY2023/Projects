<?php
require_once('/home/indiamart/public_html/serve-biztradeshows-com/db.php');
include_once '/home/indiamart/public_html/serve-biztradeshows-com/cron_status_update.php';
include '/home/indiamart/public_html/serve-biztradeshows-com/domaindetect.php';

$today = date("d-M-y");
$csv_data = "";
$header1 ="";
$timeout = 30;
$csv_data="Event ID"."\t"."Event Name"."\t"."Website"."\t"."Start-End Date"."\n";
$upcomEvt = "SELECT e.id,e.name,e.website,e.start_date,e.end_date from post_review pr,event e where pr.entity_id=e.id and  date(qc_on)=curdate() - INTERVAL 1 DAY and entity_type='event' and review_type in('N','M') and modify_type NOT in('E') and e.published=1 limit 10000";

$sql_T_event=mysqli_query($con,$upcomEvt);
while ($data= mysqli_fetch_assoc($sql_T_event))
{
    $header1 = array('Accept: */*');
    $url=$data['website'];
    $curl = curl_init($url);
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_HEADER, true);
    curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true); 
    curl_setopt($curl, CURLOPT_USERAGENT,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36');
    curl_setopt($curl, CURLOPT_HTTPHEADER, $header1);
    curl_setopt($curl, CURLOPT_VERBOSE,  true   );  // new
    curl_setopt($curl, CURLOPT_COOKIEJAR,  '/tmp/cookiejar'   );  // new
    curl_setopt($curl, CURLOPT_COOKIEFILE,  '/tmp/cookiejar'   );  // new
    curl_setopt($curl, CURLOPT_ENCODING, 'gzip');   
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($curl, CURLOPT_SSLVERSION,6);
    if($header1=='header_required')
    {
     curl_setopt($curl, CURLOPT_HEADER, 1);
    }
    if(!empty($timeout))
        curl_setopt($curl,CURLOPT_TIMEOUT,$timeout);
    $Wval = curl_exec($curl);
    $start_date = $data['start_date'];
      $end_date = $data['end_date'];

      $output=array();
      //Dates in number
      $st_dt = date('j', strtotime($start_date));
      $en_dt = date('j', strtotime($end_date));
      //Dates in number with leading Zeroes
      $st_dt0 = date('d', strtotime($start_date));
      $en_dt0 = date('d', strtotime($end_date));
      //Ordinary date (st,nd,th)
      $st_OrdDt = $st_dt.date('S', strtotime($start_date));
      $en_OrdDt = $en_dt.date('S', strtotime($end_date));

      //month in without leading Zeroes
      $st_mn = date('n', strtotime($start_date));
      $en_mn = date('n', strtotime($end_date));
      //month in with leading Zeroes
      $st_mn0 = date('m', strtotime($start_date));
      $en_mn0 = date('m', strtotime($end_date));
      //month in fullname
      $st_mn_s = date('M', strtotime($start_date));
      $en_mn_s = date('M', strtotime($end_date));
      //month in shortname
      $st_mn_f = date('F', strtotime($start_date));
      $en_mn_f = date('F', strtotime($end_date));

      //Day in shortname
      $st_day_s = date('D', strtotime($start_date));
      $en_day_s = date('D', strtotime($end_date));
      //Day in fullname
      $st_day_f = date('l', strtotime($start_date));
      $en_day_f = date('l', strtotime($end_date));

      //Year in XXXX
      $st_yr = date('Y', strtotime($start_date));
      $en_yr = date('Y', strtotime($end_date));
      //Year in XX
      $st_yr2 = date('y', strtotime($start_date));
      $en_yr2 = date('y', strtotime($end_date));

      if($st_mn==$en_mn)
      $st_en_date = $st_dt." - ".$en_dt." ".$en_mn_s." ".$en_yr;
      else $st_en_date = $st_dt." ".$st_mn_s." - ".$en_dt." ".$en_mn_s." ".$en_yr;

        $format[0] = $st_day_f.", ".$st_mn_f." ".$st_dt.", ".$st_yr;
      $format[1] = $st_mn_f." ".$st_dt.", ".$st_yr;
      $format[2] = $st_dt." ".$st_mn_s." - ".$en_dt." ".$en_mn_s." ".$en_yr;
      if($st_mn==$en_mn)
      $format[3] = $st_mn_s.". ".$st_dt." - ".$en_dt.", ".$en_yr;
      $format[4] = $st_mn_s." ".$st_dt.", ".$st_yr." - ".$en_mn_s." ".$en_dt.", ".$en_yr;
      if($st_mn==$en_mn)
      $format[5] = $st_mn_f." ".$st_dt."-".$en_dt.", ".$en_yr;
      if($st_mn==$en_mn)
      $format[6] = $st_mn_f." ".$st_dt." - ".$en_dt.", ".$en_yr;
      if($st_mn==$en_mn)
      $format[7] = $st_dt."-".$en_dt." ".$en_mn_f."'".$en_yr2;
      $tmp="";
      if($en_dt-$st_dt >= 1 && $st_mn==$en_mn)
      {           
            for ($i=1; $i <($en_dt-$st_dt) ; $i++) { 
                  # code...
                  // echo $en_dt-$st_dt;
                  $dt = strtotime('+'.$i.' day',strtotime($start_date));
                  $tmp .= ', '.date('j', $dt).date('S', $dt);
            }
            $format[8] = $st_mn_f." ".$st_OrdDt.$tmp." & ".$en_OrdDt;
      }
      if($st_mn==$en_mn)
      $format[9] = $st_dt." – ".$en_dt." ".$en_mn_f." ".$en_yr;
      $format[10] = $st_dt0.".".$st_mn0.".".$st_yr."-".$en_dt0.".".$en_mn0.".".$en_yr;
      if($st_mn==$en_mn)
      $format[11] = $st_mn_f." ".$st_dt."-".$en_dt.", ".$en_yr;
      $format[12]= $st_day_s." ".$st_mn_s." ".$st_OrdDt." - ".$en_day_s." ".$en_mn_s." ".$en_OrdDt;
      $format[13] = $st_day_f.", ".$st_mn_f." ".$st_OrdDt.", ".$en_yr;
      $format[14] = $st_day_f.", ".$st_mn_f." ".$st_dt.", ".$en_yr;
      $tmp="";
      if($en_dt-$st_dt >= 1 && $st_mn==$en_mn)
      {           
            for ($i=1; $i <($en_dt-$st_dt) ; $i++) { 
                  # code...
                  // echo $en_dt-$st_dt;
                  $dt = strtotime('+'.$i.' day',strtotime($start_date));
                  $tmp .= ', '.date('j', $dt).date('S', $dt);
            }
            $format[15] = $st_mn_f." ".$st_OrdDt.$tmp." & ".$en_OrdDt.", ".$en_yr;
      }
      
      $format[16] = $st_mn_f." ".$st_dt.", ".$st_yr." - ".$en_mn_f." ".$en_dt.", ".$en_yr;
      $format[17] = $st_mn_s." ".$st_dt0.", ".$st_yr." To ".$en_mn_s." ".$en_dt0.", ".$en_yr;
      $format[18] = $st_day_f." ".$st_mn_f." ".$st_dt.", ".$st_yr;
      if($st_mn==$en_mn)
            $format[19] = $st_dt." - ".$en_dt." ".$en_mn_f." ".$en_yr;  
      $format[20] = $st_dt." ".$st_mn_s." - ".$en_dt." ".$en_mn_f." ".$en_yr;
      $format[21] = $st_dt0." ".$st_mn_s." - ".$en_dt0." ".$en_mn_s." ".$en_yr;
      $tmp="";
      if($en_dt-$st_dt >= 1 && $st_mn==$en_mn)
      {           
            for ($i=1; $i <($en_dt-$st_dt) ; $i++) { 
                  # code...
                  // echo $en_dt-$st_dt;
                  $dt = strtotime('+'.$i.' day',strtotime($start_date));
                  $tmp .= ', '.date('j', $dt);
            }
            $format[22] = $st_mn_f." ".$st_dt.$tmp." & ".$en_dt.", ".$en_yr;
      }
      $format[23] = $st_mn_f." ".$st_dt."-".$en_mn_s.". ".$en_dt.", ".$en_yr;
      if($st_mn==$en_mn)
            $format[24] = $st_dt." - ".$en_dt." ".$en_mn_f." ".$en_yr;
      $format[25] = $st_day_f.", ".$st_mn_f." ".$st_dt.", ".$st_yr." – ".$en_day_f.", ".$en_mn_f." ".$en_dt.", ".$en_yr;
      $tmp="";
      if($en_dt-$st_dt >= 1 && $st_mn==$en_mn)
      {           
            for ($i=1; $i <($en_dt-$st_dt) ; $i++) { 
                  # code...
                  $dt = strtotime('+'.$i.' day',strtotime($start_date));
                  $tmp .= ', '.date('j', $dt);
            }
            $format[26] = $st_mn_f." ".$st_dt.$tmp." and ".$en_dt.", ".$en_yr;
      }
      if($st_mn==$en_mn)
            $format[27] = $st_mn_f." ".$st_OrdDt."-".$en_OrdDt.", ".$en_yr;
      if($st_mn==$en_mn)
            $format[28] = $st_dt."-".$en_dt." ".$en_mn_f." ".$en_yr;
      if($st_mn<10)
            $format[29] = $st_yr.". ".$st_mn.".".$st_dt." ".$st_day_s." ".$en_mn.".".$en_dt." ".$en_day_s;
      $format[30] = $st_day_f." ".$st_dt."/".$st_mn0."/".$st_yr;
      if($en_dt-$st_dt<2)
      $format[31] = $st_day_f.", ".$st_mn_f." ".$st_dt." and ".$en_day_f.", ".$en_mn_f." ".$en_dt.", ".$en_yr;
      $format[32] = $st_day_f.", ".$st_mn_f." ".$st_dt.", ".$st_yr." to ".$en_day_f.", ".$en_mn_f." ".$en_dt.", ".$en_yr;
      if($en_dt-$st_dt<2 && $st_mn==$en_mn)
      $format[33] = $st_day_f." ".$st_OrdDt." and ".$en_day_f." ".$en_OrdDt." ".$en_mn_f." ".$en_yr;
        if($st_mn==$en_mn)
      $format[34] = $st_yr.": ".$st_mn_f." ".$st_dt."-".$en_dt;
      if($st_mn==$en_mn)
            $format[35] = $st_dt.". - ".$en_dt.". ".$en_mn_f." ".$en_yr;
      $format[36] = $st_day_f.", ".$st_mn_f." ".$st_dt.", ".$st_yr;
      $format[37] = $st_dt." ".$st_mn_s." – ".$en_dt." ".$en_mn_s." ".$en_yr;
      if($st_mn==$en_mn)
            $format[38] = $st_dt0.". – ".$en_dt0.". ".$en_mn_f." ".$en_yr;
      $format[39] = $st_mn_f.".".$st_dt.", ".$st_yr." - ".$en_mn_f.".".$en_dt.", ".$en_yr;
      $format[40] = $st_OrdDt." of ".$st_mn_f." to ".$en_OrdDt." of ".$en_mn_f." ".$en_yr;
      $format[41] = $st_dt0."/".$st_mn0."/".$st_yr." - ".$en_dt0."/".$en_mn0."/".$en_yr;
      if($st_mn==$en_mn)
      $format[42] = $st_mn_f." ".$st_dt." – ".$en_dt.", ".$en_yr;
      if($st_mn==$en_mn)
            $format[43] = $st_OrdDt." to ".$en_OrdDt." of ".$en_mn_f." ".$en_yr;
      if($st_mn==$en_mn)
            $format[44] = $st_OrdDt."-".$en_OrdDt.".".$en_mn_f.". ".$en_yr;
      if($st_mn==$en_mn && $st_mn<10)
            $format[45] = $st_yr.". ".$st_mn.".".$st_dt." - ".$en_dt;
      if($st_mn==$en_mn)
      $format[46] = $st_mn_s.". ".$st_OrdDt."-".$en_OrdDt.", ".$en_yr;
      $format[47] = $st_dt0."/".$st_mn0."/".$st_yr;
      $format[48] = $st_dt." ".$st_mn_f." ".$st_yr." - ".$en_dt." ".$en_mn_f." ".$en_yr;
      if($st_mn==$en_mn)
            $format[49] = $st_mn_f." ".$st_dt." to ".$en_dt.", ".$en_yr;
      if($st_mn==$en_mn)
            $format[50] = $st_mn_f." ".$st_OrdDt." to ".$en_mn_f." ".$en_OrdDt." ".$en_yr;
      if($st_mn==$en_mn)
            $format[51] = $st_dt." ".$st_mn_f." to ".$en_dt." ".$en_mn_f.", ".$en_yr;
      if($st_mn==$en_mn)
            $format[52] = $st_mn_f." ".$st_dt0."-".$en_dt0.", ".$en_yr;
      if($st_mn==$en_mn)
            $format[53] = $st_OrdDt."-".$en_OrdDt." ".$en_mn_f." ".$en_yr;
      if($st_mn==$en_mn)
            $format[54] = $st_day_f.", ".$st_mn_f." ".$st_dt." – ".$en_day_f.",".$en_mn_f." ".$en_dt.", ".$en_yr;
      $format[55] = "Start: ".$st_mn_f." ".$st_dt0." ".$st_yr;
      $format[56] = "End: ".$en_mn_f." ".$en_dt0." ".$en_yr;
      if($st_mn==$en_mn)
            $format[57] = $st_dt.". - ".$en_dt.". ".$en_mn_f." ".$en_yr;
      if($st_mn==$en_mn)
            $format[58] = $st_yr.".".$st_mn0.".".$st_dt0."-".$en_dt0;
      $format[59] = $st_yr.".".$st_mn.".".$st_dt." ".$st_day_s." ".$en_mn.".".$en_dt." ".$en_day_s;
      if($st_mn==$en_mn)
            $format[60] = $st_yr.".".$st_mn.".".$st_dt." - ".$en_dt;
      if($st_mn==$en_mn)
            $format[61] = $st_mn_s." ".$st_OrdDt."-".$en_OrdDt.", ".$en_yr;

//Without Year
      $format[62] = $st_day_f.", ".$st_mn_f." ".$st_dt;
      $format[63] = $st_mn_f." ".$st_dt;
      if($st_mn==$en_mn)
      $format[64] = $st_dt." ".$st_mn_s." - ".$en_dt." ".$st_mn_s;
      if($st_mn==$en_mn)
      $format[65] = $st_mn_s.". ".$st_dt." - ".$en_dt;
      $format[66] = $st_mn_s." ".$st_dt." - ".$en_mn_s." ".$en_dt;
      if($st_mn==$en_mn)
      $format[67] = $st_mn_f." ".$st_dt."-".$en_dt;
      if($st_mn==$en_mn)
      $format[68] = $st_mn_f." ".$st_dt." - ".$en_dt;
      if($st_mn==$en_mn)
      $format[69] = $st_dt."-".$en_dt." ".$en_mn_f;
      $tmp="";
      if($en_dt-$st_dt >= 1 && $st_mn==$en_mn)
      {           
            for ($i=1; $i <($en_dt-$st_dt) ; $i++) { 
                  # code...
                  // echo $en_dt-$st_dt;
                  $dt = strtotime('+'.$i.' day',strtotime($start_date));
                  $tmp .= ', '.date('j', $dt).date('S', $dt);
            }
            $format[70] = $st_mn_f." ".$st_OrdDt.$tmp." & ".$en_OrdDt;
      }
      if($st_mn==$en_mn)
      $format[71] = $st_dt." – ".$en_dt." ".$en_mn_f;
      $format[72] = $st_dt0.".".$st_mn0."-".$en_dt0.".".$en_mn0;
      if($st_mn==$en_mn)
      $format[73] = $st_mn_f." ".$st_dt."-".$en_dt;
      $format[74]= $st_day_s." ".$st_mn_s." ".$st_OrdDt." - ".$en_day_s." ".$en_mn_s." ".$en_OrdDt;
      $format[75] = $st_day_f.", ".$st_mn_f." ".$st_OrdDt;
      $format[76] = $st_day_f.", ".$st_mn_f." ".$st_dt;
      $tmp="";
      if($en_dt-$st_dt >= 1 && $st_mn==$en_mn)
      {           
            for ($i=1; $i <($en_dt-$st_dt) ; $i++) { 
                  # code...
                  // echo $en_dt-$st_dt;
                  $dt = strtotime('+'.$i.' day',strtotime($start_date));
                  $tmp .= ', '.date('j', $dt).date('S', $dt);
            }
            $format[77] = $st_mn_f." ".$st_OrdDt.$tmp." & ".$en_OrdDt;
      }
      
      $format[78] = $st_mn_f." ".$st_dt." - ".$en_mn_f." ".$en_dt;
      $format[79] = $st_mn_s." ".$st_dt0." To ".$en_mn_s." ".$en_dt0;
      $format[80] = $st_day_f." ".$st_mn_f." ".$st_dt;
      if($st_mn==$en_mn)
            $format[81] = $st_dt." - ".$en_dt." ".$en_mn_f;  
      $format[82] = $st_dt." ".$st_mn_s." - ".$en_dt." ".$en_mn_f;
      $format[83] = $st_dt0." ".$st_mn_s." - ".$en_dt0." ".$en_mn_s;
      $tmp="";
      if($en_dt-$st_dt >= 1 && $st_mn==$en_mn)
      {           
            for ($i=1; $i <($en_dt-$st_dt) ; $i++) { 
                  # code...
                  // echo $en_dt-$st_dt;
                  $dt = strtotime('+'.$i.' day',strtotime($start_date));
                  $tmp .= ', '.date('j', $dt);
            }
            $format[84] = $st_mn_f." ".$st_dt.$tmp." & ".$en_dt;
      }
      $format[85] = $st_mn_f." ".$st_dt."-".$en_mn_s.". ".$en_dt;
      if($st_mn==$en_mn)
            $format[86] = $st_dt." - ".$en_dt." ".$en_mn_f;
      $format[87] = $st_day_f.", ".$st_mn_f." ".$st_dt." – ".$en_day_f.", ".$en_mn_f." ".$en_dt;
      $tmp="";
      if($en_dt-$st_dt >= 1 && $st_mn==$en_mn)
      {           
            for ($i=1; $i <($en_dt-$st_dt) ; $i++) { 
                  # code...
                  $dt = strtotime('+'.$i.' day',strtotime($start_date));
                  $tmp .= ', '.date('j', $dt);
            }
            $format[88] = $st_mn_f." ".$st_dt.$tmp." and ".$en_dt;
      }
      if($st_mn==$en_mn)
            $format[89] = $st_mn_f." ".$st_OrdDt."-".$en_OrdDt;
      if($st_mn==$en_mn)
            $format[90] = $st_dt."-".$en_dt." ".$en_mn_f;
      if($st_mn<10)
            $format[91] = $st_mn.".".$st_dt." ".$st_day_s." ".$en_mn.".".$en_dt." ".$en_day_s;
      $format[92] = $st_day_f." ".$st_dt."/".$st_mn0;
      if($en_dt-$st_dt<2)
      $format[93] = $st_day_f.", ".$st_mn_f." ".$st_dt." and ".$en_day_f.", ".$en_mn_f." ".$en_dt;
      $format[94] = $st_day_f.", ".$st_mn_f." ".$st_dt." to ".$en_day_f.", ".$en_mn_f." ".$en_dt;
      if($en_dt-$st_dt<2 && $st_mn==$en_mn)
      $format[95] = $st_day_f." ".$st_OrdDt." and ".$en_day_f." ".$en_OrdDt." ".$en_mn_f;
      if($st_mn==$en_mn)
      $format[96] = $st_mn_f." ".$st_dt."-".$en_dt;
      if($st_mn==$en_mn)
            $format[97] = $st_dt.". - ".$en_dt.". ".$en_mn_f;
      $format[98] = $st_day_f.", ".$st_mn_f." ".$st_dt;
      $format[99] = $st_dt." ".$st_mn_s." – ".$en_dt." ".$en_mn_s;
      if($st_mn==$en_mn)
            $format[100] = $st_dt0.". – ".$en_dt0.". ".$en_mn_f;
      $format[101] = $st_mn_f.".".$st_dt." - ".$en_mn_f.".".$en_dt;
      $format[102] = $st_OrdDt." of ".$st_mn_f." to ".$en_OrdDt." of ".$en_mn_f;
      $format[103] = $st_dt0."/".$st_mn0." - ".$en_dt0."/".$en_mn0;
      if($st_mn==$en_mn)
      $format[104] = $st_mn_f." ".$st_dt." – ".$en_dt;
      if($st_mn==$en_mn)
            $format[105] = $st_OrdDt." to ".$en_OrdDt." of ".$en_mn_f;
      if($st_mn==$en_mn)
            $format[106] = $st_OrdDt."-".$en_OrdDt.".".$en_mn_f;
      if($st_mn==$en_mn && $st_mn<10)
            $format[107] = $st_mn.".".$st_dt." - ".$en_dt;
      if($st_mn==$en_mn)
      $format[108] = $st_mn_s.". ".$st_OrdDt."-".$en_OrdDt;
      $format[109] = $st_dt0."/".$st_mn0;
      $format[110] = $st_dt." ".$st_mn_f." - ".$en_dt." ".$en_mn_f;
      if($st_mn==$en_mn)
            $format[111] = $st_mn_f." ".$st_dt." to ".$en_dt;
      if($st_mn==$en_mn)
            $format[112] = $st_mn_f." ".$st_OrdDt." to ".$en_mn_f." ".$en_OrdDt;
      if($st_mn==$en_mn)
            $format[113] = $st_dt." ".$st_mn_f." to ".$en_dt." ".$en_mn_f;
      if($st_mn==$en_mn)
            $format[114] = $st_mn_f." ".$st_dt0."-".$en_dt0;
      if($st_mn==$en_mn)
            $format[115] = $st_OrdDt."-".$en_OrdDt." ".$en_mn_f;
      if($st_mn==$en_mn)
            $format[116] = $st_day_f.", ".$st_mn_f." ".$st_dt." – ".$en_day_f.",".$en_mn_f." ".$en_dt;
      $format[117] = "Start: ".$st_mn_f." ".$st_dt0;
      $format[118] = "End: ".$en_mn_f." ".$en_dt0;
      if($st_mn==$en_mn)
            $format[119] = $st_dt.". - ".$en_dt.". ".$en_mn_f;
      if($st_mn==$en_mn)
            $format[120] = $st_mn0.".".$st_dt0."-".$en_dt0;
      $format[121] = $st_mn.".".$st_dt." ".$st_day_s." ".$en_mn.".".$en_dt." ".$en_day_s;
      if($st_mn==$en_mn)
            $format[122] = $st_mn.".".$st_dt." - ".$en_dt;
      if($st_mn==$en_mn)
            $format[123] = $st_mn_s." ".$st_OrdDt."-".$en_OrdDt;
      if($st_mn==$en_mn)
            $format[124] = $st_OrdDt." - ".$en_OrdDt." ".$en_mn_s.", ".$en_yr;
            $format[125] = $st_mn."/".$st_dt."/".$st_yr;
            $format[126] = $st_OrdDt." ".$st_mn_f;
            $format[127] = $st_OrdDt." ".$st_mn_f." ".$en_yr;
            $format[128] = $st_mn_s." ".$st_dt."/".$en_dt;
            $format[129] = $st_mn_s.". ".$st_dt;
            $format[130] = $st_mn_s." ".$st_dt;
            $format[140] = $st_dt0.".".$st_mn0.".".$st_yr." - "$en_dt0.".".$en_mn0.".".$en_yr;
            $format[141] = $st_dt0.". ".$st_mn_f." ".$st_yr;
            $format[142] = $st_mn_s." ".$st_OrdDt.", ".$st_yr;
            $format[143] = $st_dt0.". ".$st_mn0." - ".$en_dt0.". ".$en_mn0.". ".$en_yr;
            $format[144] = $st_day_f." ".$st_OrdDt." ".$st_mn_f;
            $format[145] = $st_dt0.".".$st_mn0." -".$en_dt0.".".$en_mn0.".".$en_yr;
            $format[146] = $st_mn_s." ".$st_dt.", ".$en_yr;
            $format[147] = $st_mn_f."&nbsp;".$st_OrdDt." & ".$en_mn_f."&nbsp;".$en_OrdDt;
            $format[148] = $st_day_f." ".$st_OrdDt." ".$st_mn_f." ".$st_yr;
            $format[149] = $st_mn_s.", ".$st_OrdDt.", ".$st_yr;
            $format[150] = $st_mn_f." ".$st_OrdDt." ".$st_yr;
      
      



      // make for loop for push array format; Check for "" for Empty values not to push;
        $dateFound = 0;
      for ($i=0; $i < count($format) ; $i++) 
       { 
            if(!empty($format[$i]))
            {
                 if(stripos($Wval, $format[$i]) !== false)
                    {$dateFound=1;break;}
            }
        }
        if($dateFound!=1)
            if(!empty($Wval) && !empty($data['website']))
                      {
                        $csv_data.=$data['id']."\t".$data['name']."\t".$data['website']."\t".$st_en_date."\n";
                      }
}

$hitData['path'] = '/home/indiamart/public_html/10into/web/manage/csv/Previous_Day_Publish_events.tsv';
  $hitData['type'] = "w";
  $hitData['fileType'] = "tsv";
  $hitData['data'] =$csv_data;
  $options = array('http' =>
      array(
        'method'  => 'POST',
        'header'  => 'Content-type: application/x-www-form-urlencoded',
        'content' => http_build_query($hitData)
        )
      );
  $context  = stream_context_create($options);
  $mail = file_get_contents('http://'.$domain.'/index.php/v1/crm/readWriteFile', false, $context);
print_r($mail);

$email=array('apoorva@10times.com','sharad@10times.com','rajkumar@10times.com');

      $senddata['from'] = "report@10times.com";
      $senddata['from_name'] = "10times";
      $senddata['subject'] = "Published Events' Date Auto-Reverification (".$today.")";
      $senddata['type']='emails';
      $senddata['emails']= $email;
      $senddata['category']= "user_system_blacklist_domains_update";
      $senddata['message'] ="List of Updated blacklist_domains<br>";
      $senddata['attachments'][0]['mime']='text/tsv';
      $senddata['attachments'][0]['path']=$hitData['path'];

      $options = array('http' =>
        array(
          'method'  => 'POST',
          'header'  => 'Content-type: application/x-www-form-urlencoded',
          'content' => http_build_query($senddata)
          )
        );
      $context  = stream_context_create($options);
      $result_mail = file_get_contents('http://'.$domain.'/index.php/user/send_mail', false, $context);
print_r($result_mail);

$update=update_cron_status(279, "Published Events Date Auto-Reverification");

?>