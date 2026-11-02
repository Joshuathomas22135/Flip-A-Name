""" A Python program that reverses a string using recursion by calling the function on s[1:] and placing the first character at the end as
the calls return."""

def flipName(name):
    if len(name) == 1:
        return name

    return flipName(name[1:]) + name[0]

name = str(input("Enter a name: "))
fliped = flipName(name)

print(f"Reversed: {fliped}")