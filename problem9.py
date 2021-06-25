def pythagorean_triplet():
    for a in range(1000):
        for b in range(a + 1, 1000 - a):
            for c in range(b + 1, 1000 - b):
                if a + b + c == 1000 and a * a + b * b == c * c:
                    return a * b * c


print(pythagorean_triplet())
