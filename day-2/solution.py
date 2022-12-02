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
    print('My score:', sum(scores))

def my_total_score_2(input):
    input_2 = []
    for item in input:
        outcome = my_map[item[1]]['outcome']
        opponent_move = part2_draw[item[0]]
        if outcome == 'draw':
            input_2.append([item[0], opponent_move])
        elif outcome == 'win':
            input_2.append([item[0], part2_loser[item[0]]])
        else:
            pass
            input_2.append([item[0], part2_winner[item[0]]])
    # Resuing first solution
    my_total_score(input_2)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    input = refine_input(input)
    my_total_score(input)
    my_total_score_2(input)

