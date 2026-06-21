# Escape Sequence
''' What are Escape Sequences?
    Escape sequences are special character combinations used inside strings or characters to represent things 
    that can’t be typed directly (like newline, tab, quotes, etc.).
    They always start with a backslash \.   '''

print("Hello\nWorld")      # New line
print("Hello\tWorld")      # Tab spaces
print("It\'s Python")      # Single quote
print("He said \"Hi\"")    # Double quote
print("C:\\Users\\Frank")  # Backslash
print("Hello\bWorld")      # Backspace
print("A in octal:", "\101")
print("A in hex:", "\x41")


'''     Escape Sequence	    Description
        \\	                Backslash (\)
        \'	                Single quote (')
        \"	                Double quote (")
        \n	                New line
        \t	                Horizontal tab
        \r	                Carriage return
        \b	                Backspace
        \f	                Form feed
        \v	                Vertical tab
        \a	                Bell (alert)
        \N{name}	        Unicode character by name
        \uXXXX	            Unicode character (16-bit, 4 hex digits)
        \UXXXXXXXX	        Unicode character (32-bit, 8 hex digits)
        \ooo	            Character with octal value
        \xhh	            Character with hex value    '''