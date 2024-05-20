height = int(input())


for n in range(1, height+1):
    i = 0
    num_stars = 2*n - 1
    stars = "*" * num_stars
    size = height * 2 -1
    print(stars.center(size))
