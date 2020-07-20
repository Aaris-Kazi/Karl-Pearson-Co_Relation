import pandas as pd
from math import sqrt

def average(x):
    temp = 0
    count = 0
    for i in x:
        i = int(i)
        temp = temp + i
        count = count + 1
    temp = temp / count
    return temp

def summation(x):
    temp = 0
    for i in x:
        temp = temp + i
    
    return temp 

def minus(z, z_bar):
    min_z = []
    for i in z:
        i = int(i)
        i = i - z_bar
        min_z.append(i)
    return min_z

def squaring(new_min):
    sq_z = []
    for i in new_min:
        i = float(i)
        i = i * i
        sq_z.append(i)
    return sq_z

def mul(x_bar, y_bar):
    result = []
    temp = 0
    for i in range(0,4):
        temp = x_bar[i] * y_bar[i]
        result.append(temp)
    return result


x = [67,54,34,4]
y = [88,76,5,9]
d = {"X": x,"Y": y}
df = pd.DataFrame(d)

x_bar = average(x)
y_bar = average(y)

minus_x = minus(x,x_bar)
minus_y = minus(y,y_bar)

df['X - X'] = minus_x
df['Y - Y'] = minus_y

result = mul(minus_x,minus_y)
df['(X - X)*(Y - Y)'] = result

sq_x = squaring(minus_x)
df['(X - X)*2'] = sq_x
sq_y = squaring(minus_y)
df['(Y - Y)*2'] = sq_y

print(df)
mul_sum = summation(result)
sum_xx = summation(sq_x)
sum_yy = summation(sq_y)

print("SUM X BAR ",x_bar) 
print("SUM Y BAR ",y_bar)
print("E(X - X)*(Y - Y) ",mul_sum)
print("E(X - X)*2 ",sum_xx)
print("E(Y - Y)*2 ",sum_yy)

final = sum_xx * sum_yy
final = sqrt(final)
final = mul_sum / final
print(final)