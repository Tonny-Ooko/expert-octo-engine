import sqlite3
from tkinter import Tk, messagebox, simpledialog
from Hardware import check_hardware

class HardwareManagement:
    def __init__(self):
        self.conn = None

    def create_table(self, table_name):
        self.conn.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                            (id TEXT PRIMARY KEY,
                             type TEXT,
                             name TEXT,
                             year INTEGER)''')

    def register_device(self, table_name, device_type):
        id = simpledialog.askstring(f"{device_type} Registration", "Enter ID:")
        type = simpledialog.askstring(f"{device_type} Registration", "Enter Type:")
        name = simpledialog.askstring(f"{device_type} Registration", "Enter Name:")
        year = simpledialog.askinteger(f"{device_type} Registration", "Enter Year of Manufacture:")

        self.conn.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?)", (id, type, name, year))
        self.conn.commit()

        messagebox.showinfo(f"{device_type} Registration", f"{device_type} registered successfully!")

    def check_hardware_state(self):
        id = simpledialog.askstring("Hardware Check", "Enter ID (Microphone/Speaker):")
        result = check_hardware(id, self.conn)
        messagebox.showinfo("Hardware Check", result)

    def main(self):
        # Create database connection and tables
        self.conn = sqlite3.connect('hardware.db')
        self.create_table('microphones')
        self.create_table('speakers')

        while True:
            # Prompt user to select microphone, speaker registration, or hardware check
            root = Tk()
            root.withdraw()
            choice = messagebox.askquestion("Hardware Management", "What would you like to do?\n\n1. Register Microphone\n2. Register Speaker\n3. Check Hardware State\n\nChoose 'Yes' for options 1 and 2, 'No' for option 3")

            if choice == 'yes':
                register_choice = simpledialog.askinteger("Hardware Management", "Which device would you like to register?\n\n1. Microphone\n2. Speaker")

                if register_choice == 1:
                    self.register_device('microphones', 'Microphone')
                elif register_choice == 2:
                    self.register_device('speakers', 'Speaker')
                else:
                    messagebox.showwarning("Hardware Management", "Invalid choice. Please try again.")
            elif choice == 'no':
                self.check_hardware_state()
            else:
                messagebox.showwarning("Hardware Management", "Invalid choice. Please try again.")

            # Prompt user to continue or exit
            choice = messagebox.askquestion("Hardware Management", "Do you want to continue?\n\nYes: Continue\nNo: Exit")

            if choice == 'no':
                break

        self.conn.close()


if __name__ == "__main__":
    manager = HardwareManagement()
    manager.main()


    def check_hardware(device_id, conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM microphones WHERE id = ?", (device_id,))
        microphone = cursor.fetchone()

        cursor.execute("SELECT * FROM speakers WHERE id = ?", (device_id,))
        speaker = cursor.fetchone()

        if microphone:
            return f"Microphone found:\nID: {microphone[0]}\nType: {microphone[1]}\nName: {microphone[2]}\nYear of Manufacture: {microphone[3]}"
        elif speaker:
            return f"Speaker found:\nID: {speaker[0]}\nType: {speaker[1]}\nName: {speaker[2]}\nYear of Manufacture: {speaker[3]}"
        else:
            return "Device not found."

