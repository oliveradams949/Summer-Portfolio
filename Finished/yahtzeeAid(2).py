import random
import itertools

dice_choices = []
for i in range(1,6):
    choices = itertools.combinations(tuple(range(1,6)), i)
    dice_choices.extend(choices)

dice_choices.append(tuple([]))

class handTypes:
    def __init__(self):
        self.three_of_a_kind_achieved = False
        self.four_of_a_kind_achieved = False
        self.full_house_achieved = False       
        self.yahtzee_achieved = False
        self.small_straight_achieved = False
        self.large_straight_achieved = False
        self.chance_achieved = False
        self.aces_achieved = False
        self.twos_achieved = False
        self.threes_achieved = False
        self.fours_achieved = False
        self.fives_achieved = False
        self.sixes_achieved = False

hand_types = handTypes()


def roller(n):
    """
    An n dice roller, that returns the results in a single list.
    
    Parameters
    __________

    n, integer.

    Returns
    __________

    rolls: list of length n, of numbers from 1 to 6.
    
    """
    rolls = [random.randint(1,6) for roll in range(n)]
    return rolls

def number_checker(given_hand):
    """
    Takes a given hand, and then counts the number of values of each number from one to six, appending each to a list.

    e.g. number_checker([1,2,3,3,6]) returns [1,1,2,0,0,1]
    
    Parameters
    __________
    given_hand, list of 5 integers from 1 to 6

    Returns
    __________
    dice_number, list of 6 integers from 1 to 6
    
    """
    dice_number = []
    for x in range(1,7):
        dice_number.append(given_hand.count(x))
    return dice_number

def achievable_lower_hands(lower_achieved):
    """
    Used to define what lower hand types are still achievable for later simulations.
    Checks if the inputs are correct, then updates each of the variables.

    Parameters
    ___________

    lower_achieved, list, length 7, all either ones or zeros.
    ___________

    Takes each variable in the class hand_types, then modifies them dependent upon if a corresponding value is a one or a zero. 
    There are 7, which will then be compared in later functions, but not modified. Used in tandem with upper_hands in game_setup.
    """
    counter_lower = 0
    for i in lower_achieved:
        if i != 0 and i != 1:
            raise Exception("Incorrect input of lower hands.")
        else:
            counter_lower += 1
        if counter_lower == 7:   
            if lower_achieved[0] == 1:
                hand_types.three_of_a_kind_achieved = True
            else:
                hand_types.three_of_a_kind_achieved = False
            if lower_achieved[1] == 1:
                hand_types.four_of_a_kind_achieved = True
            else:
                hand_types.four_of_a_kind_achieved = False
            if lower_achieved[2] == 1:
                hand_types.full_house_achieved = True
            else:
                hand_types.full_house_achieved = False
            if lower_achieved[4] == 1:
                hand_types.small_straight_achieved = True
            else:
                hand_types.small_straight_achieved = False
            if lower_achieved[5] == 1:
                hand_types.large_straight_achieved = True
            else:
                hand_types.large_straight_achieved = False
            if lower_achieved[6] == 1:
                hand_types.chance_achieved = True
            else:
                hand_types.chance_achieved = False
            if lower_achieved[3] == 1:
                hand_types.yahtzee_achieved = True
            else:
                hand_types.yahtzee_achieved = False

def achievable_upper_hands(upper_achieved):
    """
    Used to define what upper hand types are still achievable for later simulations.
    Checks if the inputs are correct, then updates each of the variables.

    Parameters
    ___________

    upper_achieved: list, length 6, all either ones or zeros.
    ___________

    Takes each variable in the class hand_types, then modifies them dependent upon if a corresponding value is a one or a zero. 
    There are 6, which will then be compared in later functions, but not modified. Used in tandem with lower_hands in game_setup.
    """

    counter_upper = 0
    for i in upper_achieved:
        if i != 0 and i != 1:
            raise Exception("Incorrect input of lower hands.")
        else:
            counter_upper += 1
        if counter_upper == 6:
            if upper_achieved[0] == 1:
                hand_types.aces_achieved = True
            else:
                hand_types.aces_achieved = False
            if upper_achieved[1] == 1:
                hand_types.twos_achieved = True
            else:
                hand_types.twos_achieved = False
            if upper_achieved[2] == 1:
                hand_types.threes_achieved = True
            else:
                hand_types.threes_achieved = False
            if upper_achieved[3] == 1:
                hand_types.fours_achieved = True
            else:
                hand_types.fours_achieved = False
            if upper_achieved[4] == 1:
                hand_types.fives_achieved = True
            else:
                hand_types.fives_achieved = False
            if upper_achieved[5] == 1:
                hand_types.sixes_achieved = True
            else:
                hand_types.sixes_achieved = False

def game_setup(turn, lower_achieved, upper_achieved):
    """
    Used to define what hand types are still achievable for later simulations.
    Checks if the inputs are correct, then updates each of the variables, using the functions lower_hands and upper_hands.

    Parameters
    ___________

    turn, int, between 1 and 13

    lower_achieved, list, length 7, all either ones or zeros.

    upper_achieved, list, length 6, either ones or zeros.

    ___________

    Takes each variable in the class hand_types, then modifies them dependent upon if a corresponding value is a one or a zero. 
    There are 13, which will then be compared in later functions, but not modified.
    """
    if 1 <= turn <= 13:
        if len(lower_achieved) == 7 and len(upper_achieved) ==  6:
            achievable_lower_hands(lower_achieved)
            achievable_upper_hands(upper_achieved)
        else:
            raise Exception("Incorrect input length of lower/upper hands.")
            
    else:
        raise Exception("Incorrect input of the turns.")
      


def simmed_hand_holder(turn_hand, dice_held):
    """
    Used to hold specified dice within a given hand.

    Parameters
    __________
    dice_held, a list of integers from 1 to 5, of length 0 to 5. Has 32 possibilities, listed in dice_choices

    turn_hand, a list of integers from 1 to 6, of length 5.
    
    Returns
    __________
    held_hand, a list of integers from 1 to 6, with length equivalent to the length of dice_held.
    
    """
    used_hand = tuple(turn_hand)
    held_hand = []
    held_numbers = []
    if len(dice_held) <= 5:
        for i in range(len(dice_held)):
            specifiedNum = dice_held[i]
            if 1<=specifiedNum < 6:
                if specifiedNum not in held_numbers:
                    held_hand.append(used_hand[specifiedNum - 1])
                    held_numbers.append(specifiedNum)
                else:
                    raise Exception("Incorrect input of numbers, duplicates.")
            else:
                raise Exception("Incorrect input of numbers, number not in range.")
    else:
        raise Exception("Incorrect number of dice held, please specify a number between 0 and 5.")    
    held_hand.sort()
    return held_hand

def hand_scorer(given_hand):
    """
    Scores a given hand, by first calculating the possible score for each open slot the hand can be entered, 
    which is then inserted into a representative list, preliminary_score.
    Then returns the largest number in the list, preliminary_score.

    This function is dependent on number_checker and game_setup to work.

    The slot is checked if it is open by checking against the corresponding global variable defined in game_setup.

    Parameters
    __________
    
    given_hand: List of length 5 of numbers between 1 and 6
    
    Returns
    __________

    preliminary_score, integer

    """
    dice_number = number_checker(given_hand)
    preliminary_score_list = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    preliminary_score = 0
    if 2 in dice_number and 3 in dice_number:
        if hand_types.full_house_achieved != True:
            preliminary_score_list[3] = 25
        if hand_types.three_of_a_kind_achieved != True:
            preliminary_score_list[0] = sum(given_hand)
    elif 3 in dice_number and 2 not in dice_number:
        if hand_types.three_of_a_kind_achieved != True:
            preliminary_score_list[0] = sum(given_hand)
    if 4 in dice_number:
        if hand_types.four_of_a_kind_achieved != True:
            preliminary_score_list[1] = sum(given_hand)
        if hand_types.three_of_a_kind_achieved != True:
            preliminary_score_list[0] = sum(given_hand)
    if 5 in dice_number:
        if hand_types.yahtzee_achieved != True:
            preliminary_score_list[2] = 50
        else:
            preliminary_score_list[2] = 100
    if dice_number[0:4].count(0) == 0 or dice_number[1:5].count(0) == 0 or dice_number[2:].count(0) == 0:
        if dice_number[0:5].count(0) == 0 or dice_number[1:].count(0) == 0:
            if hand_types.large_straight_achieved != True:
                    preliminary_score_list[5] = 40
            else:
                if hand_types.small_straight_achieved != True:
                    preliminary_score_list[4] = 30
                
        else:
            if hand_types.small_straight_achieved != True:
                preliminary_score_list[4] = 30
    if hand_types.chance_achieved != True:
        preliminary_score_list[6] = sum(given_hand)
    if hand_types.aces_achieved != True:
        preliminary_score_list[7] = dice_number[0] * 1
    if hand_types.twos_achieved != True:
        preliminary_score_list[8] = dice_number[1] * 2
    if hand_types.threes_achieved != True:
        preliminary_score_list[9] = dice_number[2] * 3
    if hand_types.fours_achieved != True:
        preliminary_score_list[10] = dice_number[3] * 4
    if hand_types.fives_achieved != True:
        preliminary_score_list[11] = dice_number[4] * 5
    if hand_types.sixes_achieved != True:
        preliminary_score_list[12] = dice_number[5] * 6
    

    preliminary_score = max(preliminary_score_list)
    return preliminary_score

def in_hand_hand_type(given_hand):
    """
    Checks what hands the given hand is eligible for, then returns a list of true or false values for them.
    
    Dependent upon number_checker and game_setup to work.

    Paramters
    _________
    
    given_hand: list of 5 numbers between 1 and 6

    Returns
    _______
    list of 6 boolean values, representing the six hand types that require eligibility.
    """
    dice_number = number_checker(given_hand)
    three_of_a_kind_in_hand = False
    four_of_a_kind_in_hand = False
    yahtzee = False
    small_straight_in_hand = False
    large_straight_in_hand = False
    full_house_in_hand = False

    if 2 in dice_number and 3 in dice_number:
        full_house_in_hand = True
        three_of_a_kind_in_hand = True
    elif 3 in dice_number and 2 not in dice_number:
        three_of_a_kind_in_hand = True
    if 4 in dice_number:
        four_of_a_kind_in_hand = True
        three_of_a_kind_in_hand = True
    if 5 in dice_number:
        yahtzee = True
        four_of_a_kind_in_hand=True
        three_of_a_kind_in_hand=True
    if dice_number[0:4].count(0) == 0 or dice_number[1:5].count(0) == 0 or dice_number[2:6].count(0) == 0:
        if dice_number[0:5].count(0) == 0 or dice_number[1:6].count(0) == 0:
            large_straight_in_hand = True
            small_straight_in_hand = True
        else:
            small_straight_in_hand = True

    return three_of_a_kind_in_hand, four_of_a_kind_in_hand, full_house_in_hand, yahtzee, small_straight_in_hand, large_straight_in_hand

def roll_sim(turn_hand, hold):
    """
    Sims a roll, consisting first of a hold and then a roll.

    Parameters
    __________

    turn_hand: list of 5 numbers from 1 to 6. Either  blank (e.g. []) or of length 5.

    hold: list of up to five numbers from 1 to 5. 

    Returns
    _______
    
    turn_hand: the new hand for the next roll. Same structure  as turn_hand.

    """
    if turn_hand == []:
        turn_hand = roller(5)
        return turn_hand
    else:
        if len(turn_hand) == 5:
            turn_hand = simmed_hand_holder(turn_hand, hold)
            rolled_dice = roller(5 - len(hold))
            turn_hand.extend(rolled_dice)
            return turn_hand
        else:
            raise Exception("Incorrect input, length of hand must be 5.")

def turn_sim(roll_counter, turn_hand):
    """
    Sims a full turn, up to the 3rd roll.

    Parameters
    __________

    roll_counter: integer, between 1 and  3. Represents the number 1 in the turn. i.e. if one roll has occurred, the next roll will be roll 2.

    turn_hand: list, Can be either blank or of length 5. the hand the algorithm is starting from. 

    Returns
    _______

    turn_hand: the resultant hand at the end of the turn. Same structure as in parameter, but no blanks.
    """
    if not 1 <= roll_counter <= 3:
        raise Exception("Incorrect input of the roll number.")
    else:
        while 1 <= roll_counter <= 3:
            turn_hand = roll_sim(turn_hand,random.choice(dice_choices))
            roll_counter += 1
        return turn_hand

def ten_thousand_round_firsthold_sim_value(roll_counter, turn_hand, first_hold):
    """
    Finds the expected value of the resultant hand from a specific first hold. Runs 10000 copies of one_round_hold_sim to accomplish this.

    Parameters
    __________

    roll_counter: integer, between 1 and  3. Represents the number 1 in the turn. i.e. if one roll has occurred, the next roll will be roll 2.
    
    turn_hand: list, Can be either blank or of length 5. the hand the algorithm is starting from. 

    first_hold: Defines the first hold of the turn sim, then used in the roll sim portion.

    Returns
    _______

    Average maximum value of every hand simmed.

    """
    
    value = 0
    for i in range(0, 10000):
        hand_value = hand_scorer(one_round_hold_sim(roll_counter, turn_hand, first_hold))
        value += hand_value
    return value / 10000

def one_round_hold_sim(roll_counter, turn_hand, first_hold):
    """
    Takes a specific first hold, then performs a turn_sim using that first hold.

    Parameters
    __________

    roll_counter: integer, between 1 and  3. Represents the number 1 in the turn. i.e. if one roll has occurred, the next roll will be roll 2.
    
    turn_hand: list, Can be either blank or of length 5. the hand the algorithm is starting from. 

    first_hold: Defines the first hold of the turn sim, then used in the roll sim portion.

    Returns
    _______

    turn_hand: list, Can be either blank or of length 5. Hand obtained at the end of the turn. 
    """
    if turn_hand == []:
        turn_hand = roller(5)
        roll_counter += 1
    else:
        if roll_counter == 1:
            roll_counter += 1
    turn_hand = roll_sim(turn_hand, first_hold)
    roll_counter += 1
    score = hand_scorer(turn_hand)
    if 1 < roll_counter <= 3:
        turn_hand = turn_sim(roll_counter, turn_hand)
    return turn_hand

def best_firsthold_value(roll_counter, test_hand):
    """
    Finds the first hold with the highest expected value for a given hand.

    Parameters
    __________

    roll_counter: integer, between 1 and  3. Represents the number 1 in the turn. i.e. if one roll has occurred, the next roll will be roll 2.
    
    test_hand: list, Can be either blank or of length 5. the hand the algorithm is starting from.

    Returns
    _______

    (best_average_score, best_hold) as a tuple, representing the best hold and the average score associated with it.
    
    """
    best_hold = []
    best_average_score = 0 
    if 1 <= roll_counter <= 3:
        for combination_hold in dice_choices:
            prospect_score = ten_thousand_round_firsthold_sim_value(roll_counter, test_hand, combination_hold)
            print(prospect_score, combination_hold)
            if prospect_score > best_average_score:
                best_average_score = prospect_score
                best_hold = combination_hold
        print(best_average_score, best_hold, "*")
        return best_average_score, best_hold

def three_of_a_kind_counter(current_hand_type, three_of_a_kind_numbers_of):
    """
    Iterates the given count of three of a kinds if the hand_type function returned true for it.

    Paramaters
    __________

    current_hand_type: list of boolean values of length 6, each representing the hand types.

    three_of_a_kind_numbers_of: integer, reprensents the three of a kinds obtained within the 10000 sims.

    Returns
    _______

    three_of_a_kind_numbers_of: same as in parameters, but iterated by 1 if true.
    
    """
    if current_hand_type[0] == True:
        three_of_a_kind_numbers_of += 1
    return three_of_a_kind_numbers_of

def four_of_a_kind_counter(current_hand_type, four_of_a_kind_numbers_of):
    """
    Iterates the given count of four of a kinds if the hand_type function returned true for it.

    Paramaters
    __________

    current_hand_type: list of boolean values of length 6, each representing the hand types.

    four_of_a_kind_numbers_of: integer, reprensents the four of a kinds obtained within the 10000 sims.

    Returns
    _______

    four_of_a_kind_numbers_of: same as in parameters, but iterated by 1 if true.
    
    """
    if current_hand_type[1] == True:
        four_of_a_kind_numbers_of += 1
    return four_of_a_kind_numbers_of

def full_house_counter(current_hand_type, full_house_numbers_of):
    """
    Iterates the given count of full houses if the hand_type function returned true for it.

    Paramaters
    __________

    current_hand_type: list of boolean values of length 6, each representing the hand types.

    full_house_numbers_of: integer, reprensents the full houses obtained within the 10000 sims.

    Returns
    _______

    full_house_numbers_of: same as in parameters, but iterated by 1 if true.
    
    """
    if current_hand_type[2] == True:
        full_house_numbers_of += 1
    return full_house_numbers_of

def yahtzee_counter(current_hand_type, yahtzee_numbers_of):
    """
    Iterates the given count of yahtzees if the hand_type function returned true for it.

    Paramaters
    __________

    current_hand_type: list of boolean values of length 6, each representing the hand types.

    yahtzee_numbers_of: integer, reprensents the yahtzees obtained within the 10000 sims.

    Returns
    _______

    yahtzee_numbers_of: same as in parameters, but iterated by 1 if true.
    
    """
    if current_hand_type[3] == True:
        yahtzee_numbers_of += 1
    return yahtzee_numbers_of

def small_straight_counter(current_hand_type, small_straight_numbers_of):
    """
    Iterates the given count of small straights if the hand_type function returned true for it.

    Paramaters
    __________

    current_hand_type: list of boolean values of length 6, each representing the hand types.

    small_straight_numbers_of: integer, reprensents the small straights obtained within the 10000 sims.

    Returns
    _______

    small_straight_numbers_of: same as in parameters, but iterated by 1 if true.
    
    """
    if current_hand_type[4] == True:
        small_straight_numbers_of += 1
    return small_straight_numbers_of

def large_straight_counter(current_hand_type, large_straight_numbers_of):
    """
    Iterates the given count of large straights if the hand_type function returned true for it.

    Paramaters
    __________

    current_hand_type: list of boolean values of length 6, each representing the hand types.

    large_straight_numbers_of: integer, reprensents the large straights obtained within the 10000 sims.

    Returns
    _______

    large_straight_of: same as in parameters, but iterated by 1 if true.
    
    """
    if current_hand_type[5] == True:
        large_straight_numbers_of += 1
    return large_straight_numbers_of

def firsthold_hand_types(roll_counter, turn_hand, first_hold):       
    """
    Finds the proportion of hands that achieve each hand type of the lower score card from a specific first hold. Runs 10000 copies of one_round_hold_sim to accomplish this.

    Parameters
    __________

    roll_counter: integer, between 1 and  3. Represents the number 1 in the turn. i.e. if one roll has occurred, the next roll will be roll 2.
    
    turn_hand: list, Can be either blank or of length 5. the hand the algorithm is starting from. 

    first_hold: Defines the first hold of the turn sim, then used in the roll sim portion.

    Returns
    _______

    Proportion of hands with each specific hand type as a tuple. (i.e. (three of a kinds, four of a kinds, full houses, yahtzees, small straights, large straights)).

    """
    three_of_a_kind_numbers_of = 0
    four_of_a_kind_numbers_of = 0
    full_house_numbers_of = 0
    yahtzee_numbers_of = 0
    small_straight_numbers_of = 0
    large_straight_numbers_of = 0
    for i in range(0, 10000):
        
        hand_types_obtained_in_sim = in_hand_hand_type(one_round_hold_sim(roll_counter, turn_hand, first_hold))
        
        three_of_a_kind_numbers_of = three_of_a_kind_counter(hand_types_obtained_in_sim, three_of_a_kind_numbers_of)
        
        four_of_a_kind_numbers_of = four_of_a_kind_counter(hand_types_obtained_in_sim, four_of_a_kind_numbers_of)
        
        full_house_numbers_of = full_house_counter(hand_types_obtained_in_sim, full_house_numbers_of)
        
        yahtzee_numbers_of = yahtzee_counter(hand_types_obtained_in_sim, yahtzee_numbers_of)
        
        small_straight_numbers_of = small_straight_counter(hand_types_obtained_in_sim, small_straight_numbers_of)
        
        large_straight_numbers_of = large_straight_counter(hand_types_obtained_in_sim, large_straight_numbers_of)
        
    return three_of_a_kind_numbers_of / 10000, four_of_a_kind_numbers_of / 10000,  full_house_numbers_of / 10000, yahtzee_numbers_of / 10000, small_straight_numbers_of / 10000, large_straight_numbers_of / 10000

def best_firsthold_hands(roll_counter, test_hand):
    """
    Finds the first hold with the highest probability of obtaining each lower hand type.

    Parameters
    __________

    roll_counter: integer, between 1 and 3. Represents the number 1 in the turn. i.e. if one roll has occurred, the next roll will be roll 2.
    
    test_hand: list, Can be either blank or of length 5. the hand the algorithm is starting from.

    Returns
    _______

    (best_probability, best_hold) as a tuple for each hand, in a list of length 6, representing the best hold and the probability associated with it.
    
    """
    best_holds = [(),(),(),(),(),()]
    best_hold_probability = [0,0,0,0,0,0]
    if 1 <= roll_counter <= 3:
        for combination_hold in dice_choices:
            prospect_score = firsthold_hand_types(roll_counter, test_hand, combination_hold)
            for i in range(6):
                if prospect_score[i] > best_hold_probability[i]:
                    best_hold_probability[i] = prospect_score[i]
                    best_holds[i] = combination_hold
        return [(best_hold_probability[i], best_holds[i]) for i in range(6)]
