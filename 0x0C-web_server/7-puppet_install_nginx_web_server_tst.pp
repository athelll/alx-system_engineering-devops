# puppet

class { 'nginx':
  provider => 'apt',
}

exec { 'landing_page':
  command => 'sudo echo "Hello World!" > /var/www/html/index.nginx-debian.html',
}

exec { 'redirect_handle':
  command => 'sudo sed -i "45i \\\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4; \n\t}\n" /etc/nginx/sites-available/default'
}

exec { 'start_nginx':
  command => 'sudo service nginx start'
}
