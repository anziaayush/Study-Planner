import json
import datetime
from collections import defaultdict

class SmartStudyPlanner:
    def __init__(self):
        self.subjects = {}
        self.schedule = defaultdict(list)

    def add_subject(self, name, weightage):
        self.subjects[name] = weightage

    def generate_schedule(self, daily_hours, start_date, end_date):
        total_weightage = sum(self.subjects.values())
        total_days = (end_date - start_date).days + 1
        total_hours = daily_hours * total_days

        subject_hours = {subject: (weight / total_weightage) * total_hours for subject, weight in self.subjects.items()}

        for i in range(total_days):
            current_date = start_date + datetime.timedelta(days=i)
            for subject, hours in subject_hours.items():
                daily_allocation = hours / total_days
                self.schedule[current_date].append((subject, round(daily_allocation, 2)))

    def display_schedule(self):
        for day, tasks in sorted(self.schedule.items()):
            print(f"\n{day.strftime('%Y-%m-%d')}:")
            for subject, hours in tasks:
                print(f"  {subject}: {hours} hours")

    def save_schedule(self, filename):
        with open(filename, 'w') as f:
            json.dump({str(k): v for k, v in self.schedule.items()}, f, indent=4)

    def load_schedule(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.schedule = {datetime.datetime.strptime(k, '%Y-%m-%d').date(): v for k, v in data.items()}

# Example usage
if __name__ == "__main__":
    planner = SmartStudyPlanner()

    # Add subjects with weightage
    planner.add_subject("Math", 8)
    planner.add_subject("Programming", 7)
    planner.add_subject("Engineering Science", 6)
    planner.add_subject("Computer Science", 9)

    # Define study parameters
    daily_hours = 6
    start_date = datetime.date(2024, 12, 7)
    end_date = datetime.date(2024, 12, 20)

    # Generate schedule
    planner.generate_schedule(daily_hours, start_date, end_date)

    # Display schedule
    planner.display_schedule()

    # Save to file
    planner.save_schedule("study_schedule.json")
