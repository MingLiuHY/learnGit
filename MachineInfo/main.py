#!/usr/bin/python
#coding:utf-8
from  machine import Machine
name="root"
password="beacon"
ip="15.44.20.111"
machine=Machine(ip,name,password);
hostname=machine.getHostname()
disk=machine.getDisk()
memory=machine.getMemory()
cpu=machine.getCpuInfo()
#print(info[0]+"*"+info[1]+" "+info[2])
with open("/tmp/data.txt",'a') as file:
    file.write(hostname+" "+ip+"\n")
    file.write(cpu[0]+"*"+cpu[1]+" "+cpu[2]+"\n")
    for d in range(len(disk)):
        if d == 0:
            file.write("硬盘:" + disk[d].strip()+"\n")
        else:
            file.write("\t" + disk[d].strip()+"\n")

    for m in range(len(memory)):
        if m==0:
            file.write("内存:"+memory[m].strip()+"\n")
        else:
            file.write("\t"+memory[m].strip()+"\n")




