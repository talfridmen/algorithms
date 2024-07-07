def prime_factors(num):
#    pass # Implement Here!
    factors=[]
    pf=2

    while num > 1:
       if num%pf == 0:
         factors.append(pf)
         num = num//pf
       else:
         pf+=1

    return factors

