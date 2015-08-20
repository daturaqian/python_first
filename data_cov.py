# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:12:52 2015

@author: qianjunzhou
"""
data_base = raw_input("please the initial value of the array:\n")

data_array = [[[data_base for i in range(3)] for j in range(96)] for k in range(32)]
    

#print(data_array)


#set up the input data array
print("all the data value is "+ data_base)
write_mode = raw_input("do you want to modify the data if yes please type 1, if no type 0:\n")
while(int(write_mode)):
    disp_str   =  '''please select your modify style 1 represents row_mode, 0 represent dot mode:
2 represents list_mode, 3 represetns bias mode \n'''
    row_mode   = raw_input(disp_str)
    if(int(row_mode) == 1 or int(row_mode) == 0):
        row_32     = raw_input("please type in the row number range from 0 - 31:\n")
        if(int(row_32) < 0 or int(row_32) > 31):
            row_32     = raw_input("value wrong!!!! please type in the row name range from 0 - 31:\n")
    if(int(row_mode)== 0 or int(row_mode) == 2):
        list_96 = raw_input("please type in the list number range from 0 - 95:\n")
        if(int(list_96) > 95 or int(list_96) < 0):
            list_96 = raw_input("value wrong!!!! please type in the list number range from 0 - 95:\n")
    data_value_r = raw_input("please type the value of the R. if you do not want change the value of R type 0 \n")            
    if(data_value_r == "0"):
        data_value_r = data_base
    data_value_g = raw_input("please type the value of the G. if you do not want change the value of G type 0 \n")
    if(data_value_g == "0"):
        data_value_g = data_base    
    data_value_b = raw_input("please type the value of the B. if you do not want change the value of B type 0 \n")                
    if(data_value_b == "0"):
        data_value_b = data_base
    if(int(row_mode) == 1):
        for i in range(96):
            data_array[int(row_32)][i] = [data_value_r,data_value_g,data_value_b]
    elif(int(row_mode) == 2):
        for i in range(32):
            data_array[i][int(list_96)] = [data_value_r,data_value_g,data_value_b]
    elif(int(row_mode) == 3):
        for i in range(32):
            data_array[i][i*3+2] = [data_value_r,data_value_g,data_value_b]
    else:
        data_array[int(row_32)][int(list_96)] = [data_value_r,data_value_g,data_value_b]
    write_mode = raw_input("do you want to modify the data again if yes please type 1, if no type 0:\n")

#split the data array into R G B three arrays
#initial generate the three arrays

data_array_r = [[[] for i in xrange(96)] for j in range(32)]
data_array_g = [[[] for i in xrange(96)] for j in range(32)]
data_array_b = [[[] for i in xrange(96)] for j in range(32)]

#start the split the array
for i in range(32):
    for j in range(96):
        data_array_r[i][j] = int(data_array[i][j][0],16)
        data_array_r[i][j] = bin(data_array_r[i][j])[2:18]
        data_array_r[i][j] = data_array_r[i][j][::-1]+"0000000000000000"
        data_array_r[i][j] = data_array_r[i][j][0:16]
        data_array_r[i][j] = data_array_r[i][j][::-1]
    
for i in range(32):
    for j in range(96):
        data_array_g[i][j] = int(data_array[i][j][1],16)
        data_array_g[i][j] = bin(data_array_g[i][j])[2:18]
        data_array_g[i][j] = data_array_g[i][j][::-1]+"0000000000000000"
        data_array_g[i][j] = data_array_g[i][j][0:16]
        data_array_g[i][j] = data_array_g[i][j][::-1]

for i in range(32):
    for j in range(96):
        data_array_b[i][j] = int(data_array[i][j][2],16)
        data_array_b[i][j] = bin(data_array_b[i][j])[2:18]
        data_array_b[i][j] = data_array_b[i][j][::-1]+"0000000000000000"
        data_array_b[i][j] = data_array_b[i][j][0:16]
        data_array_b[i][j] = data_array_b[i][j][::-1]

#set initial split array
data_array_r_1 = [[[] for i in range(32)] for j in range(32)]
data_array_r_2 = [[[] for i in range(32)] for j in range(32)]
data_array_r_3 = [[[] for i in range(32)] for j in range(32)]
data_array_g_1 = [[[] for i in range(32)] for j in range(32)]
data_array_g_2 = [[[] for i in range(32)] for j in range(32)]
data_array_g_3 = [[[] for i in range(32)] for j in range(32)]
data_array_b_1 = [[[] for i in range(32)] for j in range(32)]
data_array_b_2 = [[[] for i in range(32)] for j in range(32)]
data_array_b_3 = [[[] for i in range(32)] for j in range(32)]

#set initial write array
data_write_r = [[] for i in range(32*96)]
data_write_g = [[] for i in range(32*96)]
data_write_b = [[] for i in range(32*96)]

#change the array size
for i in range(32):
    for j in range(0,32):
        data_array_r_1[i][j] = data_array_r[i][j]
    for j in range(32,64):
        data_array_r_2[i][j-32] = data_array_r[i][j]
    for j in range(64,96):
        data_array_r_3[i][j-64] = data_array_r[i][j]
        
for i in range(32):
    for j in range(0,32):
        data_array_g_1[i][j] = data_array_g[i][j]
    for j in range(32,64):
        data_array_g_2[i][j-32] = data_array_g[i][j]
    for j in range(64,96):
        data_array_g_3[i][j-64] = data_array_g[i][j]
        
for i in range(32):
    for j in range(0,32):
        data_array_b_1[i][j] = data_array_b[i][j]
    for j in range(32,64):
        data_array_b_2[i][j-32] = data_array_b[i][j]
    for j in range(64,96):
        data_array_b_3[i][j-64] = data_array_b[i][j]
r = 0    
for i in range(32):
    for j in range(15,-1,-1):
        data_write_r[r] = data_array_r_1[i][0][j]+data_array_r_1[i][1][j]+data_array_r_1[i][2][j]\
                        + data_array_r_1[i][3][j]+data_array_r_1[i][4][j]+data_array_r_1[i][5][j]\
                        + data_array_r_1[i][6][j]+data_array_r_1[i][7][j]+data_array_r_1[i][8][j]\
                        + data_array_r_1[i][9][j]+data_array_r_1[i][10][j]+data_array_r_1[i][11][j]\
                        + data_array_r_1[i][12][j]+data_array_r_1[i][13][j]+data_array_r_1[i][14][j]\
                        + data_array_r_1[i][15][j]
        r = r + 1
    for j in range(15,-1,-1):
        data_write_r[r] = data_array_r_1[i][16][j]+data_array_r_1[i][17][j]+data_array_r_1[i][18][j]\
                        + data_array_r_1[i][19][j]+data_array_r_1[i][20][j]+data_array_r_1[i][21][j]\
                        + data_array_r_1[i][22][j]+data_array_r_1[i][23][j]+data_array_r_1[i][24][j]\
                        + data_array_r_1[i][25][j]+data_array_r_1[i][26][j]+data_array_r_1[i][27][j]\
                        + data_array_r_1[i][28][j]+data_array_r_1[i][29][j]+data_array_r_1[i][30][j]\
                        + data_array_r_1[i][31][j]
        r = r + 1

for i in range(32):
    for j in range(15,-1,-1):
        data_write_r[r] = data_array_r_2[i][0][j]+data_array_r_2[i][1][j]+data_array_r_2[i][2][j]\
                        + data_array_r_2[i][3][j]+data_array_r_2[i][4][j]+data_array_r_2[i][5][j]\
                        + data_array_r_2[i][6][j]+data_array_r_2[i][7][j]+data_array_r_2[i][8][j]\
                        + data_array_r_2[i][9][j]+data_array_r_2[i][10][j]+data_array_r_2[i][11][j]\
                        + data_array_r_2[i][12][j]+data_array_r_2[i][13][j]+data_array_r_2[i][14][j]\
                        + data_array_r_2[i][15][j]
        r = r + 1
    for j in range(15,-1,-1):
        data_write_r[r] = data_array_r_2[i][16][j]+data_array_r_2[i][17][j]+data_array_r_2[i][18][j]\
                        + data_array_r_2[i][19][j]+data_array_r_2[i][20][j]+data_array_r_2[i][21][j]\
                        + data_array_r_2[i][22][j]+data_array_r_2[i][23][j]+data_array_r_2[i][24][j]\
                        + data_array_r_2[i][25][j]+data_array_r_2[i][26][j]+data_array_r_2[i][27][j]\
                        + data_array_r_2[i][28][j]+data_array_r_2[i][29][j]+data_array_r_2[i][30][j]\
                        + data_array_r_2[i][31][j]
        r = r + 1

for i in range(32):
    for j in range(15,-1,-1):
        data_write_r[r] = data_array_r_3[i][0][j]+data_array_r_3[i][1][j]+data_array_r_3[i][2][j]\
                        + data_array_r_3[i][3][j]+data_array_r_3[i][4][j]+data_array_r_3[i][5][j]\
                        + data_array_r_3[i][6][j]+data_array_r_3[i][7][j]+data_array_r_3[i][8][j]\
                        + data_array_r_3[i][9][j]+data_array_r_3[i][10][j]+data_array_r_3[i][11][j]\
                        + data_array_r_3[i][12][j]+data_array_r_3[i][13][j]+data_array_r_3[i][14][j]\
                        + data_array_r_3[i][15][j]
        r = r + 1
    for j in range(15,-1,-1):
        data_write_r[r] = data_array_r_3[i][16][j]+data_array_r_3[i][17][j]+data_array_r_3[i][18][j]\
                        + data_array_r_3[i][19][j]+data_array_r_3[i][20][j]+data_array_r_3[i][21][j]\
                        + data_array_r_3[i][22][j]+data_array_r_3[i][23][j]+data_array_r_3[i][24][j]\
                        + data_array_r_3[i][25][j]+data_array_r_3[i][26][j]+data_array_r_3[i][27][j]\
                        + data_array_r_3[i][28][j]+data_array_r_3[i][29][j]+data_array_r_3[i][30][j]\
                        + data_array_r_3[i][31][j]
        r = r + 1

g = 0    
for i in range(32):
    for j in range(15,-1,-1):
        data_write_g[g] = data_array_g_1[i][0][j]+data_array_g_1[i][1][j]+data_array_g_1[i][2][j]\
                        + data_array_g_1[i][3][j]+data_array_g_1[i][4][j]+data_array_g_1[i][5][j]\
                        + data_array_g_1[i][6][j]+data_array_g_1[i][7][j]+data_array_g_1[i][8][j]\
                        + data_array_g_1[i][9][j]+data_array_g_1[i][10][j]+data_array_g_1[i][11][j]\
                        + data_array_g_1[i][12][j]+data_array_g_1[i][13][j]+data_array_g_1[i][14][j]\
                        + data_array_g_1[i][15][j]
        g = g + 1
    for j in range(15,-1,-1):
        data_write_g[g] = data_array_g_1[i][16][j]+data_array_g_1[i][17][j]+data_array_g_1[i][18][j]\
                        + data_array_g_1[i][19][j]+data_array_g_1[i][20][j]+data_array_g_1[i][21][j]\
                        + data_array_g_1[i][22][j]+data_array_g_1[i][23][j]+data_array_g_1[i][24][j]\
                        + data_array_g_1[i][25][j]+data_array_g_1[i][26][j]+data_array_g_1[i][27][j]\
                        + data_array_g_1[i][28][j]+data_array_g_1[i][29][j]+data_array_g_1[i][30][j]\
                        + data_array_g_1[i][31][j]
        g = g + 1

for i in range(32):
    for j in range(15,-1,-1):
        data_write_g[g] = data_array_g_2[i][0][j]+data_array_g_2[i][1][j]+data_array_g_2[i][2][j]\
                        + data_array_g_2[i][3][j]+data_array_g_2[i][4][j]+data_array_g_2[i][5][j]\
                        + data_array_g_2[i][6][j]+data_array_g_2[i][7][j]+data_array_g_2[i][8][j]\
                        + data_array_g_2[i][9][j]+data_array_g_2[i][10][j]+data_array_g_2[i][11][j]\
                        + data_array_g_2[i][12][j]+data_array_g_2[i][13][j]+data_array_g_2[i][14][j]\
                        + data_array_g_2[i][15][j]
        g = g + 1
    for j in range(15,-1,-1):
        data_write_g[g] = data_array_g_2[i][16][j]+data_array_g_2[i][17][j]+data_array_g_2[i][18][j]\
                        + data_array_g_2[i][19][j]+data_array_g_2[i][20][j]+data_array_g_2[i][21][j]\
                        + data_array_g_2[i][22][j]+data_array_g_2[i][23][j]+data_array_g_2[i][24][j]\
                        + data_array_g_2[i][25][j]+data_array_g_2[i][26][j]+data_array_g_2[i][27][j]\
                        + data_array_g_2[i][28][j]+data_array_g_2[i][29][j]+data_array_g_2[i][30][j]\
                        + data_array_g_2[i][31][j]
        g = g + 1

for i in range(32):
    for j in range(15,-1,-1):
        data_write_g[g] = data_array_g_3[i][0][j]+data_array_g_3[i][1][j]+data_array_g_3[i][2][j]\
                        + data_array_g_3[i][3][j]+data_array_g_3[i][4][j]+data_array_g_3[i][5][j]\
                        + data_array_g_3[i][6][j]+data_array_g_3[i][7][j]+data_array_g_3[i][8][j]\
                        + data_array_g_3[i][9][j]+data_array_g_3[i][10][j]+data_array_g_3[i][11][j]\
                        + data_array_g_3[i][12][j]+data_array_g_3[i][13][j]+data_array_g_3[i][14][j]\
                        + data_array_g_3[i][15][j]
        g = g + 1
    for j in range(15,-1,-1):
        data_write_g[g] = data_array_g_3[i][16][j]+data_array_g_3[i][17][j]+data_array_g_3[i][18][j]\
                        + data_array_g_3[i][19][j]+data_array_g_3[i][20][j]+data_array_g_3[i][21][j]\
                        + data_array_g_3[i][22][j]+data_array_g_3[i][23][j]+data_array_g_3[i][24][j]\
                        + data_array_g_3[i][25][j]+data_array_g_3[i][26][j]+data_array_g_3[i][27][j]\
                        + data_array_g_3[i][28][j]+data_array_g_3[i][29][j]+data_array_g_3[i][30][j]\
                        + data_array_g_3[i][31][j]
        g = g + 1

b = 0    
for i in range(32):
    for j in range(15,-1,-1):
        data_write_b[b] = data_array_b_1[i][0][j]+data_array_b_1[i][1][j]+data_array_b_1[i][2][j]\
                        + data_array_b_1[i][3][j]+data_array_b_1[i][4][j]+data_array_b_1[i][5][j]\
                        + data_array_b_1[i][6][j]+data_array_b_1[i][7][j]+data_array_b_1[i][8][j]\
                        + data_array_b_1[i][9][j]+data_array_b_1[i][10][j]+data_array_b_1[i][11][j]\
                        + data_array_b_1[i][12][j]+data_array_b_1[i][13][j]+data_array_b_1[i][14][j]\
                        + data_array_b_1[i][15][j]
        b = b + 1
    for j in range(15,-1-1):
        data_write_b[b] = data_array_b_1[i][16][j]+data_array_b_1[i][17][j]+data_array_b_1[i][18][j]\
                        + data_array_b_1[i][19][j]+data_array_b_1[i][20][j]+data_array_b_1[i][21][j]\
                        + data_array_b_1[i][22][j]+data_array_b_1[i][23][j]+data_array_b_1[i][24][j]\
                        + data_array_b_1[i][25][j]+data_array_b_1[i][26][j]+data_array_b_1[i][27][j]\
                        + data_array_b_1[i][28][j]+data_array_b_1[i][29][j]+data_array_b_1[i][30][j]\
                        + data_array_b_1[i][31][j]
        b = b + 1

for i in range(32):
    for j in range(15,-1,-1):
        data_write_b[b] = data_array_b_2[i][0][j]+data_array_b_2[i][1][j]+data_array_b_2[i][2][j]\
                        + data_array_b_2[i][3][j]+data_array_b_2[i][4][j]+data_array_b_2[i][5][j]\
                        + data_array_b_2[i][6][j]+data_array_b_2[i][7][j]+data_array_b_2[i][8][j]\
                        + data_array_b_2[i][9][j]+data_array_b_2[i][10][j]+data_array_b_2[i][11][j]\
                        + data_array_b_2[i][12][j]+data_array_b_2[i][13][j]+data_array_b_2[i][14][j]\
                        + data_array_b_2[i][15][j]
        b = b + 1
    for j in range(15,-1,-1):
        data_write_b[b] = data_array_b_2[i][16][j]+data_array_b_2[i][17][j]+data_array_b_2[i][18][j]\
                        + data_array_b_2[i][19][j]+data_array_b_2[i][20][j]+data_array_b_2[i][21][j]\
                        + data_array_b_2[i][22][j]+data_array_b_2[i][23][j]+data_array_b_2[i][24][j]\
                        + data_array_b_2[i][25][j]+data_array_b_2[i][26][j]+data_array_b_2[i][27][j]\
                        + data_array_b_2[i][28][j]+data_array_b_2[i][29][j]+data_array_b_2[i][30][j]\
                        + data_array_b_2[i][31][j]
        b = b + 1

for i in range(32):
    for j in range(15,-1,-1):
        data_write_b[b] = data_array_b_3[i][0][j]+data_array_b_3[i][1][j]+data_array_b_3[i][2][j]\
                        + data_array_b_3[i][3][j]+data_array_b_3[i][4][j]+data_array_b_3[i][5][j]\
                        + data_array_b_3[i][6][j]+data_array_b_3[i][7][j]+data_array_b_3[i][8][j]\
                        + data_array_b_3[i][9][j]+data_array_b_3[i][10][j]+data_array_b_3[i][11][j]\
                        + data_array_b_3[i][12][j]+data_array_b_3[i][13][j]+data_array_b_3[i][14][j]\
                        + data_array_b_3[i][15][j]
        b = b + 1
    for j in range(15,-1,-1):
        data_write_b[b] = data_array_b_3[i][16][j]+data_array_b_3[i][17][j]+data_array_b_3[i][18][j]\
                        + data_array_b_3[i][19][j]+data_array_b_3[i][20][j]+data_array_b_3[i][21][j]\
                        + data_array_b_3[i][22][j]+data_array_b_3[i][23][j]+data_array_b_3[i][24][j]\
                        + data_array_b_3[i][25][j]+data_array_b_3[i][26][j]+data_array_b_3[i][27][j]\
                        + data_array_b_3[i][28][j]+data_array_b_3[i][29][j]+data_array_b_3[i][30][j]\
                        + data_array_b_3[i][31][j]
        b = b + 1

#start to write the data into file
fp_r = open("E:data_file_r.txt","w")
fp_g = open("E:data_file_g.txt","w")
fp_b = open("E:data_file_b.txt","w")

for i in range(r):
    fp_r.write(data_write_r[i]+"\n")
fp_r.close()
for i in range(g):
    fp_g.write(data_write_g[i]+"\n")
fp_g.close()
for i in range(b):
    fp_b.write(data_write_b[i]+"\n")
fp_b.close()

#start convert into HEX format

fp_r_h = open("E:data_file_r_h.txt","w")
fp_g_h = open("E:data_file_g_h.txt","w")
fp_b_h = open("E:data_file_b_h.txt","w")

for i in range(r):
    data_write_r[i] = int(data_write_r[i],2)
    data_write_r[i] = hex(data_write_r[i])[2:6]
    data_write_r[i] = data_write_r[i][::-1]+"0000"
    data_write_r[i] = data_write_r[i][:4]
    data_write_r[i] = data_write_r[i][::-1]
    fp_r_h.write(data_write_r[i]+"\n")
fp_r_h.close()

for i in range(g):
    data_write_g[i] = int(data_write_g[i],2)
    data_write_g[i] = hex(data_write_g[i])[2:6]
    data_write_g[i] = data_write_g[i][::-1]+"0000"
    data_write_g[i] = data_write_g[i][0:4]
    data_write_g[i] = data_write_g[i][::-1]
    fp_g_h.write(data_write_g[i]+"\n")
fp_g_h.close()

for i in range(b):
    data_write_b[i] = int(data_write_b[i],2)
    data_write_b[i] = hex(data_write_b[i])[2:6]
    data_write_b[i] = data_write_b[i][::-1]+"0000"
    data_write_b[i] = data_write_b[i][0:4]
    data_write_b[i] = data_write_b[i][::-1]
    fp_b_h.write(data_write_b[i]+"\n")
fp_b_h.close()


