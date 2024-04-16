def SubtractCubes(a, b):
    return ((((a-b)**2)+(2*((a-b)*b)))*a)+(b**2)*(a-b)

Error,Correct =0,0
for i in range(-100,100):
    for j in range(-100,100):
        try:
            assert SubtractCubes(i,j) == (i**3)-(j**3)
        except AssertionError:Error = Error + 1
        else: Correct = Correct + 1

try:
    print ((Error+Correct)/Error)
except ZeroDivisionError:print("success")