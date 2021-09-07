# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000
# note that the csv is organized ast team,rating (key,value)
def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")
    # creates a var called teams and makes it an empty list
    teams = []
    # Opens file from argv[1] and calls it fileName
    fileName = sys.argv[1]
    with open(fileName) as file:
        # csv.DictReader(f) to give you a “reader”: an object in Python that you reads the file
        reader = csv.DictReader(file)
        # loop over to read the file one row at a time, treating each row as a dictionary.
        for team in reader:
            # [] accesses the value (rating) for a key (team) inside the dictionary (file), casts rating to int
            team["rating"] = int(team["rating"])
            # adds a dictionary with the team to the teams list
            teams.append(team)

    # creat an empty dict called counts
    counts = {}
    # Simulate N tournaments and keep track of win counts
    # Note that i can be named anything, it is part of the for loop and is incremented N times, similiar to
    # for (i = 0; i < N; i++) in C language
    for i in range(N):
        # calll simulation which will give the winner N times and add up the number of wins (counts)
        winner = simulate_tournament(teams)
        # keeps track of each teams wins
        if winner in counts:
            counts[winner] += 1
        # their first win, add them to counts
        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # take a list of teams, and run rounds on that list of teams, as long as there is more
    # than one team, we keep simulating rounds until there is a winner
    while len(teams) > 1:
        # will only contain winners, until there is just one
        teams = simulate_round(teams)
    # teams will only have one element [0] in the list, which is the winner. ["team"] gives the
    # name of the team in the dict
    return teams[0]["team"]


if __name__ == "__main__":
    main()
