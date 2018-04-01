import random

def typoglycemia(a):
    s = ''
    for i in a.split():
        if len(i) <= 4:
            s += i + ' '
        else:
            l = list(i[1:len(i)-1])
            random.shuffle(l)
            s += i[0] + ''.join(l) + i[-1] + ' '
    return s[:len(s)-1]
    
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(s)) 
# I cn'odlut bilevee that I cuold autcally untendarsd what I was rndiaeg : the pnomneeahl peowr of the hmaun mind .
# I c'nudolt bevilee that I could atlculay uradtsennd what I was radieng : the peanenhoml pwoer of the human mind .
