from NitrotypePy import user

def check_racers():
    # List of Nitro Type usernames to track
    racers = ["exampleUser1", "exampleUser2", "exampleUser3"]

    for racer in racers:
        racer_data = user(racer)

        if racer_data["racesCompleted"] >= 100:
            print(f"{racer} has reached 100 races! 🎉")

if __name__ == "__main__":
    check_racers()
 
