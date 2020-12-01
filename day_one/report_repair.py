""" Day one of the advent of code 2020."""

def fetch_input_as_list(file_name):
    """Read the input from file, pity no API for this."""
    try:
        file_content = open(file_name, "r")
        return [int(x) for x in file_content.read().split('\n')]
    except:
        print("Issue reading input from file.")
        raise ValueError("Issue reading input from file.")


def simple_solve(file_name):
    """Solve the problem the old fashioned way, slow as hell."""
    input_list = fetch_input_as_list("day_one.txt")

    for i, first_item in enumerate(input_list):
        for j, second_item in enumerate(input_list):
            if i != j:
                if first_item + second_item == 2020:
                    return first_item * second_item
    raise ValueError("Does not exist.")


def medium_solve(file_name):
    """Get each element line by line and store 2020-{line} until we find a line which is in the list."""
    inverted_list = []

    try:
        file_content = open(file_name, "r")
        for line in file_content:
            num = int(line.rstrip())
            if num in inverted_list:
                return num * (2020-num)
            else:
                inverted_list.append(2020 - num)
    except:
        print("Issue parsing input from file.")
        raise ValueError("Issue parsing input from file.")


def speed_solve(file_name):
    """Get each element line by line and store dict[2020-{line}] as True, faster for search."""
    inverted_dict = {}

    try:
        file_content = open(file_name, "r")
        for line in file_content:
            num = int(line.rstrip())
            try:
                if inverted_dict[num]:
                    return num * (2020-num)
            except:
                inverted_num = 2020 - num
                inverted_dict[inverted_num] = True
    except:
        print("Issue parsing input from file.")
        raise ValueError("Issue parsing input from file.")

if __name__ == "__main__":
    simple_ans = simple_solve("day_one.txt")
    medium_ans = medium_solve("day_one.txt")
    speed_ans = speed_solve("day_one.txt")
    print(simple_ans, medium_ans, speed_ans)
