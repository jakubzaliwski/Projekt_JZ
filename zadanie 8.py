from datetime import datetime
import random

def create_files():
    for _ in range(1, 11):
        current_time = datetime.now()
        current_time_str = current_time.strftime("%Y_%m_%d_%H_%M_%S_%f")
        file_name = f"{current_time_str}.bin"

        with open(file_name, 'wb') as file:
            for _ in range(10):
                number = random.randint(1, 100)
                file.write(str(number).encode() + b'\n')

create_files()

