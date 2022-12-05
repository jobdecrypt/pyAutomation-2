# Explicit Conversion
base = 6
height = 3
area = (base*height) / 2
print("The area of the triangle is: " + str(area))

numerator = 10
denominator = 10
result = numerator / denominator
print(int(result))

# Functions


def greeting(name):
    print("Welcome, " + name)


greeting("job")

def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)
    
greeting("Blake", "IT Support")