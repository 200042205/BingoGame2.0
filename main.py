from pyscript import document
import card_matrix
import random

# this array store all possible number the caller can call, and should be shuffled during reset
all_bingo_numbers = []
# this array stores the numbers that have been called this game.
called_numbers = []
#this array stores the 25 numbers generated for the bingo card
card_numbers = []

# EVENTS
def reset_game(event):
    print("calling 'reset_game'")
    #complete me
    generate_card()
    shuffle_caller()
    reset_calls()
    document.querySelector("#current_call").innerHTML = " "
    document.querySelector("#win_game").close()


def check_cell(event):
    print("calling 'check_cell'")
    # use event to get the cell id that
    # was clicked and it's value
    cell_id = event.target.id
    cell_val = int(event.target.innerHTML)

    # complete me
    coords = cell_id.split("_")[1:]
    x = int(coords[0])
    y = int(coords[1])
    print(x)
    print(y)

    if cell_val in called_numbers and not card_matrix.is_position_marked(x, y):
        highlight_card_cell("#" + cell_id)
        if card_matrix.mark_position(x, y):
            document.querySelector("#win_game").showModal()


def call_next(event):
    global all_bingo_numbers
    print("calling 'call_next'")

    #complete me
    if len(all_bingo_numbers) > 0:
        next_number = all_bingo_numbers.pop(0) # Remove and return the first number in the list
        document.querySelector("#current_call").innerHTML = next_number
        add_called(next_number)
    else:
        document.querySelector("#current_call").innerHTML = "No more numbers left to call."

# INTERNAL FUNCTIONS
def shuffle_caller():
    global all_bingo_numbers
    print("Calling 'shuffle_caller'")

    # complete me
    all_bingo_numbers = list(range(1, 76))
    random.shuffle(all_bingo_numbers)
    for x in all_bingo_numbers:
        id = f"#cell_{x}"
        reset_caller_cell(id)


def reset_calls():
    global called_numbers
    print("Calling 'reset_calls'")

    # complete me
    called_numbers.clear()
    document.querySelector("#called_numbers").innerHTML = " "


def generate_card():
    global card_numbers
    print("Calling 'generate_card'")

    # complete me
    card_numbers = (list(range(1,76)))
    random.shuffle(card_numbers)
    card_numbers = card_numbers[:25]

    for x in range(1,6):
        for y in range(1,6):
            id = "#cell_" + str(x) + "_" + str(y)
            document.querySelector(id).innerHTML = str(card_numbers.pop())
            reset_card_cell(id)





def add_called(num):
    global called_numbers
    print("Calling 'add_called'")

    # complete me + use the join functino in python
    called_numbers.append(num)
    highlight_caller_cell(f"#cell_{num}")
    document.querySelector("#called_numbers").innerHTML = ", ".join(str(x) for x in called_numbers)


# adds/removes highlight CSS classes from cells (these are complete, don't change)
def highlight_card_cell(cell_id):
    document.querySelector(cell_id).className += "highlight-card"


def reset_card_cell(cell_id):
    document.querySelector(cell_id).className = ""


def highlight_caller_cell(cell_id):
    document.querySelector(cell_id).className += "highlight-caller"


def reset_caller_cell(cell_id):
    document.querySelector(cell_id).className = ""


# initial setup
reset_game(0)
