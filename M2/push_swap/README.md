# Push_swap

*This project has been created as part of the 42 curriculum by hgarcia2.*

## Description

**Push_swap** is a sorting algorithm project that challenges you to sort a stack of integers using a limited set of operations and the smallest number of moves possible. The program uses two stacks (a and b) and must sort the numbers in stack a in ascending order using only the following operations:

- **sa** (swap a): Swap the first 2 elements at the top of stack a
- **sb** (swap b): Swap the first 2 elements at the top of stack b
- **ss**: sa and sb at the same time
- **pa** (push a): Take the first element at the top of b and put it at the top of a
- **pb** (push b): Take the first element at the top of a and put it at the top of b
- **ra** (rotate a): Shift up all elements of stack a by 1
- **rb** (rotate b): Shift up all elements of stack b by 1
- **rr**: ra and rb at the same time
- **rra** (reverse rotate a): Shift down all elements of stack a by 1
- **rrb** (reverse rotate b): Shift down all elements of stack b by 1
- **rrr**: rra and rrb at the same time

### Project Goals

- Implement an efficient sorting algorithm using limited operations
- Understand and apply algorithmic complexity concepts
- Work with stack data structures
- Optimize the number of operations based on the size of the input

### Algorithm Overview

The implementation uses different strategies depending on the size of the input:

- **2 elements**: Simple swap if needed
- **3 elements**: Optimized hardcoded sorting (max 3 operations)
- **4+ elements**: Radix sort algorithm with bit manipulation

The radix sort implementation normalizes the values into indices (0, 1, 2, ..., n-1) and then sorts them by examining each bit position, pushing numbers with a 0 bit to stack b and rotating numbers with a 1 bit, then pushing everything back from b to a.

## Instructions

### Requirements

- **Operating System**: Linux or macOS
- **Compiler**: GCC or Clang with support for C99 standard
- **Make**: GNU Make

### Compilation

1. Clone the repository:
```bash
git clone <repository_url>
cd push_swap
```

2. Compile the project:
```bash
cd src
make
```

This will create the `push_swap` executable in the `src` directory.

### Compilation Flags

The project is compiled with the following flags:
- `-Wall`: Enable all warnings
- `-Wextra`: Enable extra warnings
- `-Werror`: Treat warnings as errors

### Cleaning

- Remove object files:
```bash
make clean
```

- Remove object files and executable:
```bash
make fclean
```

- Recompile everything:
```bash
make re
```

### Usage

Run the program with a list of integers as arguments:

```bash
./push_swap [list of integers]
```

**Examples:**

```bash
# Sort 3 numbers
./push_swap 2 1 3
# Output: sa

# Sort 5 numbers
./push_swap 5 2 4 1 3
# Output: pb pb sa pa pa ra ra (example output)

# Using quotes (single argument with spaces)
./push_swap "3 2 1"

# Invalid input (produces "Error\n")
./push_swap 1 2 three
./push_swap 1 2 2
./push_swap 1 2147483648

# Sort 100 random numbers (1-100)
ARG=$(seq 1 100 | shuf | tr '\n' ' '); ./push_swap $ARG
```

### Input Validation

The program validates input and displays "Error\n" (followed by exit) if:
- Arguments are not integers
- Arguments exceed INT_MAX or INT_MIN
- Duplicate numbers are present
- Non-numeric characters are found

### Output

The program outputs a list of operations (one per line) that, when executed on stack a, will result in a sorted stack. If the stack is already sorted, no output is produced.

## Testing

### Manual Testing

Test with different input sizes:

```bash
# Already sorted
./push_swap 1 2 3 4 5

# Reverse sorted
./push_swap 5 4 3 2 1

# Random order
./push_swap 3 7 1 9 2 8 4 6 5

# Edge cases
./push_swap 2147483647 -2147483648 0
./push_swap 42
```

### Counting Operations

To verify the number of operations:

```bash
./push_swap 3 2 1 5 4 | wc -l
```

### Performance Benchmarks

Expected maximum number of operations:

- **3 numbers**: 3 operations
- **5 numbers**: 12 operations
- **100 numbers**: < 700 operations (< 900 for grade 4, < 1100 for grade 3)
- **500 numbers**: < 5500 operations (< 7000 for grade 4, < 8500 for grade 3)

### Testing with Checker (if available)

If you have the checker program from the project:

```bash
ARG="4 3 2 1"; ./push_swap $ARG | ./checker $ARG
```

This should output "OK" if the sorting is correct.

## Project Structure

```
push_swap/
├── README.md
├── src/
│   ├── Makefile
│   ├── push_swap.c      # Main program and stack operations
│   ├── push_swap.h      # Header file with structures and prototypes
│   ├── sort.c           # Sorting algorithms implementation
│   ├── utils.c          # Stack utilities and validation
│   ├── utils2.c         # Parsing and initialization
│   └── utils3.c         # Radix sort utilities
└── libft/               # Custom C library
    ├── libft.h
    ├── Makefile
    └── [various subdirectories with utility functions]
```

## Technical Choices

### Data Structure

The project uses a **doubly linked list** to represent each stack:

```c
typedef struct s_stack
{
    int             value;
    struct s_stack  *next;
    struct s_stack  *prev;
} t_stack;
```

This allows efficient operations at both ends of the stack.

### Algorithm Selection

- **Radix Sort**: Chosen for its O(n×k) time complexity where k is the number of bits needed to represent the numbers. This is particularly efficient for sorting integers with a limited range.
- **Normalization**: Values are normalized to indices (0 to n-1) before sorting, which reduces the number of bits needed and thus the number of operations.

## Resources

### AI Usage

**AI tools were used in the following ways:**

1. **Code Review and Debugging**
   - Used AI to review sorting algorithm logic
   - Helped identify potential edge cases in input validation
   - Assisted in debugging memory leaks and pointer issues

2. **Algorithm Research**
   - Consulted AI to understand radix sort implementation details
   - Asked for explanations of bit manipulation techniques
   - Explored different algorithmic approaches and their trade-offs

3. **Documentation**
   - AI assisted in writing this README.md file structure
   - Helped format and organize technical documentation
   - Generated usage examples and test cases

4. **Code Optimization**
   - Discussed algorithm optimization strategies with AI
   - Reviewed time and space complexity analysis
   - Explored alternative sorting approaches for comparison

**Note**: All core algorithm implementation and logic were written by hand. AI was used as a learning tool and documentation assistant, not for generating the main project code.
