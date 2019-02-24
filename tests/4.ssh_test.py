# import paramiko
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
#
# # 把要连接的机器添加到known_hosts文件中
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # 连接服务器
# ssh.connect(hostname='47.112.3.96', port=22, username='root', password='112358')
#
# cmd = 'ps'
# # cmd = 'cd ~;cd /etc;ls'       #多个命令用;隔开
# stdin, stdout, stderr = ssh.exec_command(cmd)
#
# result = stdout.read()
#
# if not result:
#     result = stderr.read()
# ssh.close()
#
# print(result.decode())

import paramiko

host_name = '47.112.3.96'
user_name = 'root'
user_password = '112358'
cmd = 'cd /root/lcs/xyb;python hello.py'


class SSHRaspberry(object):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = 22

    def login(self):
        self.ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)

    def run_cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        print(stdout.read().decode())

    def logout(self):
        self.ssh.close()


if __name__ == '__main__':
    raspberry = SSHRaspberry(host_name, user_name, user_password)
    raspberry.login()
    while True:
        your_input = input('>>')
        if your_input == 'quit':
            raspberry.logout()
            break
        else:
            raspberry.run_cmd(your_input)
