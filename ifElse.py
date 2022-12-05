# Sample of username

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("What a Valid Username")


hint_username("hello")


def is_positive(number):
    if number > 0:
        return True


print(is_positive(4))

# If and Else


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


print(is_positive(5))

# Even or Odd


def is_even(number):
    # to see if the number given is divisible by 2 or equal "==" to 0
    if number % 2 == 0:
        return True
    return False


print(is_even(2))


# to check a number that's divisible by 3
def nat_numbers(num):
    for i in range(num):
        if i % 3 == 0:
            print(i)


nat_numbers(1000)
