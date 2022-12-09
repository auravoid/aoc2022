input = open('input.txt').read().strip().splitlines()

h = len(input)
w = len(input[0])
vis = set()
scr = 0

for y in range(h):
    for x in range(w):
        score = 1
        tree = input[y][x]
        l = input[y][:x][::-1]
        r = input[y][x+1:w]
        u = [input[ny][x] for ny in reversed(range(y))]
        d = [input[ny][x] for ny in range(y+1,h)]
        
        for direction in l, d, u, r:
            for i, neighbour in enumerate(direction):
                if tree <= neighbour:
                    score *= i+1; break
            else:
                score *= len(direction) if direction else 1
                vis.add((y,x))
        scr = max(scr, score)

print(len(vis))
print(scr)