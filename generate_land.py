import random
from termcolor import colored
from noise import pnoise2


def generate_land(columns=10, rows=10, noise_level=10):
    # data = ["*", "-", ".", "|", " ", ":", " ", "|", ".", "-", "*"]
    data = ["💜", "🚙", "🌿", "🌝", "📙", "🎒", "🎒", "📙", "🌝", "🌿", "🚙", "💜"]
    seed = random.randint(0, 100)  # add some randomness to the noise function
    land = ""

    print(f"\nGenerating a {columns} by {rows} landscape\n")

    for row in range(rows):
        for column in range(columns):
            noise = pnoise2(row / rows, column / columns, base=seed)
            noise *= noise_level  # controls how much noise there is
            noise = round(noise)
            noise = noise % len(data)

            land += data[noise]
        land += "\n"

    print("Finished generating landscape\n")
    return land


def get_number(question):
    tries = 0

    while tries < 3:
        answer = input(colored(question + "\n", "yellow"))

        if answer == "quit":
            quit()
        elif answer.isnumeric():
            return int(answer)
        else:
            print(colored("Sorry, this is not a number.", "yellow"))
            tries += 1

    print("Please try again later.")
    quit()


if __name__ == "__main__":  # only run code if running from this file
    columns = get_number("How many columns?")
    rows = get_number("How many rows?")

    output = generate_land(columns, rows)
    print(output)
