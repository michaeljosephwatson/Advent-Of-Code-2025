"""My solution for day 4 of Advent of Code 2025."""

def get_puzzle_input() -> list[str]:
    with open('input_day_4.txt', 'r') as f:
        return [line.replace('\n', '') for line in f.readlines()]
    
def process_part_one(data: list[str]) -> int:
    """Returns my answer to part one"""

    accessible_rolls = 0
    for row_index in range(len(data)):
        focus_row = data[row_index]
        for space_index in range(len(focus_row)):

            if focus_row[space_index] != '@':
                continue

            adj_rolls = 0

            # Directly Below
            if row_index != len(data) - 1:
                row_below = data[row_index + 1]
                adj_rolls += row_below[space_index] == '@'

                # Diagonal Left Below
                if space_index != 0:
                    adj_rolls += row_below[space_index-1] == '@'

                # Diagonal Right Below
                if space_index != len(focus_row) - 1:
                    adj_rolls += row_below[space_index+1] == '@'

            # Directly Above
            if row_index != 0:
                row_above = data[row_index - 1]
                adj_rolls += row_above[space_index] == '@'

                # Diagonal Left Above
                if space_index != 0:
                    adj_rolls += row_above[space_index-1] == '@'

                # Diagonal Right Above
                if space_index != len(focus_row) - 1:
                    adj_rolls += row_above[space_index+1] == '@'

            # Directly Left
            if space_index != 0:
                adj_rolls += focus_row[space_index-1] == '@'

            # Directly Right
            if space_index != len(focus_row) - 1:
                adj_rolls += focus_row[space_index+1] == '@'

            if adj_rolls < 4:
                accessible_rolls += 1

    return accessible_rolls

def process_part_two(data: list[str]) -> int:
    """Returns my answer to part two of the problem"""

    accessible_rolls = 0
    while True:
        stack = []
        for row_index in range(len(data)):
            focus_row = data[row_index]
            for space_index in range(len(focus_row)):

                if focus_row[space_index] != '@':
                    continue

                adj_rolls = 0

                # Directly Below
                if row_index != len(data) - 1:
                    row_below = data[row_index + 1]
                    adj_rolls += row_below[space_index] == '@'

                    # Diagonal Left Below
                    if space_index != 0:
                        adj_rolls += row_below[space_index-1] == '@'

                    # Diagonal Right Below
                    if space_index != len(focus_row) - 1:
                        adj_rolls += row_below[space_index+1] == '@'

                # Directly Above
                if row_index != 0:
                    row_above = data[row_index - 1]
                    adj_rolls += row_above[space_index] == '@'

                    # Diagonal Left Above
                    if space_index != 0:
                        adj_rolls += row_above[space_index-1] == '@'

                    # Diagonal Right Above
                    if space_index != len(focus_row) - 1:
                        adj_rolls += row_above[space_index+1] == '@'

                # Directly Left
                if space_index != 0:
                    adj_rolls += focus_row[space_index-1] == '@'

                # Directly Right
                if space_index != len(focus_row) - 1:
                    adj_rolls += focus_row[space_index+1] == '@'

                if adj_rolls < 4:
                    accessible_rolls += 1
                    stack.append((row_index, space_index))

        if len(stack) == 0:
            break

        for _ in range(len(stack)):
            row_index, space_index = stack.pop()
            data[row_index] = data[row_index][:space_index] + '.' + data[row_index][space_index+1:]

    return accessible_rolls


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    print(f'Part one: {process_part_one(puzzle_input)}')
    print(f'Part two: {process_part_two(puzzle_input)}')