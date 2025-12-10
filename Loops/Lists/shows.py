SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family "
]


def main():
    new_shows = []
    for show in SHOWS:
        new_shows.append(show.title().strip())

    print(", ".join(new_shows))


main()