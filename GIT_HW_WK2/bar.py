import numpy as np

l_nums =  np.arange(100)

for i in l_nums:
    if i % 2 == 0:
        print('FOO')
    elif i % 3 ==0:
        print('Woohoo!')
    else:
        print(i)
