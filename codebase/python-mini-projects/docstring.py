# ===============================================================
# Docstring
# ===============================================================
""" Docstrings in Python are string literals that appear as the first statement in a module,
function, class, or method definition.  They serve as documentation, providing a clear
explanation of what the code does, its parameters, return values, and usage examples.

Syntax: Written using triple quotes (\""" or ''') immediately after the definition.

Accessibility: Accessible via the __doc__ attribute or the help() function.

Purpose: Multiline comments. Unlike comments (#), docstrings are retained at runtime and
are used to generate automated documentation (e.g., with Sphinx, Pydoc, or doctest).
"""


def format_name(f_name, l_name):
    """Take a first and last name then format it to return the
    title case version of the name"""

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

"""
You can use docstrings to write multiline comments that document your code.

Syntax
Just enclose your text inside a pair of three double quotes.

e.g.

\""" 
My 
Multiline 
Comment 
\"""

Documenting Functions
A neat feature of docstrings is you can use it just below the definition of a function and that text will be displayed when you hover over a function call. It's a good way to remind yourself what a self-created function does.

e.g.

def my_function(num):
    \"""Multiplies a number by itself.\"""
    return num * num
"""
