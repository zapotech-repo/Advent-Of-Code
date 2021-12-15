inputs=[int(x) for x in open("2021/01/1/in.txt").read().splitlines()]
ip=[sum(inputs[x:x+3]) for x in range(len(inputs))]
a=0
for x in range(1, len(ip)):
    if ip[x]>ip[x-1]:
        a+=1
print(a)