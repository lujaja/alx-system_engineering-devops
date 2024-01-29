# Setup New Ubuntu server with nginx

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec { 'add_header_to_nginx':
  command     => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  path        => '/usr/bin:/bin', # Add the necessary path if required
  provider    => 'shell',
  refreshonly => true,             # Only run if notified
  subscribe   => File['/etc/nginx/sites-available/default'], # Notify when the file changes
}

file { '/etc/nginx/sites-available/default':
  ensure => present,
  notify => Exec['add_header_to_nginx'], # Notify the exec resource when the file changes
}


service {'nginx':                                                             
  ensure => running,                                                        
  require => Package['nginx']                                               
} 
