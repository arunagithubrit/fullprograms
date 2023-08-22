# *
# * *
# * * *
# * * * *
# * * * * *



# for row in range(1,5):
#     for col in range(row):
#         print("*",end="")
#     print()



# 1
# 12
# 123
# 1234

# for row in range(1,8):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()


# * * * *
# * * *
# * *
# *

# for row in range(1,5):
#     for col in range(5,row,-1):
#         print("*",end=" ")
#     print()


# for row in range(4,0,-1):
#     for col in range(row):
#         print("*",end=" ")
#     print()



# for row in range(1,5):
#     for col in range(1,8):
#         if (row==4) or (row+col==5) or (col-row==3):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()




for row in range(1,5):
    for col in range(1,8):
        if (row==1) or (row==col) or (row+col==8):
            print("*",end="")
        else:
            print(end=" ")
    print()


