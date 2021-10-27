# Python does not know Block Scope

# This has global Scope
# This can accessed from the inside of a function if not shadowed
enemies = 1


def increase_enemies():
    # By default this variable is shadowing the outer variable, IF you try to assign to it
    # It is also local, it is not accessible from the outside

    # Force the function to access the global variable
    # Don't do this, it's not nice...
    global enemies
    # This is the way to go, no shadowing, just return statements, reading is fine
    return enemies + 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
