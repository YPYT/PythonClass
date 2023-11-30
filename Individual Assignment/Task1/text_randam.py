import random
f= open("JPN.txt", 'w')
for count in range(100):
    patrol = random.uniform(7.0,8.0)
    gas = random.uniform(2.0,3.0)
    diesel = random.uniform(3.0,4.0)
    f.write('{:.2f}'.format(patrol)+" ")
    f.write('{:.2f}'.format(gas)+" ")
    f.write('{:.2f}'.format(diesel)+" "+"\n")
f.close()