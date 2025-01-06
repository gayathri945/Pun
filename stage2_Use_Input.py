def calculate_weather(T, H, W):
    return 0.5 * T**2 - 0.2 * H + 0.1 * W - 15

# Accept user input
T = float(input("Enter Temperature (T): "))
H = float(input("Enter Humidity (H): "))
W = float(input("Enter Wind Speed (W): "))

w = calculate_weather(T, H, W)

print("=== Stage 2: User Input ===")
print(f"Inputs: T={T}, H={H}, W={W}")
print(f"Weather Parameter (w): {w}")
