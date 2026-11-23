def alibi(statements):
    stories = {}
    
    # 1. Build the nested dictionary
    for line in statements:
        person, rest = line.split(" was with ")
        partner, time = rest.split(" at ")
        
        if time not in stories:
            stories[time] = {}
        stories[time][person] = partner

    # 2. Find the liar by checking for mismatched partner claims
    for time in stories:
        for person, partner in stories[time].items():
            if partner in stories[time] and stories[time][partner] != person:
                return person

    return ""


if __name__ == "__main__":
    statements = []
    while True:
        line = input().strip()
        if line == "stop":
            break
        if line:
            statements.append(line)
            
    print(alibi(statements))