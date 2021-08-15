import requests
d={}

def cache(inp1,inp2,inp3):
    print("Sorry, but it is not in the cache!")
    r = requests.get(f"http://www.floatrates.com/daily/{inp1}.json")
    rate=r.json()[inp2]['rate']
    d[inp1+inp2]=rate
    print(f"You received {round(rate*inp3,2)} {inp2.upper()}.")


def acachepr(inp1,inp2,inp3):
    print("Oh! It is in the cache!")
    rate=d[inp1+inp2]
    print(f"You received {round(rate*inp3,2)} {inp2.upper()}.")


def menu(inp1):
    inp2=input().lower()

    if(inp2==''):
        return 0
    inp3=float(input())

    print("Checking the cache...")

    if (inp1+inp2 in d):
        acachepr(inp1,inp2,inp3)
    else:
        cache(inp1,inp2,inp3)
    return 1




inp1=input().lower();a=1
r = requests.get(f"http://www.floatrates.com/daily/{inp1}.json")

if(inp1!='usd'):
    d[inp1+'usd'] = float(r.json()['usd']['rate'])
if(inp1!='eur'):
    d[inp1+'eur'] = float(r.json()['eur']['rate'])

while(menu(inp1)):
    pass