opponent_map = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

my_map = {
    'X': {
        'value': 'rock',
        'outcome': 'lose',
        'score': 1
    },
    'Y': {
        'value': 'paper',
        'outcome': 'draw',
        'score': 2
    },
    'Z': {
        'value': 'scissors',
        'outcome': 'win',
        'score': 3
    }
}

winner = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

loser = {
    'scissors': 'rock',
    'rock': 'paper',
    'paper': 'scissors'
}

part2_winner = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

part2_loser = {
    'C': 'X',
    'A': 'Y',
    'B': 'Z'
}

part2_draw= {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}



def refine_input(input):
    round = input.split('\n')
    round_separated = [game.split(' ') for game in round]
    return round_separated

def my_total_score(input):
    scores = []
    for item in input:
        opponent = opponent_map[item[0]]
        me = my_map[item[1]]['value']
        if opponent == me:
            scores.append(3+my_map[item[1]]['score'])
        elif (winner[me] == opponent):
            scores.append(6+my_map[item[1]]['score'])
        else:
            scores.append(my_map[item[1]]['score'])
    return sum(scores)

def my_total_score_2(input):
    prepared_input = []
    for item in input:
        outcome = my_map[item[1]]['outcome']
        if outcome == 'draw':
            prepared_input.append([item[0], part2_draw[item[0]]])
        elif outcome == 'win':
            prepared_input.append([item[0], part2_loser[item[0]]])
        else:
            pass
            prepared_input.append([item[0], part2_winner[item[0]]])
    # Resuing first solution
    return my_total_score(prepared_input)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = refine_input(input)
    score_1 = my_total_score(input)
    score_2 = my_total_score_2(input)
    print('Answer 1:', score_1)
    print('Answer 2:', score_2)


