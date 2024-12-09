# Problem 1: Assign 10 last names to an array and display them
def display_names(names):
    print("Names in original order:")
    for name in names:
        print(name)

def display_names_reverse(names):
    print("\nNames in reverse order:")
    for name in reversed(names):
        print(name)

# Problem 2: Add an array of exam scores and display both last names and scores
def display_names_and_scores(names, scores):
    print("\nNames and scores in original order:")
    for i in range(len(names)):
        print(f"{names[i]}: {scores[i]}")

def display_names_and_scores_reverse(names, scores):
    print("\nNames and scores in reverse order:")
    for i in range(len(names)-1, -1, -1):
        print(f"{names[i]}: {scores[i]}")

# Problem 3: Find highest and lowest exam score from a file
def display_highest_and_lowest(names, scores):
    high_var = 0
    low_var = 999
    high_index = low_index = -1

    # Find the highest and lowest scores
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print(f"\nHighest score: {names[high_index]} with {high_var}")
    print(f"Lowest score: {names[low_index]} with {low_var}")

# Problem 4: Load list of player names and batting averages from a file
def load_data_from_file(file_path):
    names = []
    averages = []
    with open(file_path, 'r') as file:
        for line in file:
            name, avg = line.strip().split(',')
            names.append(name)
            averages.append(float(avg))
    return names, averages

def display_player_data(names, averages):
    print("\nPlayer names and batting averages:")
    for i in range(len(names)):
        print(f"{names[i]}: {averages[i]}")

def search_player(names, averages, search_name):
    if search_name in names:
        index = names.index(search_name)
        print(f"{names[index]}: {averages[index]}")
    else:
        print("Name not found.")

# Problem 5: Modify search_player to display "Name not found" if the name doesn't exist
def search_player_with_message(names, averages, search_name):
    if search_name in names:
        index = names.index(search_name)
        print(f"{names[index]}: {averages[index]}")
    else:
        print("Name not found.")

# Example Data for Testing
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
exam_scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]

# Problem 1: Display names
display_names(last_names)
display_names_reverse(last_names)

# Problem 2: Display names and scores
display_names_and_scores(last_names, exam_scores)
display_names_and_scores_reverse(last_names, exam_scores)

# Problem 3: Display highest and lowest score
display_highest_and_lowest(last_names, exam_scores)

# Problem 4: Simulate reading player names and batting averages from a file
# Replace this with actual file reading when implementing
names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
averages = [0.267, 0.300, 0.315, 0.220, 0.310, 0.290, 0.280, 0.310, 0.250, 0.300]

# Display player data
display_player_data(names, averages)

# Search for a player
search_name = input("\nEnter the last name of the player to search: ")
search_player_with_message(names, averages, search_name)

