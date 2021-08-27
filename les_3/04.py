x = 4
y = -6


def variant2(xy, yx):
    c = -1
    b = xy/xy
    while c >= yx:
        b = b/xy
        c = c-1
    return b


print(f"если возвести {x} в степень {y}, получится {variant2(x, y)}")
