#!/usr/bin/pup
# install a specific version of flask (2.1.0)
package {'python3-pip':
  ensure   => installed,
}

packages {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
