__author__ = 'yiqing'


import  socket ;

host_name = socket.gethostname() ;

print('Host name is %s ' % host_name)

print('Ip address is %s '% socket.gethostbyname(host_name))

# print_machine_info()



