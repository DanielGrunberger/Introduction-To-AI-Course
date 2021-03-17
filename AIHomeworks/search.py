#search
from AIHomeworks import frontier, state


def search(n):
    s= state.create(n)
    print(s)
    f= frontier.create(s)
    while not frontier.is_empty(f):
        s= frontier.remove(f)
        if state.is_target(s):
            return [s, f[1], f[3]]
        ns= state.get_next(s)
        for i in ns:
            frontier.insert(f, i)
    return 0


average_depth = 0
average_items = 0
for i in range(100):
     current = search(4)
     average_depth += current[2]
     average_items += current[1]
print("-------------For search(4):-------------\n")
print(f"Average depth: {str(average_depth/100)}\nAverage items: {str(average_items/100)}")






