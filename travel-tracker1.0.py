"""
Name: weiting chen
Date: 30/04/2023
GitHub URL:https:https://github.com/chen1weiting/sandbox.git

"""

import csv
import random

import places as places

name = "Places.csv"


def main(file_path):
    places = load_places(file_path)
    if places is not None:
        print(f"Successfully loaded {len(places)} places.")
        print("Places:")
        for place in places:
            print(place)
    else:
        print("Failed to load places.")


main("places.txt")


def main():
    print("Travel Tracker 1.0 - by chen weiting")
    file_path = 'places.csv'
    places = load_places(file_path)
    print('Welcome to the Travel Tracker!')
    while True:
        print_menu()
        user_choice = input(">>> ").upper()

        if user_choice == "L":
            list_places(places)
        elif user_choice == "R":
            recommend_place(places)
        elif user_choice == "A":
            add_place(places)
        elif user_choice == "M":
            mark_visited(places)
        elif user_choice == "Q":
            save_places(places)
            print(f"{len(places)} places saved to places.csv\nHave a nice day :)")
        else:
            print("Invalid menu choice")

        print()


def print_menu():
    # Function shows the menu and ask user_choice

    print("Menu:")
    print("L - List Places")
    print("R - Recommend random place")
    print("A - Add new places")
    print("M - Mark a place that has been visited")
    print("Q - Quit")

    user_choice = input(">>>").upper()

    return user_choice


def load_places(file_path):
    place = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            places.append({'name': row[0], 'type': row[1], 'latitude': row[2], 'longitude': row[3]})
        for line in file:
            try:
                name, city, country, population = line.strip().split(',')
                population = int(population)
                place.append((name, city, country, population))
            except ValueError:
                print(f"Invalid data: {line.strip()}")
    return place


def read():
    # Read and store files inside the CSV files
    csv_data = []

    with open(name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(list(row))

    file.close()
    return csv_data


def list_places(places):
    # Function to list the data from CSV files that already made in a list
    places = sorted(places, key=lambda place: (place[3], place[2], place[0]))
    print("Places:")
    for i, place in enumerate(places):
        print(f"{i + 1}. {place[0]} in {place[1]} {place[2]}{' (visited)' if place[3] else ''}")
    num_unvisited = sum(1 for place in places if not place[3])
    print(f"{len(places)} places. You still want to visit {num_unvisited} places.")


def recommend_place(places):
    # Function to check if the place is already visited or not
    unvisited_places = [place for place in places if not place[3]]
    if not unvisited_places:
        print("No places left to visit!")
        return
    place = random.choice(unvisited_places)
    print(f"Not sure where to visit next?\nHow about... {place[0]} in {place[1]}?")


def add_place(places):
    # Function to add data or places to the list of the CSV files
    name = input("Name: ").strip()
    while not name:
        print("Input can not be blank")
        name = input("Name: ").strip()

    country = input("Country: ").strip()
    while not country:
        print("Input can not be blank")
        country = input("Country: ").strip()

    priority = input("Priority: ")
    while not priority.isdigit():
        print("Invalid input; enter a valid number")
        priority = input("Priority: ")
    priority = int(priority)

    places.append((name, country, priority, False))
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def mark_visited(places):
    # Function to mark places that has been visited
    unvisited_places = [place for place in places if not place[3]]
    if not unvisited_places:
        print("No unvisited places")
        return

    list_places(places)
    place_num = input("Enter the number of a place to mark as visited\n")
    while not place_num.isdigit() or int(place_num) < 1 or int(place_num) > len(places) or places[int(place_num) - 1][
        3]:
        if not place_num.isdigit():
            print("Invalid input; enter a valid number")
        elif int(place_num) < 1 or int(place_num) > len(places):
            print("Invalid place number")
        else:
            print(f"You have already visited {places[int(place_num) - 1][0]}")
        place_num = input()

    places[int(place_num) - 1] = (
        places[int(place_num) - 1][0], places[int(place_num) - 1][1], places[int(place_num) - 1][2], True)
    print(f"{places[int(place_num) - 1][0]} in {places[int(place_num) - 1][1]} visited!")


def save_places(filename, places):
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for place in places:
            name, country, priority, visited = place
            csv_writer.writerow([name, country, priority, "v" if visited else "n"])


if __name__ == '__main__':
    main()
