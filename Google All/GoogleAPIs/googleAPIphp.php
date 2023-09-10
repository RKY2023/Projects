<?php
echo "https://developers.google.com/gmail/api/reference/rest";

function tryPOst()
{

    $_POST['user']='encode_'.$_POST['user'].'_'.$_POST['encodeUser'];        
    $_POST['key']=$this->container->getParameter('auth_key');
    $data=$_POST;
    // $data['10t-cookie']=json_encode($_COOKIE);
    // $data['10t-esdata']=json_encode($_SERVER) ;
    $data['ip']=$this->get('acme.twig.acme_extension')->ipDetect();
    //http://'.SERVE_BTS.'/index.php/v2/auth/
       // $url = 'http://serve.biztradeshows/index.php/v2/auth/';
        $url = 'http://'.SERVE_BTS.'/index.php/v2/auth?'.http_build_query($data);
        $options = array(
            'http' => array(
                'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                'method'  => 'POST',
                'content' => http_build_query($data),
            ),
        );
        $context  = stream_context_create($options);
        $result = file_get_contents($url, false, $context);
        $status_data=json_decode($result,true);

        echo  $result;

        exit;
}

function googleProfile()
{
    // $url = 'https://gmail.googleapis.com/gmail/v1/users/{userId}/profile';
	$user_email='rajdelhi2023@gmail.com';
    $url = 'https://gmail.googleapis.com/gmail/v1/users/'.$user_email.'/profile';
    $result = file_get_contents($url);

    // $data='';
    // $options = array(
    //     'http' => array(
    //         'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
    //         'method'  => 'GET',
    //         'content' => http_build_query($data),
    //     ),
    // );
    // $context  = stream_context_create($options);
    // $result = file_get_contents($url, false, $context);
    // $status_data=json_decode($result,true);

    echo  $result;

    exit;
}
googleProfile();
?>
