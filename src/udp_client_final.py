# -*- coding: utf8 -*-
import cv2
import socket
import numpy as np
import time

import threading
import queue

# HOST= '192.168.0.20'
# PORT= 8654

HOST = '192.168.219.103'
PORT = 8486

COMPLETE_DETECT = "9"
STOP_DETECT = 9
START_DETECT = 2

flag = False

## TCP 사용
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
## server ip, port
  
## webcam 이미지 capture
cam = cv2.VideoCapture(0)
 
## 이미지 속성 변경 3 = width, 4 = height
cam.set(3, 640);
cam.set(4, 400);
 
## 0~100에서 90의 이미지 품질로 설정 (default = 95)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    
    # key = cv2.waitKey(10)
    
    if cv2.waitKey(10) == ord("q"):
        flag = True
        print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
    elif cv2.waitKey(10) == ord("s"):
        flag = False
        print("sssssssssssssssssssssssssssssssssssss")
        
    print(flag)
        
    ret, frame = cam.read()
    cv2.imshow("client", frame)
    cv2.waitKey(1)

    d = frame.flatten()
    ss = d.tobytes()
    
    if flag:    
        for i in range(20):
            # s.sendto(bytes([i]) + START_DETECT + s[i*46079:(i+1)*46079], (HOST, PORT))
            s.sendto(bytes([i]) + b'\x02' + ss[i*38400:(i+1)*38400], (HOST, PORT))
    else:
        for i in range(20):
            # j=9
            # print(("1", bytes([i]) + bytes(j)))
            # print((i, bytes([i])))
            # print(("9", bytes(j)))
            # print(len((bytes([i]) + bytes(9) + ss[i*46080:(i+1)*46080])))
            # print(b'\x01')
            # print(len(b'\x01'))
            # print(len((bytes([i]) + b'\x01' + ss[i*46079:(i+1)*46079])))
            s.sendto(bytes([i]) + b'\x01' + ss[i*38400:(i+1)*38400], (HOST, PORT))
    
    
    data, addr = s.recvfrom(16)
    msg = data.decode()
    print(msg, type(msg))
    