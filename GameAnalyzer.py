# Mini Project: Game Library Analyzer

games = ["Hogwarts Legacy", "Minecraft", "FIFA 23", "inFamous", "Dante's Inferno", "Spider-Man 2", "WWE 2K16"]
ratings = [9.2, 10, 8.4, 8.5, 8.2, 8.1, 7.4]


for index, game in enumerate(games):
    rating = ratings[index]
    print(f"{game} - {rating}/10")

print(" ")

# Average Rating
average_rating = 0

for rating in ratings:
    average_rating += rating

print(average_rating/len(ratings))

print(" ")
# Highest Rated
highest_game = games[0]
highest_rating = ratings[0]

for game, rating in zip(games, ratings):
    if rating > highest_rating:
        highest_rating = rating
        highest_game = game

print(f"Highest Rated Game: {highest_game} - {highest_rating}")

print(" ")

# Categories
masterpiece_count = 0
excellent_count = 0
good_count = 0
average_count = 0

for game, rating in zip(games, ratings):
    if rating == 10:
        masterpiece_count += 1
        print(f"{game} - Masterpiece")
    elif rating >= 9:
        excellent_count += 1
        print(f"{game} - Excellent")
    elif rating >= 8:
        good_count += 1
        print(f"{game} - Good")
    else:
        average_count += 1
        print(f"{game} - Average")

print(" ")

# Games above certain ratin

minimum_rating = float(input("Show games rated at least: "))
print(" ")

print("Games:")
for game, rating in zip(games,ratings):
    if minimum_rating <= rating:
        print(f"{game} - {rating}")

print(" ")


# Game Statistics
print("===game library===\n".upper())
print(f"Games: {len(games)}")
print(f"Average rating: {average_rating/len(games)}")
print(f"Highest rating: {highest_rating}")
print(f"Masterpiece: {masterpiece_count}")
print(f"Excellent: {excellent_count}")
print(f"Good: {good_count}")
print(f"Average: {average_count}")

print(" ")

# First 3

print("-----first 3-----".upper())

for i in range(3):
    print(games[i])


#Overall - 9.3/10