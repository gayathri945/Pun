def calculate_weather(T, H, W):
    return 0.5 * T**2 - 0.2 * H + 0.1 * W - 15

# Hardcoded values for testing
T, H, W = 10, 50, 20  # Example values
w = calculate_weather(T, H, W)

print("=== Stage 1: Basic Calculation ===")
print(f"Inputs: T={T}, H={H}, W={W}")
print(f"Weather Parameter (w): {w}")
