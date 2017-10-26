#!/usr/bin/python
#coding:utf-8
import paramiko
class Machine():
    def __init__(self,ip,username,password):
        self.ip=ip
        self.username=username
        self.password=password

    def getHostname(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.ip, port=22, username=self.username, password=self.password)
        hostnameCommand="hostname"
        stdin, stdout, stderr = ssh.exec_command(hostnameCommand)
        hostname=stdout.readline()
        ssh.close()
        return hostname

    def getCpuInfo(self):
        result=[]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.ip, port=22, username=self.username, password=self.password)
        cpuNum = "cat /proc/cpuinfo | grep \"physical id\" | sort | uniq | wc -l"
        cpuCore = "cat /proc/cpuinfo| grep \"cores\"| uniq | awk -F \":\" \'{print $2}\'"
        cpuInfo = "cat /proc/cpuinfo | grep \"model name\" | uniq | awk -F \":\" \'{print $2}\'"
        stdin, stdout, stderr = ssh.exec_command(cpuCore)
        result.append(stdout.readline().strip())
        stdin, stdout, stderr = ssh.exec_command(cpuNum)
        result.append(stdout.readline().strip())
        stdin, stdout, stderr = ssh.exec_command(cpuInfo)
        result.append(stdout.readline().strip())
        ssh.close()
        return result

    def getDisk(self):
        disk=[]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.ip, port=22, username=self.username, password=self.password)
        diskCommand = "fdisk -l | grep Disk | grep -v \"identifier\""
        stdin, stdout, stderr = ssh.exec_command(diskCommand)
        for line in stdout.readlines():
            disk.append(line)
        ssh.close()
        return disk


    def getMemory(self):
        memory= []
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.ip, port=22, username=self.username, password=self.password)
        memoryCommand = "dmidecode | grep -A16 \"Memory Device$\" | grep Size | grep -v \"No\""
        stdin, stdout, stderr = ssh.exec_command(memoryCommand)
        for line in stdout.readlines():
            memory.append(line)
        ssh.close()
        return memory




