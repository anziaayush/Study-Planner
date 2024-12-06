# Study-Planner#
# Smart Study Planner

## **Overview**
The **Smart Study Planner** is a Python-based project designed to help students manage their study schedules effectively. By taking input on the subjects, their importance (weightage), available study hours, and the study duration, the program dynamically generates a personalized study plan to maximize productivity.

---

## **Features**
- **Subject Prioritization:** Allocate study time based on the importance (weightage) of each subject.
- **Dynamic Scheduling:** Create a daily study plan for the defined study period.
- **Progress Tracker (Future Update):** Tracks completed study sessions and adjusts the plan dynamically.
- **Save and Load Schedule:** Save your generated schedule to a JSON file for future reference or modification.

---

## **Technology Used**
- **Programming Language:** Python 3
- **Libraries:**
  - `json` for saving and loading schedules.
  - `datetime` for handling dates and time allocations.

---

## **How to Use**

### 1. Prerequisites
- Install Python 3 on your system.

### 2. Clone the Repository
```bash
git clone <repository-link>
cd smart-study-planner
```

### 3. Run the Script
```bash
python smart_study_planner.py
```

### 4. Follow These Steps in the Program
- Add your subjects and their weightages.
- Define your daily available study hours and the study period (start and end dates).
- Generate and view your personalized study schedule.
- Save the schedule to a JSON file for future use.

---

## **Example**
### Input:
- Subjects: Math (Weightage: 8), Programming (Weightage: 7), Engineering Science (Weightage: 6), Computer Science (Weightage: 9)
- Daily Study Hours: 6
- Study Period: 2024-12-07 to 2024-12-20

### Output:
```text
2024-12-07:
  Math: 1.2 hours
  Programming: 1.05 hours
  Engineering Science: 0.9 hours
  Computer Science: 1.35 hours

2024-12-08:
  Math: 1.2 hours
  Programming: 1.05 hours
  Engineering Science: 0.9 hours
  Computer Science: 1.35 hours
...
```

---

## **Future Enhancements**
- **Reminder System:** Notifications for scheduled study sessions.
- **Progress Tracking:** Update the schedule dynamically based on completed tasks.
- **GUI:** A user-friendly interface using Tkinter or a web-based platform.

---

## **Contributing**
Contributions are welcome! Feel free to fork the repository and create a pull request with your enhancements or bug fixes.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
For queries or suggestions, reach out to:
- **Name:** Aayush Anzi
- **Email:** anziaayush01@gmail.com


