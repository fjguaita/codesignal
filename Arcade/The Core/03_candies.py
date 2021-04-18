# 'n' niños tienen 'm' caramelos. Quieren comer tantos dulces como puedan, 
# pero cada niño debe comer exactamente la misma cantidad de dulces que cualquier otro niño. 
# Determine cuántos dulces se comerán todos los niños juntos. Los dulces individuales no se pueden dividir.

def candies(n, m):
    return n*(m//n)


def candies2(n, m):
    return m - m % n