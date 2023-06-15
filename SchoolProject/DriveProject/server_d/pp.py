import tkinter as tk
from tkcalendar import Calendar, DateEntry


class MyCalendarApp:
    def __init__(self):
        self.root = tk.Tk()
        self.calendar = Calendar(self.root, selectmode="day", year=2023, month=6, day=1)
        self.calendar.pack()
        self.calendar.bind("<<CalendarSelected>>", self.handle_selection)

        # Disable Sundays in the calendar
        self.calendar.datevalidation_callback = self.validate_date

    def validate_date(self, date):
        # Check if the selected date is a Sunday (weekday == 6)
        if date.weekday() == 6:
            return False
        return True

    def handle_selection(self, event):
        selected_date = self.calendar.selection_get()
        print("Selected date:", selected_date)

    def run(self):
        self.root.mainloop()


# Create an instance of the MyCalendarApp class
app = MyCalendarApp()

# Run the application
app.run()
