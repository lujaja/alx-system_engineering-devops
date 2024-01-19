# create a manifest that kills a process named killmenow

exec {'pkill':
  command  => 'pkill -9 killmenow',
  provider => 'shell',
}
