# Family of 3 problem
# In a family with three children, what is the probability that, if at least one of the children is a girl, all are girls?
import random
import sys

def random_child():
    return random.random()


if __name__ == "__main__":
    for i in range(0, int(sys.argv[1])):
        child1 = random_child()
        child2 = random_child()
        child3 = random_child()
        # print(f"Child 1: {child1}, Child 2: {child2}, Child 3: {child3}")
        if child1 > 0.5 and child2 > 0.5 and child3 > 0.5:
            print("All children are girls")
