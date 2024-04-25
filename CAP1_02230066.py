#Ngawang Sonam Yoezer
#1 Electrical
#02230066
#References
# https://www.youtube.com/watch?v=BVfCWuca9nw
# https://realpython.com/python-rock-paper-scissors/
#Solution
#solution score: 40671
#solution number : input_6_cap1
def read_input_file(file_name):
    rounds = []
    with open(file_name, 'r') as file:
        for line in file:
            opponent_choice, desired_outcome = line.strip().split()
            rounds.append((opponent_choice, desired_outcome))
    return rounds

def calculate_score(opponent_choice, desired_outcome, your_choice):
    # opponent's choice to numerical value
    if opponent_choice == 'A':
        opponent_value = 1  # Rock
    elif opponent_choice == 'B':
        opponent_value = 2  # Paper
    elif opponent_choice == 'C':
        opponent_value = 3  # Scissors
    
    # desired outcome to score value
    if desired_outcome == 'X':
        outcome_score = 0  # Loss
    elif desired_outcome == 'Y':
        outcome_score = 3  # Draw
    elif desired_outcome == 'Z':
        outcome_score = 6  # Win
    
    your_score = 0
    if your_choice == opponent_value:
        # Draw
        your_score = 1 + outcome_score
    elif (your_choice == 1 and opponent_value == 3) or (your_choice == 2 and opponent_value == 1) or (your_choice == 3 and opponent_value == 2):
        # Win
        your_score = 1 + 6
    else:
        # Loss
        your_score = 1 + 0
    
    return your_score

def main():
    #  input file path
    input_file = r"input_6_cap1.txt"
    
    rounds = read_input_file(input_file)
    
    total_score = 0
    for opponent_choice, desired_outcome in rounds:
        # Determine your choice based on desired outcome
        if desired_outcome == 'Y':
            your_choice = 1  # Rock to draw
        elif desired_outcome == 'X':
            your_choice = 2  # Paper to lose
        elif desired_outcome == 'Z':
            your_choice = 3  # Scissors to win
        
        score = calculate_score(opponent_choice, desired_outcome, your_choice)
        total_score += score
    
    print("Total Score:", total_score)


main()
