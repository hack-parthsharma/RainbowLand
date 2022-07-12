import os
from generate_land import get_number, generate_land

output_dir = os.path.join(os.getcwd(), "outputs")
os.makedirs(output_dir, exist_ok=True)
print(os.path.realpath(__file__))
noise_levels = [5, 10, 20, 50, 100]

for nl in noise_levels:
    output = generate_land(80, 80, nl)

    filename = os.path.join("outputs", f"noise-levels-{nl}.txt")

    with open(filename, "w") as file:
        file.write(output)
