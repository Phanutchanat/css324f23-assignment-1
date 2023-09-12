def initial_state():
    return (8, 0, 0)

def is_goal(s):
    a, b, _ = s
    return a == 4 and b == 4

def successors(s):
    a, b, c = s
    successors_list = []

    # Pour from 8-liter to 5-liter bottle
    if a > 0 and b < 5:
        amount_to_pour = min(a, 5 - b)
        new_state = (a - amount_to_pour, b + amount_to_pour, c)
        successors_list.append((new_state, amount_to_pour))

    # Pour from 5-liter to 8-liter bottle
    if b > 0 and a < 8:
        amount_to_pour = min(b, 8 - a)
        new_state = (a + amount_to_pour, b - amount_to_pour, c)
        successors_list.append((new_state, amount_to_pour))

    # Pour from 8-liter to 3-liter bottle
    if a > 0 and c < 3:
        amount_to_pour = min(a, 3 - c)
        new_state = (a - amount_to_pour, b, c + amount_to_pour)
        successors_list.append((new_state, amount_to_pour))

    # Pour from 3-liter to 8-liter bottle
    if c > 0 and a < 8:
        amount_to_pour = min(c, 8 - a)
        new_state = (a + amount_to_pour, b, c - amount_to_pour)
        successors_list.append((new_state, amount_to_pour))

    # Pour from 5-liter to 3-liter bottle
    if b > 0 and c < 3:
        amount_to_pour = min(b, 3 - c)
        new_state = (a, b - amount_to_pour, c + amount_to_pour)
        successors_list.append((new_state, amount_to_pour))

    # Pour from 3-liter to 5-liter bottle
    if c > 0 and b < 5:
        amount_to_pour = min(c, 5 - b)
        new_state = (a, b + amount_to_pour, c - amount_to_pour)
        successors_list.append((new_state, amount_to_pour))

    return successors_list
