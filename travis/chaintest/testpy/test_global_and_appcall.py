OntCversion = '2.0.0'
from ontology.libont import str, hex
from ontology.interop.System.App import RegisterAppCall, DynamicAppCall
from ontology.libont import elt_in, hexstring2bytes, bytearray_reverse


# Test
a = 12345678987654321
s_a = str(a)
assert(s_a == '12345678987654321')

a = 9797589374729374982374981794371294719827439827491793749173491784712
s_a = str(a)
assert(s_a == '9797589374729374982374981794371294719827439827491793749173491784712')

a = 1378937591759175934898096347592347591789571970179179010971947
s_a = str(a)
assert(s_a == '1378937591759175934898096347592347591789571970179179010971947')

a = 13789375917591759348980963475923475917895719701791790109719477
s_a = str(a)
assert(s_a == '13789375917591759348980963475923475917895719701791790109719477')

a = 137893759175917593489809634759234759178957197017917901097194777
s_a = str(a)
assert(s_a == '137893759175917593489809634759234759178957197017917901097194777')

a = 1378937591759175934898096347592347591789571970179179010971947777
s_a = str(a)
assert(s_a == '1378937591759175934898096347592347591789571970179179010971947777')

a = 13789375917591759348980963475923475917895719701791790109719477777
s_a = str(a)
assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777')

a = 137893759175917593489809634759234759178957197017917901097194777777
s_a = str(a)
assert(s_a == '137893759175917593489809634759234759178957197017917901097194777777')

a = 1378937591759175934898096347592347591789571970179179010971947777777
s_a = str(a)
assert(s_a == '1378937591759175934898096347592347591789571970179179010971947777777')

a = 13789375917591759348980963475923475917895719701791790109719477777777
s_a = str(a)
assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777777')

a = 137893759175917593489809634759234759178957197017917901097194777777777
s_a = str(a)
assert(s_a == '137893759175917593489809634759234759178957197017917901097194777777777')

a = 1378937591759175934898096347592347591789571970179179010971947777777777
s_a = str(a)
assert(s_a == '1378937591759175934898096347592347591789571970179179010971947777777777')

a = 13789375917591759348980963475923475917895719701791790109719477777777777
s_a = str(a)
assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777777777')

a = 13789375917591759348980963475923475917895719701791790109719477777777777777
s_a = str(a)
assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777777777777')

a = 137893759175917593489809634759234759178957197017917901097194777777777777777
s_a = str(a)
assert(s_a == '137893759175917593489809634759234759178957197017917901097194777777777777777')

a = 1378937591759175934898096347592347591789571970179179010971947777777777777777
s_a = str(a)
assert(s_a == '1378937591759175934898096347592347591789571970179179010971947777777777777777')

a = 13789375917591759348980963475923475917895719701791790109719477777777777777777
s_a = str(a)
assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777777777777777')

a = 0x123456789abcdef
s_a = hex(a)
assert(s_a == '0x123456789abcdef')

a = 0x1234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef
s_a = hex(a)
assert(s_a == '0x1234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef')
NAME = "AppCall000"

x0 = 6
y0 = [9, 8, 7, 6]
a0 = ["wo", 2, 3, 4, 5]
z0 = {a0[1]: 'hello', a0[2]: 'world', a0[3]: x0, a0[4]: y0}
# map in map
b0 = {a0[1]: 'hello', a0[2]: 'world', a0[3]: x0, a0[4]: y0, a0[0]: z0}

a = makedict()
b = {i: j for i in range(1, 5) for j in range(5, 8)}
CalculatorContract = RegisterAppCall('a6b20575537f0b3ce1dceb1f99207db4ec8ce88c', 'operation', 'args')
x = 20

q = 0
if x0 in y0:
    for i in y0:
        q += 1
        if i == 9:
            continue
        elif i == 7:
            break
else:
    assert(False)

assert(q == 3)

if x0 > 2 and y0[3] < y0[0] or y0[1] < 2:
    pass
else:
    assert(False)


def Main(operation, args):
    global z0
    z0 = 999
    b0[a0[4]][0] = 30
    b0[a0[0]][a0[4]][1] = 20

    x = 'local'
    assert(b[1] == 7)
    assert(b[2] == 7)
    assert(b[3] == 7)
    assert(b[4] == 7)
    b[1] = 90
    global a
    a[0][0] = '00'
    assert(x == 'local')

    checkglobal()
    assert(b[1] == 'checkglobal')
    assert(a == 9)
    print(a)
    print(b[1])
    assert(b0 == 8888)
    assert(y0[2] == 88)

    if elt_in(['add', 'sub', 'mul'], operation):
        print("StaticAppCall")
        return CalculatorContract(operation, args)
    elif operation[0:1] == 'd':
        address = bytearray_reverse(hexstring2bytes('a6b20575537f0b3ce1dceb1f99207db4ec8ce88c'))
        print("DynamicAppCall")
        operation = operation[1:]
        print(operation)
        return DynamicAppCall(address, operation, args)
    elif operation == 'name':
        print("getname")
        return NAME
    elif operation == "testcase":
        return testcase()

def testcase():
    return '''
    [
        [{"needcontext":false,"env":{"witness":[]}, "method":"add", "param":"[int:111,int:222]", "expected":"int:333"},
         {"needcontext":false,"env":{"witness":[]}, "method":"sub", "param":"[int:411,int:111]", "expected":"int:300"},
         {"needcontext":false,"env":{"witness":[]}, "method":"mul", "param":"[int:2,int:3]", "expected":"int:6"},
         {"needcontext":false,"env":{"witness":[]}, "method":"dadd", "param":"[int:2,int:3]", "expected":"int:5"},
         {"needcontext":false,"env":{"witness":[]}, "method":"dsub", "param":"[int:3,int:2]", "expected":"int:1"},
         {"needcontext":false,"env":{"witness":[]}, "method":"dmul", "param":"[int:3,int:8]", "expected":"int:24"}
        ]
    ]'''


def makedict():
    return {0: makedict2(), 1: 'middle', 2: makedict3()}


def makedict2():
    return {0: arg0(), 1: arg1(), 2: arg2()}


def makedict3():
    return {0: arg2(), 1: arg1(), 2: arg0()}


def arg0():
    return '0'


def arg1():
    return '1'


def arg2():
    return '2'


def checkglobal():
    global a, b0
    assert(b[1] == 90)
    assert(a[0][0] == '00')
    assert(a[1] == 'middle')
    assert(a[2][0] == '2')
    assert(a[2][1] == '1')
    assert(a[2][2] == '0')
    assert(s_a == '0x1234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef')
    b[1] = 'checkglobal'
    a = 9
    assert(z0 == 999)
    assert(y0[0] == 30)
    assert(y0[1] == 20)
    b0[a0[0]][a0[4]][2] = 88
    b0 = 8888
    print(y0[0])
