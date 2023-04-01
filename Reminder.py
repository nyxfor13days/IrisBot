import json
from datetime import datetime
from utils.Notify import Notify


class MedicationReminder:
    def __init__(self) -> None:
        with open('./data/reminder.json', 'r') as file:
            self.data = json.load(file)

    def notification(self, current_time, current_day):
        for reminder in reminder['reminder']:
            if current_time in reminder['time'] and current_day in reminder['days']:
                Notify(message='You have to take your medication now.')

                with open('./data/reminder.json', 'w') as file:
                    self.data['reminder'].remove(reminder['time'])


if __name__ == "__main__":
    medication_reminder = MedicationReminder()

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_day = now.strftime("%A")
        medication_reminder.notification(
            current_day=current_day, current_time=current_time)
