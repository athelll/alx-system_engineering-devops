# kills a running process 
# named killmenow with puppet

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
