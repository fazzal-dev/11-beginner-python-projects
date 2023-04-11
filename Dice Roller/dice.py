from random import *
from dice_visuals import *


def parse_input(input_string):

    if input_string.strip() in {"1", "2", "3", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number between 1 and 6. ")
        raise SystemExit(1)


def roll_dice(num_dice):

    roll_result = []
    for _ in range(num_dice):
        roll = randint(1, 6)
        roll_result.append(roll)

    return roll_result


def generate_dice_face_diagram(dice_values):
    # Generate a list of dice faces from DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

     # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header]+dice_faces_rows)
    return dice_faces_diagram


num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
