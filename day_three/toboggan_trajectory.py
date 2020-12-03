""" Day three of the advent of code 2020."""

INPUT_FILE = "input.txt"
X_MOVE = 3
Y_MOVE = 1
X_MOVE_LIST = [1,3,5,7,1]
Y_MOVE_LIST = [1,1,1,1,2]

def fetch_input_as_list():
    """Testing fetching the list all at once."""
    try:
        file_content = open(INPUT_FILE, "r")
        lines = file_content.read().splitlines()
        return lines
    except Exception as ex:
        print(f"Issue reading input from file: {ex}")
        raise ValueError("Issue reading input from file.")


def calculate_wrap_move(position, step, max_pos):
    """Calculate the x position, if over the length."""
    return (position+step) - (max_pos) -1


def run_part_one():
    """Runner for logic for part one of the problem."""
    rows = fetch_input_as_list()
    x_pos = 0
    y_pos = 0
    tree_count = 0

    for row in rows:
        if row[x_pos] == '#':
            tree_count+=1

        if x_pos + X_MOVE > len(row)-1:
            x_pos = calculate_wrap_move(x_pos, X_MOVE, len(row)-1)
        else:
            x_pos += X_MOVE
        y_pos+=1

    return tree_count


if __name__ == "__main__":
    p1_ans = run_part_one()
    print(p1_ans)