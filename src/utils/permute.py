def permuteIndices_all(n: int) -> list[list[int]]:
    if n <= 0:
        return [[0]]
    # note this is 0 ==> n-1, dealing with n later
    oldPerms = [[0]]
    for i in range(1, n - 1):
        newPerms: list[list[int]] = []
        for perm in oldPerms:
            newPerms += insertM(perm, i)
        oldPerms = newPerms

    # dealing with n
    newPerms = []
    for perm in oldPerms:
        newPerms += insertAfter(1, n - 1, perm)
    return newPerms


def insertM(perm: list[int], m: int) -> list[list[int]]:
    r: list[list[int]] = []
    for i in range(len(perm) + 1):  # +1 allows appending to the perm
        left = perm[i:]
        right = perm[:i]
        r.append(left + [m] + right)
    return r


def insertAfter(a: int, b: int, perm: list[int]) -> list[list[int]]:
    """
    @param a: number to be inserted after
    @param b: number to be inserted
    """
    idxA = perm.index(a)  # ValueError here if a is poorly defined.
    uptoA = perm[: idxA + 1]
    afterA = perm[idxA + 1 :]
    all = insertM(afterA, b)
    r: list[list[int]] = []

    for perm in all:
        r.append(uptoA + perm)
    return r
