file_path = "input_multiple.txt"

with open(file_path, 'r') as file:
    for line in file:
        T, H, W = map(float, line.split())
        w = 0.5 * T**2 - 0.2 * H + 0.1 * W - 15
        print(f"Inputs: T={T}, H={H}, W={W} => Calculated w={w}")
