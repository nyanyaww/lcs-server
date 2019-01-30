# 多线程测试

import time
import threading


def fun():
    print("start fun")
    time.sleep(2)
    print("end fun")


if __name__ == '__main__':
    print("main thread")
    t1 = threading.Thread(target=fun, args=())
    # t1.setDaemon(True)
    t1.start()
    time.sleep(1)
    print("main thread end")