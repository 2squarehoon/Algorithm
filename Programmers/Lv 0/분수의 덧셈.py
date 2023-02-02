def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(numer1, denom1, numer2, denom2):
    n = gcd(denom1, denom2)
    lcm = denom1*denom2/n
    x = numer1*lcm/denom1+numer2*lcm/denom2
    y = gcd(x, lcm)
    answer = [x/y, lcm/y]
    return answer