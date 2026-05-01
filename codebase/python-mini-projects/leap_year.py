# ===============================================================
# Leap year
# ===============================================================

def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


is_leap_year(2000)


# ===============================================================
# Optimized version for Beginner - Leap year
# ===============================================================
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# ===============================================================
# Optimized Version - Leap year
# ===============================================================
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

