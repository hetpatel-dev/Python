# Python & DSA — Full Curriculum Roadmap

> **Status legend:** ✅ Done | 🔜 Current | ⬜ Upcoming
>
> Each topic has its own folder under `exercises/<topic-name>/` with progressive exercises.
> The `exercises/general/` folder holds mixed-concept exercises for retrieval practice.

---

## Phase 1: Python Fundamentals

### 1. Python Basics ✅
- `print()` and `input()` functions
- Comments (`#`)
- Variables — assignment and naming rules
- Basic data types: `int`, `float`, `str`, `bool`
- `type()` function
- f-strings and string formatting
- Basic arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)

### 2. Variables in Depth ✅
- Python's data model: objects, identity, type, value
- `id()` and `is` vs `==`
- Mutable vs immutable types
- Assignment patterns: multiple assignment, swapping, tuple unpacking, star unpacking (`*`)
- Augmented assignment (`+=`, `-=`, etc.) — in-place vs rebind
- Type annotations / type hints (`name: str = "Alice"`)
- `del` — unbinding names
- Naming conventions (PEP 8: `snake_case`, `UPPER_CASE`, `_private`)
- Variable scope (brief intro)

### 3. Data Types Overview ✅
- Full type hierarchy: numeric, boolean, text, binary, sequence, set, mapping, None, callable
- Truthiness — what's False in Python
- `bool()` and truth value testing
- Type conversion constructors (`int()`, `float()`, `str()`, `list()`, etc.)
- `type()` vs `isinstance()`
- Hashable concept
- Mutable vs immutable overview per category
- Ordered vs unordered

### 4. Operators in Depth
- Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Chained comparisons: `a < b < c`
- Logical operators: `and`, `or`, `not` — short-circuit evaluation
- Membership operators: `in`, `not in`
- Identity operators: `is`, `is not`
- Bitwise operators: `&`, `|`, `^`, `~`, `<<`, `>>`
- Operator precedence table
- Operator overloading concept (mention `__add__`, etc. — deep dive later)

### 5. Conditionals
- `if`, `elif`, `else`
- Truthiness in conditions
- Nested conditionals
- Ternary expression: `x if cond else y`
- `match`/`case` (structural pattern matching — Python 3.10+)
- Common patterns: `if x is None`, `if not x`, `if x in collection`

### 6. Loops
- `for` loop — iterating over sequences
- `range()` — `start`, `stop`, `step`
- `while` loop
- `break` and `continue`
- `else` clause on loops
- Nested loops
- `enumerate()` — getting index + value
- `zip()` — iterating multiple sequences
- Loop else patterns

### 7. Strings in Depth
- String methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`, `.replace()`, `.find()`, `.count()`, `.startswith()`, `.endswith()`
- String indexing and slicing (review + advanced)
- String immutability
- `ord()` and `chr()`
- Unicode and encoding (`str.encode()`, `bytes.decode()`)
- Raw strings (`r"..."`)
- Multi-line strings (`"""..."""`)
- Advanced f-strings: formatting specifiers, nested expressions
- `str.format()` and format spec
- `re` module basics (optional)

### 8. Lists in Depth
- List methods: `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.clear()`, `.index()`, `.count()`, `.sort()`, `.reverse()`, `.copy()`
- List indexing and slicing
- Nested lists
- List as stack (`append`/`pop`) and queue (`collections.deque`)
- `sorted()` vs `.sort()`
- List pitfalls: `[[]] * 3`, shallow copies
- `del` with lists
- List iteration patterns

### 9. Tuples
- Tuple creation and unpacking
- Single-element tuple `(1,)`
- Tuple immutability
- When to use tuples vs lists
- Named tuples (`collections.namedtuple`)
- Tuple methods: `.count()`, `.index()`
- Tuple as dict keys (hashable if elements are hashable)

### 10. Dictionaries in Depth
- Dict methods: `.get()`, `.setdefault()`, `.pop()`, `.update()`, `.keys()`, `.values()`, `.items()`, `.clear()`, `.copy()`
- Dict iteration
- `defaultdict`, `Counter`, `OrderedDict` (`collections`)
- Dict comprehensions
- Merging dicts (`|` operator, `**` unpacking)
- Insertion ordering guarantee (3.7+)
- Hashable keys requirement
- Nested dicts

### 11. Sets
- Set methods: `.add()`, `.remove()`, `.discard()`, `.pop()`, `.clear()`, `.copy()`
- Set operations: union `|`, intersection `&`, difference `-`, symmetric difference `^`
- Set comparisons: `<=`, `<`, `>=`, `>`
- `frozenset` — immutable, hashable sets
- Set comprehensions
- When to use sets (deduplication, membership, set math)

### 12. Functions in Depth
- Function definition (`def`) and calling
- Parameters: positional, keyword, default, `*args`, `**kwargs`
- Return values and `None`
- Docstrings
- Scope: `global`, `nonlocal`, LEGB rule
- Functions as first-class objects
- Lambda functions
- `map()`, `filter()`, `reduce()`
- Type annotations for functions
- Recursion basics

### 13. Comprehensions
- List comprehensions: `[expr for x in iterable if cond]`
- Dict comprehensions: `{k: v for k, v in iterable}`
- Set comprehensions: `{expr for x in iterable}`
- Generator expressions: `(expr for x in iterable)`
- Nested comprehensions
- When to use vs not use (readability trade-offs)

### 14. Error Handling
- `try`/`except`/`else`/`finally`
- Catching specific exceptions
- `raise` — raising exceptions
- `assert`
- Common built-in exceptions: `TypeError`, `ValueError`, `IndexError`, `KeyError`, `FileNotFoundError`
- Custom exception classes
- Context managers (`with` statement) — intro
- `ExceptionGroup` (Python 3.11+)

### 15. File I/O
- `open()` — modes: `r`, `w`, `a`, `b`, `+`
- `with` statement for file handling
- Reading: `.read()`, `.readline()`, `.readlines()`, iteration
- Writing: `.write()`, `.writelines()`
- Text vs binary files
- File paths: `pathlib.Path`
- CSV files (`csv` module)
- JSON (`json` module)

### 16. Modules & Packages
- `import` statement — absolute and relative imports
- `from ... import ...` and `as` aliases
- `if __name__ == "__main__"` pattern
- Creating your own modules
- Packages: `__init__.py`, subpackages
- The module search path (`sys.path`)
- `dir()` and `__all__`

### 17. Iterators & Generators
- The iteration protocol: `__iter__()`, `__next__()`, `StopIteration`
- Iterable vs iterator
- `iter()` and `next()`
- Custom iterators
- Generator functions with `yield`
- Generator expressions
- `yield from`
- `itertools` module overview: `count`, `cycle`, `chain`, `product`, `permutations`

---

## Phase 2: Object-Oriented Programming

### 18. OOP — Classes & Objects
- `class` definition
- `__init__` constructor
- `self` parameter
- Instance attributes vs class attributes
- Instance methods, class methods (`@classmethod`), static methods (`@staticmethod`)
- `__str__` and `__repr__`
- Public, private (`_`), and name mangling (`__`)
- `@property` decorator

### 19. OOP — Inheritance & Polymorphism
- Single inheritance
- `super()` — calling parent methods
- Method resolution order (MRO)
- Multiple inheritance
- Mixins
- Abstract base classes (`abc.ABC`, `@abstractmethod`)
- Duck typing — "if it walks like a duck"
- `isinstance()` and `issubclass()`

### 20. OOP — Magic Methods & Protocols
- `__add__`, `__sub__`, `__mul__` (arithmetic protocols)
- `__eq__`, `__lt__`, `__hash__` (comparison/hashing)
- `__len__`, `__getitem__`, `__setitem__` (container protocols)
- `__call__` (callable objects)
- `__enter__`, `__exit__` (context manager protocol)
- `__iter__`, `__next__` (iterator protocol)
- `__bool__` (truthiness)
- `__slots__` for memory optimization
- `dataclasses` module

### 21. OOP — Decorators & Properties
- Decorator pattern — `@decorator`
- `functools.wraps`
- Decorators with arguments
- Class decorators
- `@property` getter/setter/deleter
- `@functools.lru_cache`, `@functools.cache`

---

## Phase 3: Data Structures & Algorithms

### 22. Big O Notation
- Time complexity: O(1), O(log n), O(n), O(n log n), O(n²)
- Space complexity
- Best, average, worst case
- Analyzing loops and recursion
- Common complexity classes

### 23. Arrays & Python Lists
- Array vs list internals
- Dynamic array resizing
- Two-pointer technique
- Sliding window
- In-place operations

### 24. Linked Lists
- Singly linked list
- Doubly linked list
- Traversal, insertion, deletion
- Reversal
- Detecting cycles (Floyd's algorithm)

### 25. Stacks & Queues
- Stack: LIFO, `collections.deque` as stack
- Queue: FIFO, `collections.deque` as queue
- `queue.Queue`, `queue.PriorityQueue`
- Use cases: undo, expression evaluation, BFS

### 26. Recursion
- Base case and recursive case
- Call stack visualization
- Factorial, Fibonacci, tree traversal
- Tail recursion
- Memoization
- Divide and conquer pattern

### 27. Searching Algorithms
- Linear search
- Binary search (iterative + recursive)
- `bisect` module

### 28. Sorting Algorithms
- Bubble sort, selection sort, insertion sort
- Merge sort
- Quick sort
- Python's `sorted()` and `list.sort()` (Timsort)
- Stability

### 29. Hash Tables
- Hash function concept
- Collision resolution
- Python's dict and set internals (brief)
- Custom hashable types (`__hash__` + `__eq__`)

### 30. Trees
- Binary trees
- Binary search trees (BST)
- Tree traversals: preorder, inorder, postorder, level-order
- Tree balancedness concept
- Heaps (`heapq` module)
- Tries (prefix trees)

### 31. Graphs
- Graph representations: adjacency list, adjacency matrix
- BFS
- DFS
- Shortest path (Dijkstra)
- Cycle detection
- Topological sort

### 32. Dynamic Programming
- Overlapping subproblems
- Optimal substructure
- Top-down (memoization) vs bottom-up (tabulation)
- Classic problems: Fibonacci, knapSack, coin change, LCS, LIS

---

## Phase 4: Mixed Practice

### 33. General / Mixed-Concept Exercises
- Exercises combining multiple concepts
- Mini-projects
- Problem-solving patterns
- Coding challenges
- The `exercises/general/` folder grows here

---

> **How to use this document:**
> - We progress top-to-bottom, but you decide when each topic is mastered
> - Each topic gets a dedicated exercises folder
> - After every few topics, we can pause for mixed-concept exercises in `exercises/general/`
> - Topics with depth will have multiple lessons (e.g., OOP spans 4 lessons)
> - This document will evolve as we discover new things we want to learn
