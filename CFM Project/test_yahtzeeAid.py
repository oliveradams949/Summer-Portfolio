import yahtzeeAid as yhtz
import itertools
import random
import pytest


def test_roller():
    """
    Tests the roller function
    
    """
    random.seed(0)
    assert yhtz.roller(5) == [4, 4, 1, 3, 5], "The 0 seed did not give the expected result"
    random.seed(1)
    assert yhtz.roller(5) == [2, 5, 1, 3, 1], "The 1 seed did not give the expected result"
    random.seed(2)
    assert yhtz.roller(5) == [1, 1, 1, 3, 2], "The 2 seed did not give the expected result"
    random.seed(3)
    assert yhtz.roller(5) == [2, 5, 5, 2, 3], "The 3 seed did not give the expected result"
    random.seed(0)
    samples = [yhtz.roller(1)[0] for repetition in range(1000)]
    all_values = {1, 2, 3, 4, 5, 6}
    assert set(samples) == all_values, "Not all values have been obtained over 1000 repetitions"

test_roller()

def test_number_checker():
    """
    Tests the number_checker function
    """
    random.seed(0)
    assert yhtz.number_checker(yhtz.roller(5)) == [1, 0, 1, 2, 1, 0], "The 0 seed did not give the expected result"
    random.seed(1)
    assert yhtz.number_checker(yhtz.roller(5)) == [2, 1, 1, 0, 1, 0], "The 1 seed did not give the expected result"
    random.seed(2)
    assert yhtz.number_checker(yhtz.roller(5)) == [3, 1, 1, 0, 0, 0], "The 2 seed did not give the expected result"
    random.seed(3)
    assert yhtz.number_checker(yhtz.roller(5)) == [0, 2, 1, 0, 2, 0], "The 3 seed did not give the expected result"

test_number_checker()

def test_true_or_false_scorecard_game_setup(turn, lower_achieved, upper_achieved):
    """
    Runs through every hand in the handTypes class, and depending on if the corresponding value in lower_achieved or upper_achieved was a 1 or a 0,
    checks that said hand has been assigned the correct value.
    """
    yhtz.game_setup(turn, lower_achieved, upper_achieved)
    attrs = [attr for attr in vars(yhtz.hand_types) if not attr.startswith("__")]
    count = 0
    for attr in attrs:
        value = getattr(yhtz.hand_types, attr)
        if count < 7:
            expected = lower_achieved[count] == 1
        else:
            expected = upper_achieved[count-7] == 1
        assert value == expected, attr + " achieved is " + str(value) +" when it should be " + str(expected) + "."
        count += 1

def test_game_setup_correct_sample_doesnt_error():

    """
    tests game_setup() for correct inputs using test_true_or_false_scorecard_game_setup.
    """
    
    test_true_or_false_scorecard_game_setup(1, [0,0,0,0,0,0,0], [0,0,0,0,0,0])
    test_true_or_false_scorecard_game_setup(13, [0,0,0,0,0,0,0], [0,0,0,0,0,0])

    test_true_or_false_scorecard_game_setup(1, [1,1,1,1,1,1,1], [0,0,0,0,0,0])
    test_true_or_false_scorecard_game_setup(1, [1,1,1,1,1,1,1], [1,1,1,1,1,1])
    test_true_or_false_scorecard_game_setup(1, [0,0,0,0,0,0,0], [1,1,1,1,1,1])

test_game_setup_correct_sample_doesnt_error()

def test_game_setup_exceptions():

    """
    Tests game_setup for every type of exception.
    """

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(100, [0,0,0,0,0,0,0], [0,0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input of the turns.", "Exception for incorrect turn input above does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(14, [0,0,0,0,0,0,0], [0,0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input of the turns.", "Exception for incorrect turn input above does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(0, [0,0,0,0,0,0,0], [0,0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input of the turns.", "Exception for incorrect turn input below does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(-100, [0,0,0,0,0,0,0], [0,0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input of the turns.", "Exception for incorrect turn input below does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(1, [0,0,0,0,0,0], [0,0,0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input length of lower/upper hands.", "Exception for incorrect length of upper or lower hands input does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(1, [0,0,0,0,0,0,0,0], [0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input length of lower/upper hands.", "Exception for incorrect length of upper or lower hands input does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(1, [0], [0,0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input length of lower/upper hands.", "Exception for incorrect length of upper or lower hands input does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(1, [0,0,0,0,0,0,0], [0])
    assert exc_info.value.args[0] == "Incorrect input length of lower/upper hands.", "Exception for incorrect length of upper or lower hands input does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(1, [2,0,0,0,0,0,0], [0,0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input of lower hands.", "Exception for incorrect length of upper or lower hands input does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(1, [0,0,0,0,0,0,0], [2,0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input of lower hands.", "Exception for incorrect length of upper or lower hands input does not return the expected result"
 
    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(1, [-1,0,0,0,0,0,0], [0,0,0,0,0,0])
    assert exc_info.value.args[0] == "Incorrect input of lower hands.", "Exception for incorrect length of upper or lower hands input does not return the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.game_setup(1, [2,2,2,2,2,2,2], [2,2,2,2,2,2])
    assert exc_info.value.args[0] == "Incorrect input of lower hands.", "Exception for incorrect length of upper or lower hands input does not return the expected result"

test_game_setup_exceptions()

def test_simmed_hand_holder_correct_sample_doesnt_error():

    """
    Tests that simmed_hand_holder works as intended for correct inputs.
    """

    random.seed(0)
    assert yhtz.simmed_hand_holder(yhtz.roller(5), random.choice(yhtz.dice_choices)) == [], "The 0 seed did not give the expected result"

    random.seed(3)
    assert yhtz.simmed_hand_holder(yhtz.roller(5), random.choice(yhtz.dice_choices)) == [2, 2, 3, 5, 5], "The 3 seed did not give the expected result"

    random.seed(2)
    assert yhtz.simmed_hand_holder(yhtz.roller(5), random.choice(yhtz.dice_choices)) == [1, 1, 2], "The 2 seed did not give the expected result"

test_simmed_hand_holder_correct_sample_doesnt_error()

def test_simmed_hand_holder_exceptions():

    """
    Tests simmed_hand_holders exceptions.
    """
    list = [1,2,3,4,5]

    random.seed(0)
    with pytest.raises(Exception) as exc_info:
        yhtz.simmed_hand_holder(yhtz.roller(5), [7])
    assert exc_info.value.args[0] == "Incorrect input of numbers, number not in range.", "The exception for above range does not give the expected result"

    random.seed(1)
    with pytest.raises(Exception) as exc_info:
        yhtz.simmed_hand_holder(yhtz.roller(5), [100])
    assert exc_info.value.args[0] == "Incorrect input of numbers, number not in range.", "The exception for above range does not give the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.simmed_hand_holder(yhtz.roller(5), [6])
    assert exc_info.value.args[0] == "Incorrect input of numbers, number not in range.", "The exception for one above maximum does not give the expected result"

    random.seed(0)
    with pytest.raises(Exception) as exc_info:
        yhtz.simmed_hand_holder(yhtz.roller(5), [-1])
    assert exc_info.value.args[0] == "Incorrect input of numbers, number not in range.", "The exception for below range does not give the expected result"

    random.seed(1)
    with pytest.raises(Exception) as exc_info:
        yhtz.simmed_hand_holder(yhtz.roller(5), [-100])
    assert exc_info.value.args[0] == "Incorrect input of numbers, number not in range.", "The exception for below range does not give the expected result"

    random.seed(0)
    with pytest.raises(Exception) as exc_info:
        yhtz.simmed_hand_holder(yhtz.roller(5), [1,1,1,1,1])
    assert exc_info.value.args[0] == "Incorrect input of numbers, duplicates."   

    with pytest.raises(Exception) as exc_info:
        yhtz.simmed_hand_holder(yhtz.roller(5), [5,5])
    assert exc_info.value.args[0] == "Incorrect input of numbers, duplicates."

    random.seed(1)
    with pytest.raises(Exception) as exc_info:
        yhtz.simmed_hand_holder(yhtz.roller(5), [1,1,1,1,1])
    assert exc_info.value.args[0] == "Incorrect input of numbers, duplicates."   

    with pytest.raises(Exception) as exc_info:
        yhtz.simmed_hand_holder(yhtz.roller(5), [5,5])
    assert exc_info.value.args[0] == "Incorrect input of numbers, duplicates."

test_simmed_hand_holder_exceptions()

def test_hand_scorer_correct_sample_doesnt_error():

    """
    Test hand_scorer for correct samples.
    """

    assert yhtz.hand_scorer([1,2,3,4,5]) == 40, "The Large Straight turn 1 is does not give the expected result."

    assert yhtz.hand_scorer([5,5,5,4,4]) == 25, "The Full House turn 1 does not give the expected result"

    assert yhtz.hand_scorer([6,6,6,5,5]) == 28, "The Full House when Three of a Kind is higher does not give the expected result"

    yhtz.game_setup(1, [1,0,0,0,0,0,1], [1,1,1,1,1,1])
    assert yhtz.hand_scorer([6,6,6,5,5]) == 25, "The Full House when Three of a Kind is higher but already achieved does not give the expected result"

    yhtz.game_setup(1, [0,0,1,0,0,0,0], [1,1,1,1,1,1])    
    assert yhtz.hand_scorer([5,5,5,4,4]) == 23, "The Full House turn 1 when already achieved and Three of a Kind not does not give the expected result"

    yhtz.game_setup(1,[0,0,0,0,0,1,0],[0,0,0,0,0,0])
    assert yhtz.hand_scorer([1,2,3,4,5]) == 30, "The Large Straight when Large straight is already achieved does not give the expected result."

    yhtz.game_setup(1,[0,0,0,0,1,1,0],[0,0,0,0,0,0])
    assert yhtz.hand_scorer([1,2,3,4,5]) == 15,  "The Large Straight when both straights have been obtained does not give the expected result"

    yhtz.game_setup(1, [0,0,0,0,1,1,1], [0,0,0,0,0,0])
    assert yhtz.hand_scorer([1,2,3,4,5]) == 5, "The Large Straight with no available lower hand is not scoring correctly"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,1,1,1,1,1])
    assert yhtz.hand_scorer([1,2,3,4,5])==0, "The hand with no available upper or lower does not give the expected result"

    yhtz.game_setup(1, [0,0,0,0,0,0,0], [0,0,0,0,0,0])
    assert yhtz.hand_scorer([6,6,6,6,6]) == 50, "First Yahtzee score does not return the expected result"

    yhtz.game_setup(1, [0,0,0,1,0,0,0], [0,0,0,0,0,0])
    assert yhtz.hand_scorer([6,6,6,6,6]) == 100, "Second Yahtzee score does not return the expected result"

    yhtz.game_setup(1, [0,0,0,0,0,0,1], [0,0,0,0,0,0])
    assert yhtz.hand_scorer([6,6,6,6,1]) == 25, "Four of a Kind with no Chance does not return the expected result"

    yhtz.game_setup(1, [0,1,0,0,0,0,1], [0,0,0,0,0,0])
    assert yhtz.hand_scorer([6,6,6,6,1]) == 25, "Four of a Kind Achieved with no Chance does not return the expected result"

    yhtz.game_setup(1, [1,1,0,0,0,0,1], [0,0,0,0,0,0])
    assert yhtz.hand_scorer([6,6,6,6,1]) == 24, "Four and Three of a Kind Achieved with no Chance does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,0,1,1,1,1])
    assert yhtz.hand_scorer([1,2,3,4,5]) ==  2, "Only twos available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,0,1,1,1,1])
    assert yhtz.hand_scorer([1,2,2,4,5]) ==  4, "Only twos (2) available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,1,0,1,1,1])
    assert yhtz.hand_scorer([1,2,3,4,5]) ==  3, "Only threes available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,1,0,1,1,1])
    assert yhtz.hand_scorer([1,2,3,3,5]) ==  6, "Only threes (2) available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,1,1,0,1,1])
    assert yhtz.hand_scorer([1,2,3,4,5]) ==  4, "Only fours available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,1,1,0,1,1])
    assert yhtz.hand_scorer([1,2,3,4,4]) ==  8, "Only fours (2) available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,1,1,1,0,1])
    assert yhtz.hand_scorer([1,2,3,4,5]) ==  5, "Only fives available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,1,1,1,0,1])
    assert yhtz.hand_scorer([1,2,3,5,5]) ==  10, "Only fives (2) available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,1,1,1,1,0])
    assert yhtz.hand_scorer([1,2,3,4,6]) ==  6, "Only sixes available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [1,1,1,1,1,0])
    assert yhtz.hand_scorer([1,2,3,6,6]) ==  12, "Only sixes (2) available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [0,1,1,1,1,1])
    assert yhtz.hand_scorer([1,2,3,4,5]) ==  1, "Only ones available does not return the expected result"

    yhtz.game_setup(1,[1,1,1,1,1,1,1], [0,1,1,1,1,1])
    assert yhtz.hand_scorer([1,1,3,4,5]) ==  2, "Only ones (1) available does not return the expected result"

test_hand_scorer_correct_sample_doesnt_error()

def test_in_hand_hand_type():

    """
    Tests in_hand_hand_type.
    """

    hand_held=yhtz.in_hand_hand_type([1,2,3,4,5])
    assert hand_held[4] and hand_held[5] == True, "Large straight does not return the expected result"

    hand_held=yhtz.in_hand_hand_type([1,2,3,4,4])
    assert hand_held[4] == True, "Small straight does not return the expected result"

    hand_held=yhtz.in_hand_hand_type([4,4,4,4,4])
    assert hand_held[3] == True, "Yahtzee does not return the expected result"

    hand_held=yhtz.in_hand_hand_type([1,1,1,2,2])
    assert hand_held[0] == True and hand_held[2] == True, "Full House does not return the expected result"

    hand_held=yhtz.in_hand_hand_type([4,4,4,4,1])
    assert hand_held[0] == True and hand_held[1] == True, "Four of a Kind does not return the expected result"

    hand_held=yhtz.in_hand_hand_type([4,4,4,1,2])
    assert hand_held[0] == True, "Three of a Kind does not return the expected result"

test_in_hand_hand_type()

def test_roll_sim_exceptions():

    """
    Tests roll_sims exceptions.
    """

    with pytest.raises(Exception) as exc_info:
        yhtz.roll_sim([1], [1])
    assert exc_info.value.args[0] == "Incorrect input, length of hand must be 5.", "The exception for above range does not give the expected result"

    with pytest.raises(Exception) as exc_info:
        yhtz.roll_sim([1,1,1,1,1,1], [1])
    assert exc_info.value.args[0] == "Incorrect input, length of hand must be 5.", "The exception for above range does not give the expected result"

test_roll_sim_exceptions()

def test_roll_sim_correct_sample_doesnt_error():

    """
    Tests roll_sim for correct inputs.
    """

    random.seed(0)
    held_hand=yhtz.roll_sim([1,2,3,4,5], [1,2,3])
    assert held_hand[0:3] == [1,2,3], "Roll sim seed 0 not giving expected result"

    random.seed(1)
    held_hand=yhtz.roll_sim([1,2,3,4,5], [1,2,3])
    assert held_hand[0:3] == [1,2,3], "Roll sim seed 1 not giving expected result"

    random.seed(0)
    held_hand=yhtz.roll_sim([1,2,3,4,5], [3,4,5])
    assert held_hand[0:3] == [3,4,5], "Roll sim seed 0 not giving expected result"

    random.seed(1)
    held_hand=yhtz.roll_sim([1,2,3,4,5], [3,4,5])
    assert held_hand[0:3] == [3,4,5], "Roll sim seed 1 not giving expected result"

    random.seed(0)
    held_hand=yhtz.roll_sim([1,2,4,5,6], [1,3,5])
    assert held_hand[0:3] == [1,4,6], "Roll sim seed 0 not giving expected result"

    random.seed(1)
    held_hand=yhtz.roll_sim([1,2,4,5,6], [1,3,5])
    assert held_hand[0:3] == [1,4,6], "Roll sim seed 1 not giving expected result"

    random.seed(0)
    held_hand=yhtz.roll_sim([1,2,4,5,6], [2,4,5])
    assert held_hand[0:3] == [2,5,6], "Roll sim seed 0 not giving expected result"

    random.seed(1)
    held_hand=yhtz.roll_sim([1,2,4,5,6], [2,4,5])
    assert held_hand[0:3] == [2,5,6], "Roll sim seed 1 not giving expected result"

test_roll_sim_correct_sample_doesnt_error()

def test_turn_sim_exceptions():

    """
    Tests turn_sim for exceptions.
    """

    with pytest.raises(Exception) as exc_info:
        yhtz.turn_sim(0, [1,2,3,4,5])
    assert exc_info.value.args[0] == "Incorrect input of the roll number.", "The exception for above range does not give the expected result"    

    with pytest.raises(Exception) as exc_info:
        yhtz.turn_sim(4, [1,2,3,4,5])
    assert exc_info.value.args[0] == "Incorrect input of the roll number.", "The exception for above range does not give the expected result" 

    with pytest.raises(Exception) as exc_info:
        yhtz.turn_sim(100, [1,2,3,4,5])
    assert exc_info.value.args[0] == "Incorrect input of the roll number.", "The exception for above range does not give the expected result" 

    with pytest.raises(Exception) as exc_info:
        yhtz.turn_sim(-100, [1,2,3,4,5])
    assert exc_info.value.args[0] == "Incorrect input of the roll number.", "The exception for above range does not give the expected result" 

test_turn_sim_exceptions()

def test_turn_sim_correct_sample_doesnt_error():

    """
    Tests turn_sim for correct inputs.
    """

    random.seed(0)
    turn_hand=yhtz.turn_sim(1,[])
    assert len(turn_hand) == 5, "The length of the returned hand does not give the expected result"

    random.seed(1)
    turn_hand=yhtz.turn_sim(1,[])
    assert len(turn_hand) == 5, "The length of the returned hand does not give the expected result"

    random.seed(2)
    turn_hand=yhtz.turn_sim(1,[])
    assert len(turn_hand) == 5, "The length of the returned hand does not give the expected result"

    samples=[yhtz.turn_sim(1,[]) for repetition in range(100000)]
    all_values=list(itertools.combinations_with_replacement(range(1,7), 5))
    samples = sorted({tuple(sorted(x)) for x in samples})
    samples = sorted(set(map(tuple, samples)))

    assert all_values == samples, "Not all values have been obtained over 1000 repetitions"

test_turn_sim_correct_sample_doesnt_error()

def test_one_round_hold_sim():
    """
    Tests that the first roll within the one_round_hold_sim is applied correctly. Other tests are equivalent to the turn_sim().
    """
    random.seed(0)
    one_hand=yhtz.one_round_hold_sim(3, [2,2,2,4,5], [1,2,3])
    one_hold=yhtz.roll_sim([2,2,2,4,5], [1,2,3])
    assert one_hand[0:3] == one_hold[0:3], "The 0 seed does not give the expected result"

    random.seed(1)
    one_hand=yhtz.one_round_hold_sim(3, [2,2,2,4,5], [1,2,3])
    one_hold=yhtz.roll_sim([2,2,2,4,5], [1,2,3])
    assert one_hand[0:3] == one_hold[0:3], "The 1 seed does not give the expected result"

    random.seed(1)
    one_hand=yhtz.one_round_hold_sim(3, [2,2,2,4,5], [1,2,3])
    one_hold=yhtz.roll_sim([2,2,2,4,5], [1,2,3])
    assert one_hand[0:3] == one_hold[0:3], "The 1 seed does not give the expected result"

test_one_round_hold_sim()

def test_ten_thousand_round_firsthold_sim_value():
    """
    Tests the ten_thousand_round_firsthold_sim_value function. Only tests at roll_counter=3 as any other roll counter is too unpredictable.
    """
    yhtz.game_setup(1,[0,0,0,0,0,0,0], [0,0,0,0,0,0])

    random.seed(0)
    value=yhtz.ten_thousand_round_firsthold_sim_value(3, [1,2,3,4,4], [1,2,3,4])
    assert abs((value - 31.6)/ value)<=0.01, "The 0 seed does not give the expected result"

    random.seed(1)
    value=yhtz.ten_thousand_round_firsthold_sim_value(3, [1,2,3,4,4], [1,2,3,4])
    assert abs((value - 31.6)/ value)<=0.01, "The 1 seed does not give the expected result"

    random.seed(2)
    value=yhtz.ten_thousand_round_firsthold_sim_value(3, [1,2,3,4,4], [1,2,3,4])
    assert abs((value - 31.6)/ value)<=0.01, "The 2 seed does not give the expected result"

test_ten_thousand_round_firsthold_sim_value()

def test_best_firsthold_value():

    """
    Tests best_firsthold_value.
    """

    yhtz.game_setup(1,[0,0,0,0,0,0,0], [0,0,0,0,0,0])

    random.seed(0)
    value=yhtz.best_firsthold_value(3, [1,2,3,4,6])
    assert value[0] == 31.636, "The 0 seed does not give the expected result."
    assert value[1] == (1,2,3,4), "The 0 seed does not give the expected result."

    random.seed(1)
    value=yhtz.best_firsthold_value(3, [1,2,3,4,6])
    assert value[0] == 31.631, "The 1 seed does not give the expected result."
    assert value[1] == (1,2,3,4), "The 1 seed does not give the expected resul.t"

    random.seed(2)
    value=yhtz.best_firsthold_value(3, [1,2,3,4,6])
    assert value[0] == 31.663
    assert value[1] == (1,2,3,4), "The 2 seed does not give the expected result."

    random.seed(0)
    value=yhtz.best_firsthold_value(2, yhtz.roller(5))
    assert value[0] == 22.1055, "The 0 seed general does not give the expected result."
    assert value[1] == (1,2,4,5), "The 0 seed general does not give the expected result."

    random.seed(1)
    value=yhtz.best_firsthold_value(2, yhtz.roller(5))
    assert value[0] == 20.7765, "The 1 seed general does not give the expected result."
    assert value[1] == (2, 4), "The 1 seed general does not give the expected result."

    random.seed(2)
    value=yhtz.best_firsthold_value(2, yhtz.roller(5))
    assert value[0] == 20.2469, "The 2 seed general does not give the expected result."
    assert value[1] == (4,), "The 2 seed general does not give the expected result."

test_best_firsthold_value()

def test_three_of_a_kind_counter():

    """
    Tests three_of_a_kind_counter.
    """

    current_hand_type=yhtz.in_hand_hand_type([1,1,1,2,3])
    assert yhtz.three_of_a_kind_counter(current_hand_type, 0) == 1, "Three of a kind True does not return the expected result"

    current_hand_type=yhtz.in_hand_hand_type([1,1,2,2,3])
    assert yhtz.three_of_a_kind_counter(current_hand_type, 0) == 0, "Three of a kind False does not return the expected result"

test_three_of_a_kind_counter()

def test_four_of_a_kind_counter():
    
    """
    Tests fours_of_a_kind_counter.
    """

    current_hand_type=yhtz.in_hand_hand_type([1,1,1,1,3])
    assert yhtz.four_of_a_kind_counter(current_hand_type, 0) == 1, "Four of a kind True does not return the expected result"

    current_hand_type=yhtz.in_hand_hand_type([1,1,2,2,3])
    assert yhtz.four_of_a_kind_counter(current_hand_type, 0) == 0, "Four of a kind False does not return the expected result"

test_four_of_a_kind_counter()

def test_yahtzee_counter():

    """
    Tests yahtzee_counter.
    """

    current_hand_type=yhtz.in_hand_hand_type([1,1,1,1,1])
    assert yhtz.yahtzee_counter(current_hand_type, 0) == 1, "Yahtzee True does not return the expected result"

    current_hand_type=yhtz.in_hand_hand_type([1,1,2,2,3])
    assert yhtz.yahtzee_counter(current_hand_type, 0) == 0, "Yahtzee False does not return the expected result"

test_yahtzee_counter()

def test_full_house_counter():

    """
    Tests full_house_counter.
    """

    current_hand_type=yhtz.in_hand_hand_type([1,1,2,2,2])
    assert yhtz.full_house_counter(current_hand_type, 0) == 1, "Full House True does not return the expected result"

    current_hand_type=yhtz.in_hand_hand_type([1,1,2,2,3])
    assert yhtz.full_house_counter(current_hand_type, 0) == 0, "Full House False does not return the expected result"

test_full_house_counter()

def test_small_straight_counter():

    """
    Tests small_straight_counter.
    """

    current_hand_type=yhtz.in_hand_hand_type([1,2,3,4,4])
    assert yhtz.small_straight_counter(current_hand_type, 0) == 1, "Small Straight True does not return the expected result"

    current_hand_type=yhtz.in_hand_hand_type([1,1,2,2,3])
    assert yhtz.small_straight_counter(current_hand_type, 0) == 0, "Small Straight False does not return the expected result"

test_small_straight_counter()

def test_large_straight_counter():

    """
    Tests large_straight_counter.
    """

    current_hand_type=yhtz.in_hand_hand_type([1,2,3,4,5])
    assert yhtz.large_straight_counter(current_hand_type, 0) == 1, "Large Straight True does not return the expected result"

    current_hand_type=yhtz.in_hand_hand_type([1,1,2,2,3])
    assert yhtz.large_straight_counter(current_hand_type, 0) == 0, "Large Straight False does not return the expected result"

test_large_straight_counter()

def test_firsthold_hand_types_large_straights():

    """
    Tests firsthold_hand_types specifically for large straights, and on roll 3.
    """

    random.seed(0)

    hand_types_simmed=yhtz.firsthold_hand_types(3,[1,2,3,4,5], [1,2,3,4,5])
    assert hand_types_simmed[4] == 1, "The large (small straights) straights have not returned the expected result"
    assert hand_types_simmed[5] == 1, "The large straights have not returned the expected result"

test_firsthold_hand_types_large_straights()

def test_firsthold_hand_types_small_straights():

    """
    Tests firsthold_hand_types specifically for small straights, and on roll 3.
    """

    random.seed(0)

    hand_types_simmed=yhtz.firsthold_hand_types(3,[1,2,3,4,4], [1,2,3,4])
    assert hand_types_simmed[4] == 1, "The small straights have not returned the expected result"

test_firsthold_hand_types_small_straights()

def test_firsthold_hand_types_full_houses():

    """
    Tests firsthold_hand_types specifically for full houses, and on roll 3.
    """

    random.seed(0)

    hand_types_simmed=yhtz.firsthold_hand_types(3,[1,1,1,2,2], [1,2,3,4,5])
    assert hand_types_simmed[0] == 1, "The full houses (three of a Kinds) have not returned the expected result"
    assert hand_types_simmed[2] == 1, "The full houses have not returned the expected result"

test_firsthold_hand_types_full_houses()

def test_firsthold_hand_types_three_of_a_kind():

    """
    Tests firsthold_hand_types specifically for three of a kind, and on roll 3.
    """

    random.seed(0)

    hand_types_simmed=yhtz.firsthold_hand_types(3,[1,1,1,2,3], [1,2,3])
    assert hand_types_simmed[0] == 1, "The three of a kinds have not returned the expected result"

test_firsthold_hand_types_three_of_a_kind()

def test_firsthold_hand_types_four_of_a_kind():

    """
    Tests firsthold_hand_types specifically for four of a kind, and on roll 3.
    """

    random.seed(0)

    hand_types_simmed=yhtz.firsthold_hand_types(3,[1,1,1,1,2], [1,2,3,4])
    assert hand_types_simmed[1] == 1, "The four of a kinds have not returned the expected result"

test_firsthold_hand_types_four_of_a_kind()

def test_firsthold_hand_types_yahtzees():

    """
    Tests firsthold_hand_types specifically for yahtzees, and on roll 3.
    """

    random.seed(0)

    hand_types_simmed=yhtz.firsthold_hand_types(3,[4,4,4,4,4], [1,2,3,4,5])
    assert hand_types_simmed[3] == 1, "The yahtzees have not returned the expected result"

test_firsthold_hand_types_yahtzees()

def test_firsthold_hand_types_general():

    """
    Tests firsthold_hand_types for a general randomised case.
    """

    random.seed(0)

    assert yhtz.firsthold_hand_types(2,yhtz.roller(5),random.choice(yhtz.dice_choices)) == (0.2099, 0.0157, 0.0386, 0.0003, 0.1561, 0.0323), "The 0 seed does not give the expected result."

    random.seed(1)

    assert yhtz.firsthold_hand_types(2,yhtz.roller(5),random.choice(yhtz.dice_choices)) == (0.2098, 0.0222, 0.0376, 0.0012, 0.1613, 0.031), "The 1 seed does not give the expected result."

    random.seed(2)

    assert yhtz.firsthold_hand_types(2,yhtz.roller(5),random.choice(yhtz.dice_choices)) == (0.2451, 0.0247, 0.0465, 0.001, 0.1084, 0.0224), "The 2 seed does not give the expected result."

test_firsthold_hand_types_general()

def test_best_firsthold_hands():

    """
    Tests the best_firsthold_hands function.
    """
    
    random.seed(0)

    assert yhtz.best_firsthold_hands(2, yhtz.roller(5)) == [(0.2749, (1, 2)), (0.0311, (1, 2)), (0.0561, (1, 2)), (0.0018, (1, 2)), (0.2668, (1, 4, 5)), (0.0575, (2, 3, 4, 5))], "The 0 seed does not return the expected result."

    random.seed(1)

    assert yhtz.best_firsthold_hands(2, yhtz.roller(5)) == [(0.2726, (3, 5)), (0.0338, (3, 5)), (0.0561, (3, 4, 5)), (0.0022, (3, 5)), (0.1995, (1, 2, 4)), (0.055, (1, 2, 4, 5))], "The 1 seed does not return the expected result."

    random.seed(2)

    assert yhtz.best_firsthold_hands(2, yhtz.roller(5)) == [(0.3971, (1, 2, 3)), (0.077, (1, 2, 3)), (0.0714, (1, 2, 3, 5)), (0.0059, (1, 2, 3)), (0.19, (4, 5)), (0.0398, (4, 5))], "The 2 seed does not return the expected result."

test_best_firsthold_hands()
