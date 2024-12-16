import sys
import random

def simulate_dice_throws(num_throws):
    count_sum_30 = 0

    for _ in range(num_throws):
        # Generate 10 random dice throws
        dice_throws = [random.randint(1, 6) for _ in range(10)]

      # if case where checks the sum of 10 dice = 30
        if sum(dice_throws) == 30:
            count_sum_30 += 1

    # Calculate the ratio
    ratio = (count_sum_30 / num_throws)

    return ratio

# Get the number of throws from the user
if len(sys.argv) == 2:
    num_throws = int(sys.argv[1])
    ratio = simulate_dice_throws(num_throws)
    print(f"The ratio of throws where the sum of 10 dice tosses equals 30 out of {num_throws} is {ratio:.2f}")
else :
    print("Usage: python diceTest.py <num_throws>")



