def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor"
    else:
        return "Hello there, " + name


print(greeting("Taylor"))
print(greeting("John"))

# What's the output of this code if number equals 10?
number = 10

if number > 11:
    print(0)
elif number != 10:
    print(1)
elif number >= 20 or number < 12:
    print(2)
else:
    print(3)

# finding file size


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # print(partial_block_remainder)

    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0 and full_blocks != 0:
        return block_size*2
    return block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192
