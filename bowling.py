def is_strike(char):
    if char in "Xx":
        return True
    return False


def is_spare(char):
    if char is "/":
        return True
    return False


def is_number(char):
    if char in "123456789":
        return True
    return False

def frame_counting(frame, in_first_half, char):
    if in_first_half:
        in_first_half = False
    else:
        in_first_half = True
        frame += 1
    if is_strike(char):
        in_first_half = True
        frame += 1
    return frame, in_first_half


def score_for_strike_and_spare(game, i, char, result):
    score = 0
    next_roll = game[i + 1]
    next_to_next_roll = game[i + 2]
    score += get_value(next_roll)
    if is_strike(char):
        if is_spare(next_to_next_roll):
            score += get_value(next_to_next_roll) - get_value(next_roll)
        else:
            score += get_value(next_to_next_roll)
    return score

def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        char = game[i]
        if is_spare(char):
            result += get_value(char) - last
        elif is_number(char) or is_strike(char):
            result += get_value(char)
        if frame < 10 and is_strike(char) or is_spare(char):
            result += score_for_strike_and_spare(game, i, char, result)
        last = get_value(char)
        frame, in_first_half = frame_counting(frame, in_first_half, char)
    return result


def get_value(char):
    if is_number(char):
        return int(char)
    if is_strike(char) or is_spare(char):
        return 10
    elif char is '-':
        return 0
    else:
        raise ValueError()
