import re
asa_conn = 'TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\nTCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'
asa_dict={}
for conn in asa_conn.split('\n'):
   # print(conn)
    re_result=re.match("\S+\s+\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)\s+\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)\S+\s+\S+\s+\d{1,2}:\d{1,2}:\d{1,2}\S+\s+\S+\s+(\d+)\S+\s+\S+\s+(\S+)",conn).groups()
    print(re_result)
    #asa_dict[re_result[0:4]] = (re_result[-2:])
   # print("打印分析后的字典")
