"""
Generates a random chaos line and score for the daily briefing.
No repeats. No mercy.
"""

import random

CHAOS_LINES = [
    "The flatlands are wide open — punch through the sunrise like a chrono-flux juggernaut.",
    "Coke cup locked, drivers rolling, horizon bending — ShaneBrain is AWAKE.",
    "7 at 4AM means the competition never even saw you coming. Keep it that way.",
    "Every load dropped is a brick in the legacy wall. Stack 'em up.",
    "Chaos doesn't schedule itself — but you do. That's the difference.",
    "The Pi is humming, the crew is deployed, and you haven't even had your Coke yet.",
    "North Alabama doesn't know what hit it. Keep rolling.",
    "Dispatch is done. Drivers are rolling. You built this. Own it.",
    "Another day, another empire brick. Let's go.",
    "ShaneBrain online. Tiffany in your corner. Boys watching. Make it count.",
    "Gavin's getting married, Ryker's growing up, and the fleet doesn't stop for any of it. Neither do you.",
    "Sobriety, faith, family, fleet. All four firing. That's not luck — that's you.",
]

def get_chaos_line():
    return random.choice(CHAOS_LINES)

def get_chaos_score():
    return random.randint(1, 10)

if __name__ == "__main__":
    print(f"Chaos Score: {get_chaos_score()}/10")
    print(get_chaos_line())
