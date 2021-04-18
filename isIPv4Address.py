def isIPv4Address(s):
    p = s.split('.')
    for n in p:
        if len(n)>1 and n[0]=='0':
            return False
    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p) 


s1="01.233.161.131"     #false
s2="64.00.161.131"      #false
s3="1.23.256.."         #false
s4="0.254.255.0"        #true
s5="64.233.161.00"      #false


print(isIPv4Address(s1))
print(isIPv4Address(s2))
print(isIPv4Address(s3))
print(isIPv4Address(s4))
print(isIPv4Address(s5))
    

