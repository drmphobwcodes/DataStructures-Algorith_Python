# This is a python code that finds Pythagorean triplets under an upper limit n.
# It uses two nsted loops to iterate through all possible values
# of a and b, and then it checks if c is a whole number and if a, b, and c
# add up to a number less than or equal to n. If it is, it appends the triplet (a, b, c)
# to the triplets list and returns the list at the end.

def find_triplets(n):
    # where n is the upper limit n
    triplets = []
    for a in range(1, n):
        for b in range(a, n):
            c = (a ** 2 + b ** 2) ** 0.5
            if c.is_integer() and a + b + c <= n:
                triplets.append((a, b, int(c)))
    return triplets


print(find_triplets(20))
