<?php
 function send_get()
    {
      //configuracion para gmail

      $config = array(
      'protocol' => 'smtp',
      'smtp_host' => 'ssl://smtp.gmail.com',
      'smtp_port' => 465,
      'mailtype' => 'html',
      'smtp_user' => 'thisismyinternetid@gmail.com',
      'smtp_pass' => '9443847471',
      'newline' => "\r\n",
     );
		$mail = new PHPMailer;
      //Load email library


      $this->load->library('email',$config);
      $this->email->set_newline("\r\n");

      $this->email->from('Sasi Kumar', '');
      $this->email->to('sasikumargowsi@gmail.com');
      $this->email->subject(' Visitor');
      $this->email->message('Testing the email class.');

     if($this->email->send()){
       echo "your email was sent";
     }
     else {
       show_error($this->email->print_debugger());
     }
    } 
	send_get();
	
?>