# ===============================================================
# Type hint
# ===============================================================
age: int
name: str
height: float
is_human: bool


#  Type Hints
def greeting(name: str) -> str:
    return 'Hello' + name

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive


if police_check(12):
    print("you may pass")
else:
    print("Pay a fine.")

"""
Type hints in Python are syntactic annotations introduced in Python 3.5 (PEP 484) that specify expected 
data types for variables, function arguments, and return values without enforcing them at runtime.  
These hints are stored in the __annotations__ attribute as a dictionary and serve as documentation to 
improve code readability and enable static type checkers like mypy to detect errors before execution. 

1. Basic Syntax: Hints use the : operator for variables and parameters, and -> for return types 
(e.g., def greet(name: str) -> str:). 
2. Collections & Complex Types: The typing module provides generics like List[int], Dict[str, int], and 
Tuple to define element types within data structures. 
3. Advanced Features: Developers can use Optional for nullable values, Union for multiple possible types, 
and create type aliases for complex structures to enhance maintainability.
4. Verification: While Python ignores these hints during execution, tools like mypy analyze the 
__annotations__ to ensure consistency, often requiring the --strict flag for comprehensive checking. 
"""
from typing import List, Optional, Dict

def process_data(items: List[int]) -> Optional[Dict[str, int]]:
    """
    Takes a list of integers and returns a dictionary mapping 
    specific keys to sums, or None if input is empty.
    """
    if not items:
        return None
    return {"sum": sum(items)}