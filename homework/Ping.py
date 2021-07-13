# #!/usr/bin/python
# # -*- author: pye_zhusg
# # -*- coding: UTF-8 -*-
# import logging
# logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
# from kamene.all import *
#
# def ping_test(ip):
#     ping_pkt = IP(dst=ip)/ICMP()
#     ping_result = sr1(ping_pkt, timeout=1, verbose=False)
#     if ping_result:
#         return 1
#     else:
#         return 0
# if __name__ == '__main__':
#     for ip in ['196.21.5.254','114.114.114.114']:
#         result = ping_test(ip)
#         if result == 1:
#             print(ip," 通!")
#         else:
#             print(ip," 不通!")
# !/usr/bin/python
#  -*- author: 李兴阳
#  -*- coding: UTF-8 -*-
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
def Ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result :
        return 1
    else:
        return 0
if __name__ == "__main__":
    for ip in ["111.111.11.1","114.114.114.114"]:
        #print(ip)
        result = Ping(ip)
        if result ==1:
            print(ip ,"通了")
        else:
            print(ip ,"没通")




