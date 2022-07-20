# This script generate fibobacci sequence.
# Logic: add last two number and print till the limit mentioned in the script.
n0 = 0
n1 = 1
nf = 0
limit = 10
l1 = []

for i in range(limit):
    nf = n0 + n1 
    #print(n0)
    l1.append(n0)
    n0 = n1
    n1 = nf

print(l1)