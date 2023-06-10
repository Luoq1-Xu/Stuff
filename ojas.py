def foo(s):
    if s:
        s[0], s[-1] = s[-1], s[0]
        return foo(s[1:-1])
    else:
        return s

print((list('banana')))