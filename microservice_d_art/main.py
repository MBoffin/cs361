import zmq

game_art = {
    "Arena Gods":"arenagods.png",
    "Astro Duel":"astroduel.png",
    "Battleblock Theater":"battleblocktheater.png",
    "Blaze Rush":"blazerush.png",
    "Broforce":"broforce.png", 
    "Brotato":"brotato.png",
    "Chaotic Voic":"chatoicvoid.png", 
    "ChargeShot":"chargeshot.png", 
    "Crawl":"crawl.png", 
    "Cuphead":"cuphead.png",
    "Dirty Dirty Pirates":"dirtydirtypirates.png",
    "Duck Game":"duckgame.png",
    "Flat Heroes":"flatheroes.png",
    "Full Metal Furies":"fullmetalfuries.png",
    "Gang Beasts":"gangbeasts.png",
    "Hammerwatch":"hammerwatch.png",
    "HardLander":"Hard Lander is a tough-as-nails \"Rocket Wrestling\" arena designed for up to 4 players. Invite three of your friends to compete for bragging rights and couch cred in what might be the most advanced rocket wrestling simulation ever created! Practice your piloting expertise through 40 punishing challenge courses that will be sure to have you throwing your controller across the room as you hone your skills.",
    "Hidden in Plain Sight":"hiddeninplainsigt.png",
    "Human Fall Flat":"humanfallflat.png",
    "The Jackbox Party Pack 2":"jackboxpartypack2.png",
    "Killer Queen Black":"killerqueenblack.png",
    "Lance A Lot":"lancealot.png",
    "Lara Croft and the Temple of Osiris":"laracroftandthetempleofosiris.png",
    "Laser Lasso Ball":"laserlassoball.png",
    "Lovers in a Dangerous Spacetime":"loversinadangerousspacetime.png",
    "Magicka":"magicka.png",
    "Mimic Arena":"minicarena.png",
    "Move or Die":"moveordie.png",
    "Nidhogg":"nidhogg.png",
    "No Heroes Here":"noheroeshere.png",
    "Overcooked":"overcooked.png",
    "PICO PARK":"picopark.png",
    "Pummel Party":"pummelparty.png",
    "Risk of Rain":"riskofrain.png",
    "Rocket League":"rocketleague.png",
    "ROCKETSROCKETSROCKETS":"rocketsrocketsrockets.png",
    "ROUNDS":"rounds.png",
    "Screencheat":"screencheat.png",
    "STARWHAL":"starwhal.png",
    "Stick Fight":"stickfight.png",
    "Totall Reliable Delivery Service":"totallyreliabledeliveryservice.png",
    "Towerfall Ascension":"towerfallascension.png",
    "Tricky Towers":"trickytowers.png",
    "Trine 2":"trine2.png",
    "Ultimate Chicken Horse":"ultimatechickenhorse.png",
    "Unrailed!":"unrailed.png",
    "Unrailed 2: Back on Track":"unrailed2backontrack.png",
    "Vampire Survivors":"vampiresurvivors.png",
    "Wand Wars":"wandwars.png",
    "Worms Reloaded":"wormsreloaded.png"
}

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5559")
    print("Game Art Microservice waiting on port 5559...")

    while True:
        game_name = socket.recv_string()

        # find matches to the game name
        if game_name in game_art:
            print(f"Received game name: {game_name}")
            socket.send_string(game_art[game_name])
            print(f"Responded with game art file path for {game_name}")
        else:
            socket.send_string("")



