# while loops, you need a watch out, or they last forever!
# keep_going = True
# n = 1
# while keep_going:
#     print("This is a number" + str(n))
#     n += 1
#     if n > 1000:
#         keep_going = False
#
# print("Finished")



# Break takes us out of your current loop and back into the last bassline
# n = 1
# while n <= 1000:
#     print("this is an attempt number" + str(n))
#     n += 1
# print ("finished")
#
#
# n = 1
# while n <= 1000:
#     print(f"this is an attempt number {n}" )
#     n += 1
#     if n == 500:
#         print("500 is my fave number!")
# print ("finished")

accept = False
while not accept:
    num = input("Please enter number\n")
    if num.isdigit():
        accept = True
    else:
        print("that's not a number")
print(f"You picked the number {num}")