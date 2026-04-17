grades = {
    "Alice Johnson": "A",
    "Marcus Chen": "B+",
    "Sarah Miller": "A-",
    "David Okafor": "B",
    "Elena Rodriguez": "A+",
    "Liam Smith": "C+",
    "Priya Sharma": "A",
    "Jordan Taylor": "B-"
}

student = input("Enter name... ")

if student in grades:
    print(f"{student} secured {grades[student]}")
else: 
    print("Error 404, Student Not Found")

# Notes
# returns boolean value