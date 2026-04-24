# ===============================================================
# Love calculator
# ===============================================================
def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0
    name = (name1 + name2).lower()
    true = "true"
    love = "love"

    for char in name:
        if char in true:
            true_count += 1
        else:
            true_count

    for char in name:
        if char in love:
            love_count += 1
        else:
            love_count

    print(f"{true_count}{love_count}")
    # true_count = str(true_count)
    # love_count = str(love_count)
    # count = true_count + love_count

    # print(count)


calculate_love_score("Rogith", "Angela")


# ===============================================================
# Optimised version of Love calculator
# ===============================================================
def calculate_love_score(boy_name, girl_name):
    combined_name = (boy_name + girl_name).lower()

    true_score = sum(combined_name.count(letter) for letter in "true")
    love_score = sum(combined_name.count(letter) for letter in "love")

    love_percentage = int(f"{true_score}{love_score}")

    print(f"Love Score: {love_percentage}")


boy_name = input("Enter the boy's name: ")
girl_name = input("Enter the girl's name: ")

calculate_love_score(boy_name, girl_name)