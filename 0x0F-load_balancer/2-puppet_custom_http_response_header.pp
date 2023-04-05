# puppet config for custom
# http header

exec { 'custom_header':
  command => "sudo sed -i \"40i \\\tadd_header X-Served-By \"${hostname}\";\n\" /etc/nginx/sites-available/default",
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
