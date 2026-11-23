# Python Projects

I'm Denzel Asamoah, a computer science student at the University of Maryland, Baltimore County, expecting to graduate in 2029. This collection contains selected Python programs from my CMSC 201 coursework and practice.

## Featured programs

| Program | What it does | Concepts |
| --- | --- | --- |
| `groceries.py` | Loads inventory from a text file and manages a shopping cart | File parsing, dictionaries, stock updates |
| `crossystreet.py` | Checks whether a grid has an open route moving down and right | Grid traversal, reachability |
| `knight_ai.py` | Ranks available knight captures by piece value | Coordinate bounds, tuples, bubble sort |
| `alibi.py` | Finds conflicting partner statements at the same time | String parsing, nested dictionaries |
| `art_generator.py` | Converts numeric rows into ASCII character patterns | Normalization, edge cases |
| `ctrlf.py` | Finds a word in a text file and reports its line and offset | File reading, string processing |

Additional exercises include a tic-tac-toe winner checker, word frequency analysis, Pascal's triangle, checkerboard output, restaurant table totals, and writing prefixed log entries.

## Run a program

Use Python 3. These programs use the Python standard library.

```text
python art_generator.py
```

Enter a row of numbers, then a blank line to exit.

```text
0 5 10
```

Output:

```text
.=@
```

For the grocery simulator, save these lines in a file named `market.txt`:

```text
apple, 4
orange, 5
orange, 4
```

Run `python groceries.py`, enter `market.txt`, and follow the menu. For Buy or Remove, enter an item and quantity on one line, such as `apple 2`. Duplicate inventory entries are combined when loading the file.

## Learning focus

These exercises reflect my progress with Python functions, loops, dictionaries, lists, file input/output, and algorithmic problem solving. They use assignment-specific input formats. The grocery program currently expects positive integer quantities and correctly formatted input.
