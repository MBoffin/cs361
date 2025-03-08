import zmq

game_names = [
    "Arena Gods", "Astro Duel", "Battleblock Theater", "Blaze Rush", "Broforce", "Brotato",
    "Chaotic Voic", "ChargeShot", "Crawl", "Cuphead", "Dirty Dirty Pirates", "Duck Game",
    "Flat Heroes", "Full Metal Furies", "Gang Beasts", "Hammerwatch", "HardLander", "Hidden in Plain Sight",
    "Human Fall Flat", "The Jackbox Party Pack 2", "Killer Queen Black", "Lance A Lot",
    "Lara Croft and the Temple of Osiris", "Laser Lasso Ball", "Lovers in a Dangerous Spacetime",
    "Magicka", "Mimic Arena", "Move or Die", "Nidhogg", "No Heroes Here", "Overcooked", "PICO PARK",
    "Pummel Party", "Risk of Rain", "Rocket League", "ROCKETSROCKETSROCKETS", "ROUNDS", "Screencheat",
    "STARWHAL", "Stick Fight", "Totall Reliable Delivery Service", "Towerfall Ascension", "Tricky Towers",
    "Trine 2", "Ultimate Chicken Horse", "Unrailed!", "Unrailed 2: Back on Track", "Vampire Survivors",
    "Wand Wars", "Worms Reloaded"
]

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5557")
    print("Game Name Microservice waiting on port 5557...")

    while True:
        name_fragment = socket.recv_string()
        print(f"Received name fragment: {name_fragment}")

        # find matches to the fragment
        matches = [name for name in game_names if name_fragment.lower() in name.lower()]

        response = "\n".join(matches)
        socket.send_string(response)
        print(f"Responded with {len(matches)} matches")


