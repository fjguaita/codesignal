def longestCommonSubstring(s, t):
    aux=[]
    if not s or not t:
        return 0
    if len(t)<len(s):
        s, t = t, s
    i=0
    while i < len(s):
        
        if s[i] not in t:
            i+=1
            continue
        l=1
        while (i+l)<=len(s) and s[i:i+l] in t:
            l+=1

        i+=l-1
        aux.append(l-1)
           
    return max(aux) if len(aux)!=0 else 0

# error de limite de tiempo en los ultimos 3


s= "CHZVFRKMLNOZJK"
t= "PQPXRJXKITZYXRKMLNOCQCOENDTOMFGDWDWFCGPXIQVKUYTDLCGDEWHTACIOHORDTQKVWCSGSPQOQMSBOAGUWN"

s= "HMQUDWGHHLGASCAVGGYTKYSWIDVISLCCZSWFQEMA"
t= "QUAIZAFFGDZSDTQNWLVRZXTY"


print(longestCommonSubstring(s, t))


def longestCommonSubstring(s, t):
    
    limit = 500000000023
    prime_base = 101
    
    # Append dummy element in front so we can ignore first hash.
    # It makes the loops cleaner and adds insignificant computation.
    s = [0] + [ord(i) - 31 for i in s]
    t = [0] + [ord(i) - 31 for i in t]
    
    # Build global list of powers of base and initial hashes of s and t so they
    # don't need to be recomputed for each hasSubstringOfLength call.
    powers_of_base = [1]
    s_init_hashes = [0]
    t_init_hashes = [0]
    
    def hasSubstringOfLength(n):
        """Return True if a substring of s with length n also appears in t.
        Uses a rolling hash to compute unique (with high probability) hashes for each
        substring of s with length n, then does the same for t, stopping if any hash
        from t was seen in s.
        """
        # Extend global lists as needed
        for i in range(len(powers_of_base), n):
            powers_of_base.append(powers_of_base[-1] * prime_base % limit)
            s_init_hashes.append((s_init_hashes[-1] * prime_base + s[i]) % limit)
            t_init_hashes.append((t_init_hashes[-1] * prime_base + t[i]) % limit)

        s_hashes = []  # set()
        
        # Initial s hash
        cur_hash = s_init_hashes[n - 1]
        # The rest of the s hashes
        for i in range(n, len(s)):
            cur_hash = ((cur_hash - s[i - n] * powers_of_base[n - 1]) * prime_base + s[i]) % limit
            s_hashes.append(cur_hash) # add(cur_hash)
        s_hashes = set(s_hashes)

        # Initial t hash
        cur_hash = t_init_hashes[n - 1]
        # The rest of the t hashes
        for i in range(n, len(t)):
            cur_hash = ((cur_hash - t[i - n] * powers_of_base[n - 1]) * prime_base + t[i]) % limit
            if cur_hash in s_hashes:
                return True

        return False
    
    # Binary search for length of longest substring
    lo, hi = 0, min(len(s), len(t))
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if hasSubstringOfLength(mid):
            lo = mid
        else:
            hi = mid - 1
            
    return lo