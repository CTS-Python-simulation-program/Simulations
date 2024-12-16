import random
import sys

def calc_girls(iterations):
    G1 = 0 #all girls
    G2 = 0 #at least one girl

    for i in range(iterations):
        r = [random.choice(["Girl","Boy"]) for c in range(3)] #randomly select 3 children
        if "Girl" in r:
            G2+=1
            if(r.count("Girl")==3):
                G1+= 1
        
    probability = G1 / G2

    print("Probability of the children being all girls when at least one child is a girl = ",probability)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit(1)
    try:
      iterations = int(sys.argv[1])
      if iterations <= 0:
         print("Please enter a positive integer")
         sys.exit(1)
      
      calc_girls(iterations)

    except ValueError:
        print("Please enter a valid integer")
