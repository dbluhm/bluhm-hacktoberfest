"""
Generally useful functions and stuff.
"""


def inputstr(prompt):
    """Make sure some input is received and not empty string."""
    value = ""
    while value == "":
        value = input(prompt)
    return value


def uniquestr(prompt, error, context):
    """Make sure input is an option from context."""
    while True:
        value = inputstr(prompt)
        if value.lower() not in context:
            print(error)
            continue
        break
    return value
