
import threading
import time

# 1. Function to Count Numbers
def count_numbers():
    for i in range(1, 6):
        print("Counting:", i)
        time.sleep(1)


# 2. Function to Calculate Squares
def calculate_squares():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(1)


# 3. Function to Calculate Cubes
def calculate_cubes():
    for i in range(1, 6):
        print("Cube of", i, "=", i * i * i)
        time.sleep(1)


# 4. Main Function
if __name__ == "__main__":

    print("Starting Multithreading Program\n")

    # Create Threads
    t1 = threading.Thread(target=count_numbers)
    t2 = threading.Thread(target=calculate_squares)
    t3 = threading.Thread(target=calculate_cubes)

    # Start Threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for Threads to Complete
    t1.join()
    t2.join()
    t3.join()

    print("\nAll Threads Completed Successfully!")
