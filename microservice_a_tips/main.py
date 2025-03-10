import zmq
import random

# Tips array
game_tips = [
    "You can always go back to your full list of games by clicking on the Home Button!",
    "You can sort your list of games by name, genre, or year.",
    "When adding game art to a new game, you can either browse your files for game art, or you can drag and drop art.",
    "If you don't have art for a game, don't worry! Placeholder art will be used instead.",
    "Make sure to categorize your games by genre to quickly find your favorites.",
    "Use the search function in your game library to find specific titles faster."
]

def start_publisher():
    # Set up ZeroMQ context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    
    # Bind to port 5556
    socket.bind("tcp://*:5556")
    print("Publisher started on port 5556...")
    
    while True:
        # Wait for a request from a subscriber
        num_tips = int(socket.recv_string())  # Receive the number of tips requested
        print(f"Received request for {num_tips} tips")

        # Select random tips
        selected_tips = random.sample(game_tips, num_tips)  # Select unique tips
        

        # Send the selected tips back to the subscriber
        response = "\n".join(selected_tips)
        socket.send_string(response)

if __name__ == "__main__":
    start_publisher()
