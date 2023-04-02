# puppet config

# installs nginx
class{ 'nginx':
  manage_repo    => true,
  package_source => 'nginx-mainline',
}

# creates file default return page
file { '/var/www/html/hello.html':
  ensure  => present,
  content => 'Hello World!',
}

# configurs server
nginx::resource::server { 'sixdeamon.tech':
  ensure      => present,
  listen_port => 80,
  www_root    => '/var/www/html/hello.html',
  location    => {
    '/redirect_me' => {
      return => '301 https://www.youtube.com/watch?v=QH2-TGUlwu4',
    },
  },
  notify      => Service['nginx'],
}

# ensures server is running
service { 'nginx':
  ensure => running,
  enable => true,
}
