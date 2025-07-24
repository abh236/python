# envelopes =[[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]
# def maxEnvelopes(envelopes):
#     """
#     :type envelopes: List[List[int]]
#     :rtype: int
#     """
#     import copy
#     r = 0
#     ren = []
#     envelopes.sort()
#     a1 = copy.deepcopy(envelopes)
#     l = len(envelopes)
#     a = 0
#     ou = []

#     # Remove envelopes with same width or height
#     while a < l - 1:
#         if envelopes[a][0] == envelopes[a + 1][0] or envelopes[a][1] == envelopes[a + 1][1]:
#             if envelopes[a][0] == envelopes[a + 1][0]:
#                 ou = envelopes[a + 1]
#             envelopes.pop(a + 1)
#             a1.pop(a + 1)
#             l -= 1
#         else:
#             envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]
#             a += 1

#     if a == l - 1:
#         envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]

#     envelopes.sort()
#     if ou:
#         a1.append(copy.deepcopy(ou))
#     a1.sort()

#     a2 = copy.deepcopy(envelopes)
#     m = len(a1)
#     n = len(a2)
#     q = [1] * m  # stores longest length ending at index

#     for d in range(m - 2, -1, -1):
#         f = d + 1
#         un = 1
#         gn = a1[d]
#         au = [a1[d]]
#         t = [d]

#         while f < m:
#             if gn[1] < a1[f][1] and gn[0] != a1[f][0]:
#                 gn = a1[f]
#                 au.append(copy.deepcopy(gn))
#                 t.append(f)
#                 un += 1
#             elif gn[1] > a1[f][1] and gn[0] != a1[f][0] and a1[f][1] < a1[d][1]:
#                 s = len(au) - 1
#                 ot = 0
#                 while s > 0:
#                     # Ensure no IndexError
#                     if m - t[s] < len(q) and m - f < len(q):
#                         if q[m - t[s]] < q[m - f] and a1[f][1] < au[s][1]:
#                             if s > 1:
#                                 if a1[f][1] < au[s - 1][1] and q[m - f] > q[m - t[s - 1]]:
#                                     t.pop(s)
#                                     au.pop(s)
#                                     ot = 1
#                                     un -= 1
#                                 elif a1[f][1] > au[s - 1][1]:
#                                     t.pop(s)
#                                     au.pop(s)
#                                     ot = 1
#                                     un -= 1
#                             else:
#                                 t.pop(s)
#                                 au.pop(s)
#                                 ot = 1
#                                 un -= 1
#                     s -= 1

#                 if ot == 1:
#                     au.append(copy.deepcopy(a1[f]))
#                     t.append(f)
#                     un += 1
#                     gn = a1[f]

#             f += 1

#         q[d] = un  # update q with the computed un

#     # Debug print
#     print("Length array q:", q,max(q))
#     return max(q)
# maxEnvelopes(envelopes)



#  def maxEnvelopes(self, envelopes):
#         """
#         :type envelopes: List[List[int]]
#         :rtype: int
#         """
#         r=0
#         ren=[]
#         envelopes.sort()
#         import copy
#         a1=copy.deepcopy(envelopes)
#         l=copy.deepcopy(len(envelopes))
#         a = 0
#         ou=[]
#         while a < l-1:
#             if envelopes[a][0] == envelopes[a+1][0] or envelopes[a][1] == envelopes[a+1][1]:
#                 if envelopes[a][0] == envelopes[a+1][0]:
#                     ou=envelopes[a+1]
#                 envelopes.pop(a+1)
#                 a1.pop(a+1)
#                 l -= 1   
#             else:
#                 envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]
#                 a += 1
#         if a == l - 1:
#             envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]
#         envelopes.sort()
#         if ou!=[]:
#             a1.append(copy.deepcopy(ou))
#         a1.sort()     

#         a2=copy.deepcopy(envelopes)
#         #print(a1)
#         a=0
#         # m=copy.deepcopy(len(a1))
#         # while a < m-1:
#         #         if envelopes[a][0] == envelopes[a+1][0] or envelopes[a][1] == envelopes[a+1][1]:
                
#         #                 envelopes.pop(a+1)
#         #                 a2.pop(a+1)
#         #                 m -= 1   
#         #         else:
#         #                 envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]
#         #                 a += 1
#         # if a == m - 1:
#         #      envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]
#         # envelopes.sort()


#         # print (envelopes)
        
        

#         m=copy.deepcopy(len(a1))
#         n=copy.deepcopy(len(a2))
#         b=0
#         d=0
#         q=[]
#         while d<m:
#             f=d+1
#             un=1
#             gn=a1[d]
#             while f<m:
#                 if gn[1] < a1[f][1] and gn[0]!=a1[f][0]:
                    
#                     un+=1
#                 f+=1    
#             q.append(copy.deepcopy([un]))   
#             d+=1
#         #print(q)    

#         t=[]
#         while b<m:
#                 if b>0 :
#                     if a1[b][1]>ren[r-1][1] and a1[b][0]!=ren[r-1][0]:
#                         ren.append(copy.deepcopy(a1[b]))
#                         t.append(copy.deepcopy(b))
#                         r+=1

#                         print(1,b,r,ren)
                        
#                     elif a1[b][1]<ren[r-1][1]: 
#                             s=b
#                             ot=0
#                             mn=[]
#                             if r>0 :   
#                                 while s>0 and r>0 and len(t)>0 :
#                                     print(r,s,ren)
#                                     if r>0:
#                                             if q[b]>=q[t[r-1]] and a1[b][1]<ren[r-1][1]  :
#                                                 if r>1:
#                                                     if a1[b][1]>ren[r-2][1]:
#                                                         t.pop(r-1)
#                                                         ren.pop(r-1)
#                                                         r-=1 
#                                                         ot=1
#                                                     elif a1[b][1]<ren[r-2][1] and q[b]>q[t[r-2]] :
#                                                             t.pop(r-1)
#                                                             ren.pop(r-1)
#                                                             r-=1 
#                                                             ot=1
#                                                 else:
#                                                         t.pop(r-1)
#                                                         ren.pop(r-1)
#                                                         r-=1 
#                                                         ot=1
#                                 # if  ot==1:
#                                 #      mn.append(copy.deepcopy(t[r-1])) 


#                                     # elif  q[b]>=q[t[r-1]] and a1[b][1]<ren[r-1][1]  :
#                                     #                     t.pop(r-1)
#                                     #                     ren.pop(r-1)
#                                     #                     r-=1 
#                                     #                     ot=1   

#                                     # if r==0:
#                                     #     break                                    
#                                     s-=1    
#                                 if ot==1:
#                                     ren.append(copy.deepcopy(a1[b]))
#                                     t.append(copy.deepcopy(b))
#                                     r+=1
                                                    
#                         #     if a1[b][1]<ren[r-2][1]:
#                         #         ren[r-1]=a1[b]   
#                         #     print(2,b,r,ren)    
#                         # elif a1[b][1]>a1[b+2][1]:     
#                         #     ren[r-1]=a1[b]
#                         #     print(3,b,r,ren)  
                            
#                 else:
#                         ren.append(copy.deepcopy(a1[b]))
#                         t.append(copy.deepcopy(b))
#                         #print(4,b,r,ren) 
#                         r+=1
                                
#                 b+=1
#         return r   

# envelopes =[[21,33],[27,39],[6,29],[45,2],[5,16],[14,15],[31,31],[28,43],[14,13],[44,29],[44,47],[26,1],[40,18],[33,6],[39,40],[39,13],[1,33],[31,4],[21,40],[50,14],[17,44],[21,22],[32,41],[18,28],[29,50],[9,24],[25,26],[32,30],[17,32],[21,2],[17,39]]
# def maxEnvelopes( envelopes):
#     """
#     :type envelopes: List[List[int]]
#     :rtype: int
#     """
#     r=0
#     ren=[]
#     envelopes.sort()
#     print(envelopes)
#     import copy
#     a1=copy.deepcopy(envelopes)
#     l=copy.deepcopy(len(envelopes))
#     a = 0
#     ou=[]
#     # while a < l-1:
#     #     if envelopes[a][0] == envelopes[a+1][0] or envelopes[a][1] == envelopes[a+1][1]:
#     #         if envelopes[a][0] == envelopes[a+1][0]:
#     #              ou=envelopes[a+1]
#     #         envelopes.pop(a+1)
#     #         a1.pop(a+1)
#     #         l -= 1   
#     #     else:
#     #         envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]
#     #         a += 1
#     # if a == l - 1:
#     #     envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]
#     # envelopes.sort()
#     # if ou!=[]:
#     #      a1.append(copy.deepcopy(ou))
#     # a1.sort()     

#     a2=copy.deepcopy(envelopes)
#     #print(a1)
#     a=0
#     # m=copy.deepcopy(len(a1))
#     # while a < m-1:
#     #         if envelopes[a][0] == envelopes[a+1][0] or envelopes[a][1] == envelopes[a+1][1]:
            
#     #                 envelopes.pop(a+1)
#     #                 a2.pop(a+1)
#     #                 m -= 1   
#     #         else:
#     #                 envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]
#     #                 a += 1
#     # if a == m - 1:
#     #      envelopes[a][0], envelopes[a][1] = envelopes[a][1], envelopes[a][0]
#     # envelopes.sort()


#     # print (envelopes)
    
    

#     m=copy.deepcopy(len(a1))
#     n=copy.deepcopy(len(a2))
#     b=0
#     d=m-2
#     q=[1]

#     while d>-1:
#          f=d+1
#          un=1
#          gn=a1[d]
#          print(d,gn)
#          au=[a1[d]]
#          t=[d]
#          while f<m:
#                 print(a1[f],gn,f)
#                 if gn[1] < a1[f][1] and gn[0]!=a1[f][0]:
                    
#                     gn=a1[f]
                    
#                     au.append(copy.deepcopy(gn)) 
#                     t.append(copy.deepcopy(f))
#                     un+=1
#                     print(1,un,au,f)
#                 elif gn[1] > a1[f][1] and  a1[f][1] > a1[d][1] :
#                     s=len(au)-1
#                     ot=0
#                     mn=0
                    
    
#                     while s>0:
#                                 if q[m-t[s]-1]<q[m-f-1] and a1[f][1]<au[s][1]:
                                    
#                                     if s>1:
#                                         if a1[f][1]<au[s-1][1] :
#                                              mn+=1 
                                                
#                                              print(q[m-t[s-1]-1],q[m-f],au,t,m-t[s-1]-1,m-f)
                                               
#                                         elif  a1[f][1]>au[s-1][1] :
#                                                 t.pop(s)
#                                                 au.pop(s)
                                                    
#                                                 ot=1  
#                                                 un-=1             
#                                 s-=1  
#                     lo=len(au)                 
#                     if ot==1:
#                                 for i in range(mn):
#                                       au.pop(lo-1-i)
#                                       t.pop(lo-1-i)
#                                       un-=1
#                                 au.append(copy.deepcopy(a1[f]))
#                                 t.append(copy.deepcopy(f))
#                                 un+=1 
#                                 print(2,un,au,f)    
#                                 gn=a1[f]
#                 f+=1    
#          q.append(copy.deepcopy(un))  
#          un=1
#          print(d)
#          d-=1
         
        
    
#     print(q,a1)
#     print( max(q))
    

#     # t=[]
#     # while b<m:
#     #         if b>0 :
#     #             if a1[b][1]>ren[r-1][1] and a1[b][0]!=ren[r-1][0]:
#     #                 ren.append(copy.deepcopy(a1[b]))
#     #                 t.append(copy.deepcopy(b))
#     #                 r+=1

#     #                 print(1,b,r,ren)
                    
#     #             elif a1[b][1]<ren[r-1][1]: 
#     #                     s=b
#     #                     ot=0
#     #                     mn=[]
#     #                     if r>0 :   
#     #                         while s>0 and r>0 and len(t)>0 :
#     #                             print(r,s,ren)
#     #                             if r>0:
#     #                                     if q[b]>=q[t[r-1]] and a1[b][1]<ren[r-1][1]  :
#     #                                         if r>1:
#     #                                             if a1[b][1]>ren[r-2][1]:
#     #                                                 t.pop(r-1)
#     #                                                 ren.pop(r-1)
#     #                                                 r-=1 
#     #                                                 ot=1
#     #                                             elif a1[b][1]<ren[r-2][1] and q[b]>q[t[r-2]] :
#     #                                                     t.pop(r-1)
#     #                                                     ren.pop(r-1)
#     #                                                     r-=1 
#     #                                                     ot=1
#     #                                         else:
#     #                                                 t.pop(r-1)
#     #                                                 ren.pop(r-1)
#     #                                                 r-=1 
#     #                                                 ot=1
#     #                         # if  ot==1:
#     #                         #      mn.append(copy.deepcopy(t[r-1])) 


#     #                             # elif  q[b]>=q[t[r-1]] and a1[b][1]<ren[r-1][1]  :
#     #                             #                     t.pop(r-1)
#     #                             #                     ren.pop(r-1)
#     #                             #                     r-=1 
#     #                             #                     ot=1   

#     #                             # if r==0:
#     #                             #     break                                    
#     #                             s-=1    
#     #                         if ot==1:
#     #                             ren.append(copy.deepcopy(a1[b]))
#     #                             t.append(copy.deepcopy(b))
#     #                             r+=1
                                                
#     #                 #     if a1[b][1]<ren[r-2][1]:
#     #                 #         ren[r-1]=a1[b]   
#     #                 #     print(2,b,r,ren)    
#     #                 # elif a1[b][1]>a1[b+2][1]:     
#     #                 #     ren[r-1]=a1[b]
#     #                 #     print(3,b,r,ren)  
                        
#     #         else:
#     #                 ren.append(copy.deepcopy(a1[b]))
#     #                 t.append(copy.deepcopy(b))
#     #                 #print(4,b,r,ren) 
#     #                 r+=1
                            
#     #         b+=1
#     # print(r,ren,a1,q,t)     
 

# maxEnvelopes(envelopes)
# for i in range(0,len(nums)-1):
#         if len(nums)-i>indexDiff:
#               t= indexDiff+1
#         elif len(nums)-i>0  :
#               t= len(nums)-i
      
#         for j in range(t-1,1,-1):
            
#             if nums[i]-nums[i+j]>-1 and nums[i]-nums[i+j]<=valueDiff  :   
                
#                 return True
#             elif valueDiff>=nums[i+j]-nums[i] and nums[i+j]-nums[i]>-1 :
#                 return True   
#     return False
b=-3
print(abs(b))
si
print(b)
print(type(b))