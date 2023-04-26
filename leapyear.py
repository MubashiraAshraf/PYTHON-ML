# # a = int(input('enter the year:'))
# # if a%4 == 0 and a%100 != 0 or a%400 ==0:
# #     print('it is a leap year')
# # else:
# #     print('it is not a leap year')
#
#
# a = int(input('enter the year:'))
# if a%4 == 0:
#     if a%100 == 0:
#         if a%400 == 0:
#             print('leap year')
#         else:
#             print('not leap year')
#     else:
#         print('leap year')
# else:
#     print('not leap year')


a = int(input('enter the year:'))
if a%4 == 0 and a%100 !=0 :
    print('leap year')
elif a%400 == 0:
    print ('leap year')
else:
    print('not leap year')