""" Read kernel logs and write it to a file with name log-<date>-<time>.log """


import time
timestr = time.strftime("%Y%m%d-%H%M%S")

fo=open("log-"+timestr+".log",'w+')

with open('/var/log/dmesg') as logf:
    log=logf.read()

for info in log:
     fo.write(info)
