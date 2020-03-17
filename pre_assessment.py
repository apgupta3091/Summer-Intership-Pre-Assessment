#Anuj Gupta

#from pprint import pprint
​
def get_results(s1, s2):
    d= {}
    e= {}
    f=[]
    g=[]
    if len(s1) != len(s2):
        return False
    elif len(s1) == len(s2):
        for i in s1:
            if i in d:
                d[i] += 1
            else:
                d[i]= 1
        #pprint(d)
        for key in d:
            if d[key]>0:
                f.append(d[key])
        for i in s2:
            if i in e:
                e[i] += 1
            else:
                e[i]= 1
        #pprint(e)
        for key in e:
            if e[key]>0:
                g.append(e[key])
        #pprint(f)
        #pprint(g)
    return (len(f) >= len(g))
​
if __name__ == "__main__":
    s1 = input ("Enter a string: ")
    s2 = input ("Enter a second string: ")
    result = get_results(s1, s2)
    print(result)
