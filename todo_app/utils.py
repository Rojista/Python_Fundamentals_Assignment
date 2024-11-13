
import os

def clear_screen():
    """Clears the terminal screen."""
    # 'cls' for Windows, 'clear' for other operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

