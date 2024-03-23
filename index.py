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
new_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(new_list[1:9:2])

# print numbers in reverse order

print(new_list[8::-1])

print(short_message.upper())


sentence = f"{short_message.upper()} {long_message.lower()}."
print(sentence)  # dense I am  2 live
# long hood.


# multiline comment :
""" 
I am alive
"""

# Working with lists(arrays)

lists = ["here", "there", "everywhere"]
## basicaly array.push
lists.append("Art")
print(lists)


#  insert an element to the index of a list
lists.insert(0, "First")
print(lists)  # ['First', 'here', 'there', 'everywhere', 'Art']

lists2 = ["list", 2, 4]

# adds elements of a list to the back of another list

lists.extend(lists2)
print(lists)  # ['First', 'here', 'there', 'everywhere', 'Art', 'list', 2, 4]

# remove an element from a list

lists.remove("here")
print(lists)  # ['First', 'there', 'everywhere', 'Art', 'list', 2, 4]
