# FSM Modulo Three Exercise

This project implements a reusable finite automaton and applies it to compute the remainder of a binary number modulo 3.

## Project Structure

- `FiniteAutomaton.py`: Generic finite state machine implementation.
- `mod_three.py`: FSM configuration for modulo-3 computation and `mod_three()` helper.
- `test_finite_automaton.py`: Unit tests for the generic FSM behavior.
- `test_mod_three.py`: Unit tests for modulo-3 logic.

## Requirements

- Python 3.8+

## Run the Example

```bash
cd path/to/project_root
python mod_three.py
```

Expected output:

```text
1
2
0
```

## Use in Code

```python
from mod_three import mod_three

print(mod_three("1101"))  # 1
print(mod_three("1110"))  # 2
print(mod_three("1111"))  # 0
```

## Run Tests

Run all tests:

```bash
cd path/to/project_root
python -m unittest discover
```

Run specific test files:

```bash
cd path/to/project_root
python -m unittest test_finite_automaton.py
python -m unittest test_mod_three.py
```

## Notes

- Input to `mod_three()` must be a binary string containing only `0` and `1`.
- An empty string is treated as binary zero, so `mod_three("") == 0`.
