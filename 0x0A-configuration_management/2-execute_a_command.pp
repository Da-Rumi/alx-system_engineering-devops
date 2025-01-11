#a manifest that kills a process named

exec {'pkill killmenow':
    command  => 'pkill killmenow',
    provider => shell,
}
