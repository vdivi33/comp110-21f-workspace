def spooky()-> None:
    b: dict[int, int] = {0: 1}
    o: dict [int, int] = b

    b = sz(b)

    print(b[0] + o[0])

def sz(n: dict [int, int]) -> dict[int, int]:
    b: dict[int, int] = n
    print(b)
    n = {0: 3}
    b[0] = 2
    return n

spooky()