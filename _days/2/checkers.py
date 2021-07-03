WHITE, BLACK = ' ', '#'
size = 8

def checkers(size=8):
    for x in range(size // 2):
        print(f"{WHITE}{BLACK}" * (size // 2))
        print(f"{BLACK}{WHITE}" * (size // 2))

if __name__ == "__main__":
    checkers(size = 4)
