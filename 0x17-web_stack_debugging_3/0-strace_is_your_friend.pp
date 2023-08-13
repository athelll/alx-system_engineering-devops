# fixes bad `phpp` extensions to `php`
# using puppet for automation

exec { 'fix-wordpress':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path    => '/usr/local/bin:/bin/'
}
