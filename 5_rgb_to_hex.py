def rgb(r, g, b):
    if r < 0: r = 0
    if g < 0: g = 0
    if b < 0: b = 0
    if r > 255: r = 255
    if g > 255: g = 255
    if b > 255: b = 255
    x = '#%02x%02x%02x' % (r, g, b)
    result = str(x).upper().replace('#', '')
    return result


print(rgb(0, 0, 0))  # ,"000000)
print(rgb(1, 2, 3))  # ,"010203"
print(rgb(255, 255, 255))  # , "FFFFFF"
