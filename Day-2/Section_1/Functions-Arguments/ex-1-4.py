# Variable Keyword Args: Write def show_settings(**kwargs) and print all key-value pairs.

def show_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_settings(theme="dark", volume=70)
# Output:
# theme: dark
# volume: 70
