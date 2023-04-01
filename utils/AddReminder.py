import json
from tkinter import ttk
from datetime import datetime

class AddReminder:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Set Date and Time")
        self.parent.geometry("300x150")

        # Create date picker
        self.date_label = ttk.Label(self.parent, text="Select Date:")
        self.date_label.pack()
        self.date_picker = ttk.Combobox(self.parent, values=self.get_date_list())
        self.date_picker.pack()

        # Create time picker
        self.time_label = ttk.Label(self.parent, text="Select Time:")
        self.time_label.pack()
        self.time_picker = ttk.Combobox(self.parent, values=self.get_time_list())
        self.time_picker.pack()

        # Create save button
        self.save_button = ttk.Button(self.parent, text="Save", command=self.save_datetime)
        self.save_button.pack()

    def get_date_list(self):
        date_list = []
        now = datetime.now()
        for i in range(1, 32):
            try:
                date = datetime(now.year, now.month, i)
                date_list.append(date.strftime("%Y-%m-%d"))
            except ValueError:
                # Skip this date if it's invalid
                pass
        return date_list

    def get_time_list(self):
        time_list = []
        for i in range(0, 24):
            time = datetime(2000, 1, 1, i, 0)
            time_list.append(time.strftime("%I:%M %p"))
        return time_list

    def save_datetime(self):
        selected_date = self.date_picker.get()
        selected_time = self.time_picker.get()
        try:
            selected_datetime = datetime.strptime(selected_date + " " + selected_time, "%Y-%m-%d %I:%M %p")
            print("Selected datetime: ", selected_datetime)

            reminder = {
                "time": selected_datetime.strftime("%H:%M"),
                "day": selected_datetime.strftime("%A"),
            }

            try:
                with open('./data/reminder.json', 'r+') as file:
                    data = json.load(file)
                    data['reminder'].append(reminder)
                    file.seek(0)
                    json.dump(data, file, indent=4)

            except Exception as e:
                print(e)

            self.parent.destroy()

        except ValueError:
            print("Invalid date or time")
