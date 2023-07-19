class Hardware:
    def __init__(self, id, state):
        self.id = id
        self.state = state

def check_hardware(microphone_id, hardware_list):
    for hardware in hardware_list:
        if hardware.id == microphone_id:
            if hardware.state == "Good":
                return "Current state: Good."
            else:
                return "Problem detected. Check the hardware."
    return "Microphone ID not found."

def main():
    # Create hardware objects
    hardware_list = [
        Hardware("MIC001", "Good"),
        Hardware("MIC002", "Defective"),
        Hardware("MIC003", "Good"),
        Hardware("SPK001", "Good"),
        Hardware("SPK002", "Defective")
    ]

    while True:
        print("\nMenu:")
        print("1. Check microphone")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            microphone_id = input("Enter microphone ID: ")
            result = check_hardware(microphone_id, hardware_list)
            print(result)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


