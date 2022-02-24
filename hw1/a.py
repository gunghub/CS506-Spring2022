def func(a):
    sum=0;
    for y in [2.0,1.0,5.0,3.0,2.0,4.0,1.0,4.0,6.0,4.0,2.0, 6.0]:
        sum=sum+(a-y)**2
    return sum/12


# for a in [1,2,3,4,5,6]:
#     print(func(a))


print(func(10/3))

# sum=0;
# for y in [2.0,1.0,5.0,3.0,2.0,4.0,1.0,4.0,6.0,4.0,2.0, 6.0]:
#     sum=sum+y
#
# print(sum/12)