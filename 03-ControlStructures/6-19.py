computer_science = False
computer_games = False
instagram = False

computer_science_czy = input("Are you interested in computer science? (y/n): ")
computer_games_czy = input("Do you like playing computer games? (y/n): ")
instagram_czy = input("Do you have an Instagram account? (y/n): ")

if computer_science_czy == "y":
    computer_science = True

if computer_games_czy == "y":
    computer_games = True

if instagram_czy == "y":
    instagram = True

print(f'Interested in computer science: {computer_science}')
print(f'Playing computer games: {computer_games}')
print(f'Has an Instagram account: {instagram}')