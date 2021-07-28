#search
import state
import frontier

# n is size of board
def search(n):
    s=state.create(n)
    print("Initial state is :")
    print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            print("Solution found !")
            return [s, f[1], f[3]]
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return 0


print (search(3))


