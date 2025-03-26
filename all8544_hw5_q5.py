from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


def permutations(lst):
    result = []
    stack = []
    queue = []

    for item in lst:
        stack.append(item)

    while stack:
        elem = stack.pop()
        if not queue:
            queue.append([elem])
        else:
            for i in range(len(queue)):
                perm = queue.pop(0)
                for j in range(len(perm) + 1):
                    queue.append(perm[:j] + [elem] + perm[j:])

    while queue:
        result.append(queue.pop(0))

    return result
