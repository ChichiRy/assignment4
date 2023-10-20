summation = 0

# Grading system welcome message
print("\n\nMitihani Grading System. Welcome user.")

# Ask for input for each of the marks
print("Please enter the following marks: ")

# Dictionary to store subject, mark/total, grade values
marks = {"Mathematics": [],
         "Physics": [],
         "Geography": [],
         "Chemistry": [],
         }

for key in marks.keys():
    entered_val = -1
    while entered_val > 100 or entered_val < 0:  # Loop keeps running until a valid value is put in
        try:
            entered_val = int(input(f"  - {str(key)}: "))
            # Request user for acceptable value
            print("Unexpected value (Mark >100/<0). Please enter a proper value.\n") if 0 > entered_val > 100 else print("Success!\n")
            marks[key].append(entered_val)
            summation += entered_val  # Line adds entered mark to a total to determine the average
        except ValueError:
            entered_val = -1
            print('Invalid input. Please enter numbers only.')

marks["Average"] = [(summation/4), ]  # Determines the average mark

# Determine grade to be stored in mark. mark["subject"]:[value, "grade"]
for key in marks.keys():
    if marks[key][0] > 70:
        marks[key].append("A")
    elif 50 < marks[key][0] <= 70:
        marks[key].append("B")
    elif 30 < marks[key][0] <= 50:
        marks[key].append("C")
    else:
        marks[key].append("D")

print(f"\n\n\nOverall grades are:")
print(''.join([f"  - {str(key)}: {(marks[key][0] if len(str(marks[key][0])) > 1 else '0' + str(marks[key][0]))}\t\t{marks[key][1]}\n" for key in marks.keys()]))
