# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 02:37:39 2019

@author: sanke
"""


            
          
import numpy as np
import math

#  Take input from the user
user_input=input("Enter numbers seperated by a space : ") 
split_str=user_input.split(' ')
List=[]

for num in split_str:
    List.append(int(num))




#  Check the number of inversions
def inversions(array):  
    n=len(array)
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (array[i] > array[j] and array[i]!=0 and array[j]!=0): 
                inv_count += 1
    return inv_count 
   

#  Change the output file into the given format ( 1,4,7,2,5,8,3,6,0 instead of 1,2,3,4,5,6,7,8,0)
def change(mat):         
    x=np.reshape(mat,(3,3))
    y=x.T
    z=np.reshape(y,(1,-1))
    y=z[0]    
    return y 

inv_count=inversions(List)

#  Check whether a number exists in a list
def number_exists(array,n): 
    tag=False
    for i in array:
        if i==n:
            tag=True
            break
    return tag

#  Return a distinct number for a list
def distinct_number(h): 
   numb=0 
   for i in range(0,len(h)) :
        x=len(h)+12-i
        n=math.pow(10,x)
        numb+= h[i]*n
   return numb

goal=[1,2,3,4,5,6,7,8,0]
solution=distinct_number(goal)


#  For even number of inversions puzzle is solvable.
if (inv_count % 2 == 0):  
    print("Solution Exists")

    nodes=[List]
    
    nums=[distinct_number(List)]
    tag=True
    depth=0
    node_no=1
    n=[1,0,0]
    node_info=[n]
    len1=0
    count=0
    while tag:
        
        len2=len(nums)
        c=len2
        depth=depth+1
        print(depth)
        
        for pos in range(len1,len2):
            loc=nodes[pos].index(0)
                    
#  moveDown            
            if loc + 3 < len(List) :                               
                temp=nodes[pos].copy()
                temp[loc], temp[loc + 3] = temp[loc + 3], temp[loc]
                sol=distinct_number(temp)

                
                if not (number_exists(nums,sol)) :
                    node_no+=1
                    count=count+1
                    nums.append(sol)
                    n=[node_no,pos+1,depth]
                    node_info.append(n)
                    nodes.append(temp)
                    
                    if sol==solution:
                        tag=False
                        print("Solution Found")
                        break


#  moveUp                     
            if loc - 3>=0 :                   
                temp=nodes[pos].copy()
                temp[loc], temp[loc - 3] = temp[loc - 3], temp[loc]  
                sol=distinct_number(temp)
                            
                
                
                if not (number_exists(nums,sol)) :
                    node_no+=1
                    count=count+1
                    nums.append(sol)
                    n=[node_no,pos+1,depth]
                    node_info.append(n)
                    nodes.append(temp)
                    
                    
                    
                    if sol==solution:
                        tag=False
                        print("Solution Found")
                        
                        break
            
#  moveLeft                      
            if loc % 3 > 0 :                     
                temp=nodes[pos].copy()
                temp[loc], temp[loc - 1] = temp[loc - 1], temp[loc]
                sol=distinct_number(temp)

                
                if not (number_exists(nums,sol)) :
                    
                    node_no+=1
                    count=count+1
                    nums.append(sol)
                    n=[node_no,pos+1,depth]
                    node_info.append(n)
                    nodes.append(temp)
                    
                    if sol==solution:
                        tag=False
                        print("Solution Found")
                        break
                    
#  moveRight                    
            if loc % 3 < 2:                                    
                temp=nodes[pos].copy()
                temp[loc], temp[loc + 1] = temp[loc + 1], temp[loc]
                sol=distinct_number(temp)
                if not (number_exists(nums,sol)) :
                    node_no+=1
                    count=count+1
                    nums.append(sol)
                    n=[node_no,pos+1,depth]
                    node_info.append(n)
                    nodes.append(temp)
                    
                    if sol==solution:
                        tag=False
                        print("Solution Found")
                        break
    
    
        if count==0:
            print("No Solution Found")
            tag=False
            break
        len1=c
        count=0
       
    print(node_info)
    
    
    
#  Trace back the path using information from nodes_info and nodes.    
    fn=node_no-1                           
          
    path=[]
    
#  Get the path from the first node to the last
    
    while (fn > 0):
            path.append(nodes[fn])
            k=fn
            fn=(node_info[k][1])-1
    path.append(List)
    reverse_path=path[::-1]  
    
    reverse_order=[]
    for path in reverse_path:
        reverse_order.append(change(path))
    node1=[]
    for node in nodes:
        node1.append(change(node))
        
    
#  Write Nodes file
    file=open('nodes.txt','w')    
    for node in node1:
        file.write("\n") 
        for nde in node:
            file.write(str(nde)+" ")
               
#  Write Node_Info file
    file.close()
    file1=open('node_info.txt','w')
    for node_i in node_info:    
        file1.write("\n")
        for nde in node_i:
            file1.write(str(nde)+ " ")    
    file1.close()
    
    file2=open('node_path.txt','w')
    for path in reverse_order:
        file2.write("\n")
        for i in path:
            
            file2.write(str(i)+" ")    
    file2.close()
    
# If number of inversions is odd then puzzle is not solvble
    
else:
    print("Not Solvable")
    file=open('nodes.txt','w')
    file.write("Not Solvable")
    file.close()
    file1=open('node_info.txt','w')
    file1.write("Not Solvable")
    file1.close()
    file2=open('node_path.txt','w')
    file2.write("Not Solvable")
    file2.close()