def tribonacci(signature, n):
    # if less than 1, return a blank list
    if n < 1:
        return []
    # if `n` is less than the signature,
    # return a list at the item's place
    if n < len(signature):
        return signature[0:n]

    # counter
    inc = 0

    # copy the signature list as a starting point
    seq = signature[:]

    # increment
    while inc <= n:
        # add up the last 3 items
        add = sum(seq[inc:inc + 3])
        # add to the new list
        seq.append(add)
        # next!
        inc += 1

    # return the new list,
    # forcing to only the max size wanted
    return seq[0:n]


def trib(signature, n):

    if n == 2:
        return 1
    elif n < 2:
        return 0
    else:
        return trib(n - 1) + trib(n - 2) + trib(n - 3)
