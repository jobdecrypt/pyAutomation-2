# using return statement
def area_triangle(base, height):
    return base*height/2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


# here you can change the value of "remaining_seconds" since it's a return of the function "convert_seconds()"
hours, minutes, seconds = convert_seconds(5000)

print(hours, minutes, seconds)

# another sample


def greeting(name):
    print("Welcome, " + name)

# this will output "Welcome, Christine" but there's no "return" value of the function "greeting(name)"...
result = greeting("Christine")
# ... hence as we output the next line, the output will be "None". Means empty or nothing
print(result)