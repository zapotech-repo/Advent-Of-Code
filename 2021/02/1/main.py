inp=[x.split() for x in open("2021/02/1/in.txt").read().splitlines()]
h=0
d=0
for c,v in inp:
    if c=="forward":
        h+=int(v)
    elif c=="down":
        d+=int(v)
    elif c=="up":
        d-=int(v)
print(h*d)