a = [str(x) for x in range(2)]

print(', '.join(a))

def test(a='1', *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

test('1', '15', b='33')

for x in range(len(a)):
    a[x] = f''
    print(a[x])

print(a)
