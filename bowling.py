def is_strike(char):
    """
    define if the current roll
    is a strike or not

    returns a boolean value
    """
    if char in "Xx":
        return True
    return False


def is_spare(char):
    """
    define if the current roll
    is a spare or not

    returns a boolean value
    """    
    if char is "/":
        return True
    return False


def is_number(char):
    """
    define if the current roll
    is just a normal score

    returns a boolean value
    """    
    if char in "123456789":
        return True
    return False


def frame_counting(frame, in_first_half, char):
    """
    keeps track of turns and frames

    returns an integer and a boolean value
    """
    if in_first_half:
        in_first_half = False
    else:
        in_first_half = True
        frame += 1
    if is_strike(char):
        in_first_half = True
        frame += 1
    return frame, in_first_half


def score_for_strike_or_spare(game, roll, char, result):
    """
    calculate the score for
    a strike or a spare

    returns integer
    """
    score = 0
    next_roll = game[roll + 1]
    next_to_next_roll = game[roll + 2]
    score += get_value(next_roll)
    if is_strike(char):
        if is_spare(next_to_next_roll):
            score += get_value(next_to_next_roll) - get_value(next_roll)
        else:
            score += get_value(next_to_next_roll)
    return score


def score(game):
    """
    calculates the total score for the game

    returns integer
    """
    result = 0
    frame = 1
    in_first_half = True
    rolls = range(len(game))
    for roll in rolls:
        char = game[roll]
        if is_spare(char):
            result += get_value(char) - last
        elif is_number(char) or is_strike(char):
            result += get_value(char)
        if frame < 10 and is_strike(char) or is_spare(char):
            result += score_for_strike_or_spare(game, roll, char, result)
        last = get_value(char)
        frame, in_first_half = frame_counting(frame, in_first_half, char)
    return result


def get_value(char):
    """
    defines the score for the actual roll

    returns an integer
    """
    if is_number(char):
        return int(char)
    if is_strike(char) or is_spare(char):
        return 10
    elif char is '-':
        return 0
    else:
        raise ValueError()
