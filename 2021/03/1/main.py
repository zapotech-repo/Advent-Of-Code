ins=open("2021/03/1/in.txt").read().splitlines()
z=[0 for x in range(len(ins[0]))]
o=[0 for x in range(len(ins[0]))]
for x in ins:
    for a in range(len(x)):
        [z,o][int(x[a])][a]+=1
g="0b"
e="0b"
for x in range(len(z)):
    if z[x]>o[x]:
        g+="0"
        e+="1"
    else:
        g+="1"
        e+="0"
gr=int(g,2)
er=int(e,2)
print(gr*er)