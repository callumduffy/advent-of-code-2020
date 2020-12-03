""" Day three of the advent of code 2020."""

INPUT_FILE = "input.txt"

I_MOVE = 1
J_MOVE = 3

I_MOVE_LIST = [1,1,1,1,2]
J_MOVE_LIST = [1,3,5,7,1]

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


def ride_that_toboggan_bro(i_step, j_step, tree_list):
    """Iterate over each line and check if a tree."""
    i_pos = 0
    j_pos = 0
    tree_count = 0
    row_count = len(tree_list)

    while i_pos < row_count:
        max_j = len(tree_list[i_pos])-1

        if tree_list[i_pos][j_pos] == '#':
            tree_count+=1

        if j_pos + j_step > max_j:
            j_pos = calculate_wrap_move(j_pos, j_step, max_j)
        else:
            j_pos += j_step
        i_pos+=i_step
    return tree_count


if __name__ == "__main__":
    toboggan_journey = fetch_input_as_list()
    p1_ans = ride_that_toboggan_bro(I_MOVE, J_MOVE, toboggan_journey)
    print(f"Part one: {p1_ans}")

    p2_ans = 0
    i = 0

    while i < len(I_MOVE_LIST):
        trees_hit = ride_that_toboggan_bro(I_MOVE_LIST[i], J_MOVE_LIST[i], toboggan_journey)
        if i ==0:
            p2_ans += trees_hit
        else:
            p2_ans *= trees_hit
        i+=1

    print(f"Part two: {p2_ans}")