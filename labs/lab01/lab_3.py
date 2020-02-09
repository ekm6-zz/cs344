"""
    This module implements the simple blocks world using PAIP GPS.
"""
from gps import gps
import copy 

# Formulate the problem states and actions.
problem = {
    "initial": ["you are at home", "you have money", "you conform to societal pressures", "car needs prayers"],
    "goal": ["you are at johnny's", "you have money"],
    "actions": [
        {
            "action": "drive to johny's",
            "preconds": ["you are at home", "car works"],
            "add": ["you are at johnny's"],
            "delete": [" you are at home"]
        },
        {
            "action": "fake pastor prays for car",
            "preconds": ["car needs prayers", "being extorted by fake pastor", "fake pastor has your money"],
            "add": ["car works", "you delete"],
            "delete": []
        },
        {
            "action": "tell fake pastor problem",
            "preconds": ["talking to fake pastor"],
            "add": ["being extorted by fake pastor"],
            "delete": []
        },
        {
            "action": "call fake pastor",
            "preconds": ["fake pastor responds to post asking you to call him"],
            "add": ["talking to fake pastor"],
            "delete": ["fake pastor responds to post asking you to call him"]
        },
        {
            "action": "post on facebook asking for help",
            "preconds": ["you conform to societal pressures"],
            "add": ["fake pastor responds to post asking you to call him"],
            "delete": []
        },
        {
            "action": "give fake pastor money",
            "preconds": ["you have money"],
            "add": ["fake pastor has your money"],
            "delete": ["you have money"]
        }
    ]
}
 


if __name__ == '__main__':
    # Use GPS to solve the problem formulated above.
    actionSequence = [ 
        gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
        ),
    ]
    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')
