# Commenting and logging
print(3)

# Variable declaration
short_message = "live"

short_message = "dense"

print(short_message)

long_message = """I am  2 live
long hood"""


# Check length of string
print(len(long_message))

# prints character of string with index "2"
print(short_message[2])

# prints all characters from index 0 - 3 (excludes character with index "3")
print(short_message[0:3])
print(short_message[:3])


# print all odd numbers
new_list = [0,1,2,3,4,5,6,7,8]

print(new_list[1:9:2])

# print numbers in reverse order

print(new_list[8::-1])

print(short_message.upper())


sentence = "{} {}.".format(short_message, long_message)
print(sentence) #dense I am  2 live
#long hood.