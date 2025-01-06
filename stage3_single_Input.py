file_path = "input_single.txt"

with open(file_path, 'r') as file:
    line = file.readline()
    T, H, W = map(float, line.split())

w = 0.5 * T**2 - 0.2 * H + 0.1 * W - 15
print(f"Input: T={T}, H={H}, W={W} => Weather Parameter (w): {w}")
