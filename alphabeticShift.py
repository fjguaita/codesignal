def alphabeticShift(s):
    return "".join([chr(ord(i)+1) if ord(i) <122 else 'a' for i in s])


def alphabeticShift2(s):
    return "".join(chr((ord(i)-96)%26+97) for i in s)


def alphabeticShift3(s):
    return ''.join((chr(ord(i)+1) if i!="z" else "a" for i in s))