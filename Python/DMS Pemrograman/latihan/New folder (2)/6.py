def geser(key, p):
    key_res = ''
    for i in key:
        key_res += chr(ord(i) + p)
    return(key_res)

p = int(input())
key = input()