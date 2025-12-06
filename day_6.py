"""My solution to Day 6 of Advent of Code 2025."""

def get_puzzle_input() -> list[str]:
    with open('input_day_6.txt', 'r') as f:
        return f.read().splitlines()

def process_part_one(data: list[str]) -> int:
    """Returns my answer for part one"""

    max_width = max(len(line) for line in data)
    problems = []
    col = 0
    
    while col < max_width:
        while col < max_width and all(col >= len(row) or row[col] == ' ' for row in data):
            col += 1
        
        if col >= max_width:
            break
        
        start_col = col
        while col < max_width and any(col < len(row) and row[col] != ' ' for row in data):
            col += 1
        
        numbers = []
        for row in data[:-1]:
            num_str = row[start_col:col].strip()
            if num_str:
                numbers.append(int(num_str))
        
        operation = data[-1][start_col:col].strip()
        problems.append((numbers, operation))
    
    grand_total = 0
    for numbers, operation in problems:
        if operation == '+':
            result = sum(numbers)
        elif operation == '*':
            result = 1
            for num in numbers:
                result *= num
        grand_total += result
    
    return grand_total

def process_part_two(data: list[str]) -> int:
    """Returns my answer for part two"""

    max_width = max(len(line) for line in data)
    
    problems = []
    col = 0
    
    while col < max_width:
        while col < max_width and all(col >= len(row) or row[col] == ' ' for row in data):
            col += 1
        
        if col >= max_width:
            break
        
        start_col = col
        while col < max_width and any(col < len(row) and row[col] != ' ' for row in data):
            col += 1
        
        numbers = []
        for c in range(col - 1, start_col - 1, -1):
            num_str = ""
            for row in data[:-1]:
                if c < len(row) and row[c] != ' ':
                    num_str += row[c]
            if num_str:
                numbers.append(int(num_str))
        
        operation = data[-1][start_col:col].strip()
        problems.append((numbers, operation))
    
    grand_total = 0
    for numbers, operation in problems:
        if operation == '+':
            result = sum(numbers)
        elif operation == '*':
            result = 1
            for num in numbers:
                result *= num
        grand_total += result
    
    return grand_total

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    print(f'First part: {process_part_one(puzzle_input)}')
    print(f'Second part: {process_part_two(puzzle_input)}')