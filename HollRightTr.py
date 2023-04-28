N = int(input())
if N == 1:
    print("#")
else:
    print("# " * N)
    for i in range(2,N):
        spaces = "  " * (N-1-i)
        add = "+ " + spaces + "+ "
        print(add)
    print("+ ")

'''
4


# # # # 
+   + 
+ + 
+ 

'''

    
