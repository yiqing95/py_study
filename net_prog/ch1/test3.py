__author__ = 'yiqing'

import  socket

def get_remote_machine_info():
    remote_host = 'www.python.com'
    try:
        print("IP address : %s " % socket.gethostbyname(remote_host))
    except socket.error as err:
        print("%s " % err)


if __name__ == '__main__':
    get_remote_machine_info()