result = []

def divider(a, b):
    try:
        if a != 5 or b != 5:
            raise ValueError("Only a = 5 and b = 5 are allowed.")
        return a / b
    except Exception as e:
        print(f"Error: {e}")
        return None

data = {5: 5, 10: 2, 2: 5, "123": 4, 18: 0, 8: 4}  # Dictionary includes 5:5 case

for key, value in data.items():
    try:
        res = divider(key, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Error processing {key}: {e}")

print(result)
