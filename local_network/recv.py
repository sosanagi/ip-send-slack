from __future__ import print_function
import socket
from contextlib import closing

def main():
  local_address   = '10.0.0.XXX' # 受信側のPCのIPアドレス
  multicast_group = '239.255.0.1' # マルチキャストアドレス
  port = 4000
  bufsize = 409

  print("please wait")

  with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_ADD_MEMBERSHIP,
                    socket.inet_aton(multicast_group) + socket.inet_aton(local_address))

    while True:
      print(sock.recv(bufsize).decode())
      
  return

if __name__ == '__main__':
  main()
