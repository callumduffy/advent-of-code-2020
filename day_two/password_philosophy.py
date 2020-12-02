"""Day two of the Advent of Code 2020."""

from password_policy import PasswordPolicy

INPUT_FILE = "input_file.txt"

def fetch_input_as_list():
    """Read the input from file, pity no API for this."""
    policy_list = []

    try:
        file_content = open(INPUT_FILE, "r")
        for line in file_content.read().split('\n'):
            pp = split_input_line(line)
            policy_list.append(pp)
        return policy_list
    except Exception as ex:
        print(f"Issue reading input from file: {ex}")
        raise ValueError("Issue reading input from file.")


def split_input_line(line):
    """Break the input line up into its pieces and return class."""
    mid_split = line.split(":")
    password = mid_split[1].strip()
    front_split = mid_split[0].split(" ")
    character = front_split[1]
    min_max_split = front_split[0].split("-")
    min_value = int(min_max_split[0])
    max_value = int(min_max_split[1])
    return PasswordPolicy(min_value, max_value, character, password)


def simple_solve():
    """Solve the inital problem the simple slow way."""
    policy_list = fetch_input_as_list()
    count = 0
    for policy in policy_list:
        if policy.is_valid_password_p1():
            count+=1
    return count


def better_solve():
    """Improve it by processing each line as it goes."""
    correct_passwords = 0
    try:
        file_content = open(INPUT_FILE, "r")
        for line in file_content.read().split('\n'):
            pp = split_input_line(line)
            if pp.is_valid_password_p1():
                correct_passwords+=1
        return correct_passwords
    except Exception as ex:
        print(f"Issue reading input from file: {ex}")
        raise ValueError("Issue reading input from file.")


def second_star_solve():
    """Changing to solve the second star."""
    correct_passwords = 0
    try:
        file_content = open(INPUT_FILE, "r")
        for line in file_content.read().split('\n'):
            pp = split_input_line(line)
            if pp.is_valid_password_p2():
                correct_passwords+=1
        return correct_passwords
    except Exception as ex:
        print(f"Issue reading input from file: {ex}")
        raise ValueError("Issue reading input from file.")


def run_part_one():
    """Run all functions to solve part one of the problem."""
    simple_ans = simple_solve()
    print(simple_ans)
    better_ans = better_solve()
    print(better_ans)


def run_part_two():
    """Run all functions to solve part two of the problem."""
    p2_ans = second_star_solve()
    print(p2_ans)


if __name__ == "__main__":
    run_part_one()
    run_part_two()