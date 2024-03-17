
def Alice(n,g):
    a=5
    x = (g**a)%n
    return (x,a)

def Bob(n,g):
    b=9
    y = (g**b)%n
    return (y,b)

def key_check(k_a, k_b):
    if k_a==k_b:
        print(F"{k_a}, {k_b} : key matched")
    else:
        print(F"{k_a}, {k_b} : key does not matched")

def main():
    n=3
    g=7
    x,a=Alice(n,g)
    y,b=Bob(n,g)
    
    k_a = (y**a) % n
    k_b = (x**b) % n
    
    key_check(k_a, k_b)
    
    
main()
     
    