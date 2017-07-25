def score(game):
    bowling_score = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            bowling_score += 10 - last
        else:
            bowling_score += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                bowling_score += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                bowling_score += get_value(game[i+1])
                if game[i+2] == '/':
                    bowling_score += 10 - get_value(game[i+1])
                else:
                    bowling_score += get_value(game[i+2])
        last = get_value(game[i])
        if in_first_half is False:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] == ('X') or game[i] == 'x':
            in_first_half = True
            frame += 1
    return bowling_score

#renamed result to bowling_score
#fixed boolean requirements


def get_value(char):
    char_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    char_sign_list = ['X', 'x', '/']
    if char in char_list:
        return int(char)
    elif char in char_sign_list:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

#ordered get_value into lists
