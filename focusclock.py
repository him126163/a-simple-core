import time

def concentration_timer(minutes):
    """Counts down from the specified number of minutes."""
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        print("Time remaining:", i // 60, "minutes", i % 60, "seconds")
        time.sleep(1)
    print("Time's up! Focus time is over.")

if __name__ == "__main__":
    concentration_timer(25)
