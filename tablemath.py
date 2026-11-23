def tablemath(groups, command):
    parts = command.split()
    action = parts[0]
    group_name = parts[1]
    
    if action == "seat":
        groups[group_name] = 0
        return None
    elif action == "spend":
        amount = int(parts[2])
        groups[group_name] += amount
        return None
    elif action == "checkout":
        return groups.pop(group_name)
    
    return None


if __name__ == "__main__":
    groups = {}
    line = input()
    while line != "stop":
        result = tablemath(groups, line)
        if result is not None:
            print(result)
        line = input()