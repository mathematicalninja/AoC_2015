def getFirstSpace(s: str) -> int:
    # returns the index of the space itself.
    # e.g. "Hello world!" -> 5
    return s.find(" ")


def getNextSpace(s: str, start: int | None) -> int:
    if start is None:
        start = 0
    f = s[start:].find(" ")
    if f == -1:
        return -1
    return f + start


def getNthSpace(s: str, n: int) -> int:
    if n == 0:
        return -1

    firstSpace = s.find(" ")
    if firstSpace == -1 or n == 1:
        return firstSpace

    idx = firstSpace
    for i in range(1, n):
        idx = getNextSpace(s, idx + 1)
    return idx
