# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 01:16:39 2020

@author: farhad324
"""


import easygui
import cv2
import numpy as np

img = np.zeros((200,1000,3),np.uint8)


class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

    def remove_first(self):
        if self.tail is not None:
            self.__remove_node(self.head)

    def remove_last(self):
        if self.tail is not None:
            self.__remove_node(self.tail)

    def front(self):
        return self.head.val

    def back(self):
        return self.tail.val

    def getList(self):
        
        self.vals = []
        node = self.head
        while node is not None:
            self.vals.append(node.val)
            node = node.next
        return self.vals


my_list = DoubleLinkedList()

while 1:
    
    out= easygui.enterbox("Add or Remove Value", 'Double Linked List')
    if out == None or out=='':
        out='stop'
        
    if out.lower()=='stop' or cv2.waitKey(5) & 0xFF == 27:
        break
        
    out_value=int("".join(filter(str.isdigit, out)))
    out_command=out.replace(str(out_value),'')
    
    if 'add' in out_command.lower():
        my_list.add(int(out_value))
        img[:] = (256, 256, 256)
        vals=my_list.getList()
        j=104
        i = 0
        cv2.putText(img, "Double Linked List Visualization", (250, 35), cv2.FONT_HERSHEY_COMPLEX, 1, (255,50,30), 1, cv2.LINE_AA)
        while i< my_list.size:
            newj=j+60
            if i==0:
                cv2.circle(img, (22,100), 22, color=(0,0,256),thickness=2)
                cv2.putText(img, "None", (6, 100), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,255), 1, cv2.LINE_AA)
                cv2.line(img,pt1=(82,95),pt2=(44,95),color=(256,256,256),thickness=2)
                cv2.line(img,pt1=(82,105),pt2=(44,105),color=(256,256,256),thickness=2)
                cv2.putText(img, 'Size: '+str(my_list.size), (40, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,50,30), 1, cv2.LINE_AA)
            if my_list.size==1:
                cv2.putText(img, "Head", (j-16, 40), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
                cv2.putText(img, " & ", (j-16, 58), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
                cv2.putText(img, "Tail", (j-16, 75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
            elif i==0:
                cv2.putText(img, "Head", (j-16, 75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
            elif i==my_list.size-1:
                cv2.putText(img, "Tail", (j-16, 75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
            cv2.circle(img, (j,100), 22, color=(256,256,256),thickness=-1)
            cv2.line(img,pt1=(newj,95),pt2=(j,95),color=(256,256,256),thickness=2)
            cv2.line(img,pt1=(newj,105),pt2=(j,105),color=(256,256,256),thickness=2)
            if i==my_list.size-1:
                cv2.circle(img, (newj+22,100), 22, color=(0,0,256),thickness=2)
                cv2.putText(img, "None", (newj+6, 100), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,255), 1, cv2.LINE_AA)
            cv2.putText(img, str(vals[i]), (j-6, 105), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,50,30), 1, cv2.LINE_AA)
            
            j+=60
            i+=1
            
    elif 'remove' in out_command.lower():
        my_list.remove(int(out_value))
        img[:] = (256, 256, 256)
        vals=my_list.getList()
        j=104
        i = 0
        cv2.putText(img, "Double Linked List Visualization", (250, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,50,30), 1, cv2.LINE_AA)
        while i< my_list.size:
            newj=j+60
            if i==0:
                cv2.circle(img, (22,100), 22, color=(0,0,256),thickness=2)
                cv2.putText(img, "None", (6, 100), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,255), 1, cv2.LINE_AA)
                cv2.line(img,pt1=(82,95),pt2=(44,95),color=(256,256,256),thickness=2)
                cv2.line(img,pt1=(82,105),pt2=(44,105),color=(256,256,256),thickness=2)
                cv2.putText(img, 'Size: '+str(my_list.size), (40, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,50,30), 1, cv2.LINE_AA)
            if my_list.size==1:
                cv2.putText(img, "Head", (j-16, 40), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
                cv2.putText(img, " & ", (j-16, 58), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
                cv2.putText(img, "Tail", (j-16, 75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
            elif i==0:
                cv2.putText(img, "Head", (j-16, 75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
            elif i==my_list.size-1:
                cv2.putText(img, "Tail", (j-16, 75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,50,30), 1, cv2.LINE_AA)
            cv2.circle(img, (j,100), 22, color=(256,256,256),thickness=-1)
            cv2.line(img,pt1=(newj,95),pt2=(j,95),color=(256,256,256),thickness=2)
            cv2.line(img,pt1=(newj,105),pt2=(j,105),color=(256,256,256),thickness=2)
            if i==my_list.size-1:
                cv2.circle(img, (newj+22,100), 22, color=(0,0,256),thickness=2)
                cv2.putText(img, "None", (newj+6, 100), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,255), 1, cv2.LINE_AA)
            cv2.putText(img, str(vals[i]), (j-6, 105), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,50,30), 1, cv2.LINE_AA)
            
            j+=60
            i+=1
    cv2.putText(img, 'Developed by Farhad', (770, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,50,30), 1, cv2.LINE_AA)        
    cv2.imshow('Visualization Window',img)   
    
cv2.destroyAllWindows()
