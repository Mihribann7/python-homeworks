import csv

with open('grades.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(["Name", "Subject", "Grade"])
     writer.writerow(["Alice", "Math", 85])
     writer.writerow(["Bob", "Science", 78])
     writer.writerow(["Carol", "Math", 92])
     writer.writerow(["Dave", "History", 74])

grades_data = []
with open('grades.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['Grade'] = int(row['Grade'])  
        grades_data.append(row)

subject_totals = {}
subject_counts = {}

for entry in grades_data:
    subject = entry['Subject']
    grade = entry['Grade']

    if subject not in subject_totals:
        subject_totals[subject] = 0
        subject_counts[subject] = 0

    subject_totals[subject] += grade
    subject_counts[subject] += 1

average_grades = {subject: round(subject_totals[subject] / subject_counts[subject], 1)
                  for subject in subject_totals}

# Step 4: Write averages to a new file average_grades.csv
with open('average_grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg_grade in average_grades.items():
        writer.writerow([subject, avg_grade])

print("Average is calculated")
