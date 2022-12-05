# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
MAX_V = 100
N = 0
place = 0
visited = [None] * (MAX_V+1) #紀錄頂點是否已拜訪

#宣告相鄰串列
Top_order = [0] * (MAX_V+1)
adjlist = [None] * (MAX_V+1)


MAX_V = 30000
VISITED = 1
NOTVISITED = 0
Infinite = 1073741823

# A[1..N][1..N]為圖形的相鄰矩陣
# D[i] 用來儲存某起始頂點到i節點的最短路徑
# S[1..N] 用來紀錄頂點是否已經拜放過
# P[1..N] 用來記錄最近經過的中間節點
A = [[0] * (MAX_V+1) for row in range(MAX_V+1)]
D = [0] * (MAX_V+1)
S = [0] * (MAX_V+1)
P = [0] * (MAX_V+1)


a = list(range(10))
for i in range(10):
    print(i)


import sys

class TreeNode:
    def __init__(self):
        self.iD = 0 #輸出時識別節點
        self.n = 0 #節內的鍵數
        self.key = [0]*3 #節鍵
        self.link = [None]*3 #節點子節
         
MAX = 3 #設定此為3-WATRE最
ptr = None
root = None
node = None
prev = None
parent = None 
replace = None
id_seq = ''
#新增函數一新增一筆資料

def insert_f():
    add_num = int(input('\n Please enter insert number:'))
    create(add_num)
    print()
    

def search_node(num):
    global MAX
    global root
    node_temp = root
    while node_temp != None:
        if node_temp.n < MAX-1:
            return node_temp #找到有多餘空間存放NUM,具
        else:
            i = 1
            done = 0
            while i < MAX:
                if node_temp.n < i:
                    break
                if num < node_temp.key[i]:
                    node_temp = node_temp.link[i-1]
                    done = 1
                    break
                i += 1
            if done == 0:
                node_temp = node_temp.link[i-1]
            return node_temp #若沒有找到有多餘空間存放UM的節點

def create(num):
    global root
    global ptr
    global node
    global prev
    ans = 0
    i = 0
    if root == None: #樹根為空的狀況
        initial()
        ptr.key[1] = num
        ptr.n += 1
        root = ptr
    else:
        ans = search_num(num) #搜尋資料是否已存在
        if ans != 0: #資料存在,則顯示錯誤訊
            print("Number %d has existed!\n" % num)
        else:
            node = search_node(num) #找尋插入點
            if node != None: #插入點還有空存放資料的情況
                i = 1
                while i < MAX-1:
                    if num < node.key[i]:
                        break
                    i += 1
                moveright(i, num)
            else: #新增一個節點加入資料的狀況
                initial()
                ptr.key[1] = num
                ptr.n += 1
                while i < MAX:
                    if num < prev.key[i]:
                        break
                    i += 1
                prev.link[i-1] = ptr
    print('%10d has been inserted!' % num)

def initial():
    global MAX
    global ptr
    ptr = TreeNode()
    for i in range(MAX):
        ptr.link[i] = None
    ptr.n = 0

def search_num(num):
    global root
    global node
    global prev
    global parent
    n_temp = 0
    node = root
    while node != None:
        parent = prev
        prev = node
        i = 1
        done = 0
        while i <= node.n:
            if num == node.key[i]:
                return i #找到NUM,回優
            if num < node.key[i]:
                node = node.link[i-1]
                done = 1
                break
            i += 1
        if done == 0:
            node = node.link[i-1]
    return 0 #沒有找到則回傳0

def moveright(index, num):
    global node
    i = node.n + 1
    while i > index: #資料右移至INDEX處
        node.key[i] = node.key[i-1]
        node.link[i] = node.link[i-1]
        i -= 1
    node.key[i] = num #插入NUM

    if node.link[i-1] != None and node.link[i-1].key[0] > num:
        node.link[i] = node.link[i-1]
        i -= 1
    node.n += 1

def display_f():
    global root
    global id_seq
    if root == None:
        print("Im No data found!!\n")
    else:
        id_seq = 'a'
        preorder_id(root) #給予每個節點編號
        print("In The data of M-way search tree is listing below")
        print("=================================================")
        preorder_num(root) #輸出節點資料
        print("=================================================")

def preorder_id(tree):
    global id_seq
    if tree != None:
        tree.iD = id_seq
        id_seq = chr(ord(id_seq) + 1)
        for i in range(tree.n+1):
            preorder_id(tree.link[i])



def preorder_num(tree):
    i = 0
    link_id = ''
    if tree != None:
        # 當節點鍵結為OE,則現實鍵結為
        if tree != None:
            link_id = '0'
        else:
            link_id = tree.link[0].iD
        print(" %s, %d, %s" % (tree.iD, tree.n, link_id), end='')
        for i in range(1, tree.n+1):
            if tree.link[i] == None:
                link_id = '0'
            else:
                link_id = tree.link[i].iD
            print(', (%d, %s)' % (tree.key[i], link_id), end='')
            i += 1
        print()
        for i in range(tree.n+1):
            preorder_num(tree.link[i])



def main():
    option = 0
    while True:
        print("****m-waysearchtree****")
        print("* <1> Insert *")
        print("* <2> Delete *")
        print("* <3> Show *")
        print("* <4> Exit *")
        print("***********************")

        try:
            option = eval(input(' Choice:'))
        except ValueError:
            print("Not a correct number.")
            print("Try again")
        if option == 1:
            insert_f()#新增函數
# =============================================================================
#         elif option == 2:
#             delete_f()#刪除函數
# =============================================================================
        

main()
