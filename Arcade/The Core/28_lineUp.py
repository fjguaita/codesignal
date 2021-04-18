def lineUp(commands):
    weird = False
    total = 0
    for command in commands:
        if command == 'L' or command == 'R':
            weird = not weird
        if not weird:
            total += 1
    return total