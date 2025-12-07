"""My solution for day 7 of Advent of Code 2025."""

def get_puzzle_input() -> list[str]:
    """Gets the puzzle input"""

    with open("input_day_7.txt", "r") as f:
        return [line.replace('\n', '') for line in f.readlines()]
    

def process_part_one(data: list[str]) -> int:
    """Returns my answer for part one"""

    current_indexes = [data[0].index('S')]
    splits = 0
    
    for line in data[1:]:
        next_indexes = []
        for index in current_indexes:
            if line[index] == '^':
                next_indexes.append(index - 1)
                next_indexes.append(index + 1)
                splits += 1
            else:
                next_indexes.append(index)
        current_indexes = list(set(next_indexes))
    
    return splits

def process_part_two(data: list[str]) -> int:
    """Returns my answer for part two"""

    start_index = data[0].index('S')
    timeline_counts = {start_index: 1}
    
    for line in data[1:]:
        next_timeline_counts = {}
        for index, count in timeline_counts.items():
            if line[index] == '^':
                next_timeline_counts[index - 1] = next_timeline_counts.get(index - 1, 0) + count
                next_timeline_counts[index + 1] = next_timeline_counts.get(index + 1, 0) + count
            else:
                next_timeline_counts[index] = next_timeline_counts.get(index, 0) + count
        timeline_counts = next_timeline_counts
    
    return sum(timeline_counts.values())

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    print(f"First part: {process_part_one(puzzle_input)}")
    print(f"Second part: {process_part_two(puzzle_input)}")