"""
Kata Level: 8.

Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
"""

# Mi solución en Python.

def rps(p1, p2):
    if (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock") or (p1 == "rock" and p2 == "scissors"):
        return "Player 1 won!"
    elif (p1 == "scissors" and p2 == "rock") or (p1 == "paper" and p2 == "scissors") or (p1 == "rock" and p2 == "paper"):
        return "Player 2 won!"
    return "Draw!"


# Solución de la comunidad. Investigar porque no termino de entenderlo.

def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"