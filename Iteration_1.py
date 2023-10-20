summation = 0

# Grading system welcome message
print("\n\nMitihani Grading System. Welcome user.")

# Ask for input for each of the marks
print("Please enter the following marks: ")

maths = int(input("  - Mathematics: "))
if maths > 100 or maths < 0:
    while maths > 100 or maths < 0:  # Loop keeps running until a valid value is put in
        #  Request user for acceptable value
        print("Unexpected value (Mark >100/<0). Please enter a proper value.\n")
        maths = int(input("  - Mathematics: "))
else:
    pass
summation += maths  # Line adds entered mark to a total to determine the average

physics = int(input("  - Physics: "))
if physics > 100 or physics < 0:
    while physics > 100 or physics < 0:
        print("Unrecognised mark (Mark >100/<0). Please enter a proper value.\n")
        physics = int(input("  - Physics: "))
else:
    pass
summation += physics

geo = int(input("  - Geography: "))
if geo > 100 or geo < 0:
    while geo > 100 or geo < 0:
        print("Unexpected value (Mark >100/<0). Please enter a proper value.\n")
        geo = int(input("  - Geography: "))
else:
    pass
summation += geo

chem = int(input("  - Chemistry: "))
if chem > 100 or chem < 0:
    while chem > 100 or chem < 0:
        print("Unexpected value (Mark >100/<0). Please enter a proper value.\n")
        chem = int(input("  - Chemistry: "))
else:
    pass
summation += chem

average = summation / 4  # Determines the average mark

# Dictionary to store subject, mark/total, grade values
marks = {"maths": [maths, ],
         "physics": [physics, ],
         "geo": [geo, ],
         "chem": [chem, ],
         "Average": [average, ]}

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


print(f"\n\n\nOverall grades are:"
      f"\n  - Mathematics:\t {(marks['maths'][0] if len(str(marks['maths'][0])) > 1 else '0' + str(marks['maths'][0]))}\t\t{marks['maths'][1]}"
      f"\n  - Physics:\t\t {(marks['physics'][0] if len(str(marks['physics'][0])) > 1 else '0' + str(marks['physics'][0]))}\t\t{marks['physics'][1]}"
      f"\n  - Geography:\t\t {(marks['geo'][0] if len(str(marks['geo'][0])) > 1 else '0' + str(marks['geo'][0]))}\t\t{marks['geo'][1]}"
      f"\n  - Chemistry:\t\t {(marks['chem'][0] if len(str(marks['chem'][0])) > 1 else '0' + str(marks['chem'][0]))}\t\t{marks['chem'][1]}"
      f"\n  * Average grade:\t\t\t{marks['Average'][1]}")
