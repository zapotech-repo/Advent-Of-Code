inputs=[int(x) for x in open("2021/01/1/in.txt").read().splitlines()]
a=0
for x in range(1, len(inputs)):
    if inputs[x]>inputs[x-1]:
        a+=1
print(a)