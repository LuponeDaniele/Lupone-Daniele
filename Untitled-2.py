#trova il maggiore tra i tra i 4  numeri dati


def maggiore(a,b,c,d):
    if a>b:
        if a>c:
            if a>d:
                max=a
    elif c>d:
            if c>a:
                if c>b:
                    max=c
    elif b>a:
        if b>c:
            if b>d:
                max=b
    elif d>a:
        if d>b:
            if d>c:
                max=d

return max 

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))
d = float(input("inserisci d: "))
