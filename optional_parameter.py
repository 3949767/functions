


def optional_parameter(x, y, z = None, flag = False): # None makes a parameter be optional
    if(flag):
        print('Flag is True!!!')
    else:
        print('Flag is False!!!')


    if (z == None):
        return x + y
    else:
        return x + y + z

print(optional_parameter(2, 4))
print(optional_parameter(2, 4, 6))






