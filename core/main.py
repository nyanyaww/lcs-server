from core.SimpleServer import SimpleServer
from core.MessageHandle import MessageHandle


class Server(SimpleServer.SimpleServer):
    message = MessageHandle.MessageHandle()

    def __init__(self, port):
        super().__init__(port)

    def message_handle(self, receive_data, client):
        self.message.parsing = receive_data
        # 如果解析出来的数据是完整的
        if self.message.parsing.get('state') == 'data receive success':
            # 把关键的信息提取出来
            client_name = self.message.parsing['ip']
            self.client_name_dict[client_name] = client
            client_command = self.message.parsing.get('command')
            client_message = self.message.parsing.get('message')
            # 保存到对应名字的json文件夹下
            self.message.save(client_name, self.message.parsing)
            self.message.message_handle(client_name, client_command, client_message)
            server_send_command = 'receive state'
            server_send_message = 'ok'
            # if client_name == 'phone' or client_name == 'pc':
            # if client_name == 'dog':
            # 	self.message.encoding = (self.message.info_connect(
            # 			'server', 'feed', 'ok'), 'ascii')
            # 	self.receive_message_queue[self.client_hash['test']].put(
            # 			self.message.encoding)
            # else:
            # 将数据以一定形式编码成二进制
            self.message.encoding = (self.message.info_connect(
                'server', server_send_command, server_send_message), 'ascii')
            print('parsing information received from \ndevice:{0} is \'{1} : {2}\''.format(
                client_name, client_command, client_message))
            print(self.message.encoding, client_name)
            return self.message.encoding, client_name
            # self.receive_message_queue[self.client_hash[client_name]].put(
            #     self.message.encoding)
        # 解析出来的数据表明或多或少都有问题
        else:
            server_send_command = 'receive state'
            server_send_message = 'error'
            self.message.encoding = (self.message.info_connect(
                'server', server_send_command, server_send_message), 'ascii')
            print('no!!!!!!!!!')
            print('your message is GG!!!!!!!!')
            # client.send(self.message.encoding)
            return self.message.encoding, str(client)


if __name__ == '__main__':
    raspberry_server = Server(8086)
    raspberry_server.run()
