def reverseInParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            return reverseInParentheses(s[:start] + s[start+1:i][::-1] + s[i+1:])
    return s



s= "foo(bar)baz(blim)"

print(s[:3])
print(s[3+1:7])                        #   s[3+1:7] = bar  ->  lo que está entre ()
print(s[3+1:7][::-1])                  #   cuando agrego [::-1]  lo doy vuelta     ->      rab

#Expected Output:   "foorabbazmilb"

print(reverseInParentheses(s))