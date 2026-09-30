name = input("Enter your name: ")
age = input("Enter your age: ")
marks = float(input("Enter your marks: "))
student = {
    "name" : name,
    "age" : age,
    "marks" : marks
}
print("Name:",student["name"])
print("Age:",student["age"])
print("Marks",student["marks"])