"""
    This module implements the simple blocks world using PAIP GPS.
"""
from gps import gps
import copy 

# Formulate the problem states and actions.
problem = {

    'initial': ['space on a', 'a on b', 'b on c', 'c on table1', 'space on table1'],
    'goal': ['space on c', 'c on b', 'b on a', 'a on table1', 'space on table1'],

    'actions': [
         ### block A's moves ###
        {
            'action': 'move a from table3 to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on table3'
            ],
            'add': [
                'a on table2',
                'space on table3'
            ],
            'delete': [
                'a on table3',
                'space on table2'
            ]
        },
        {
            'action': 'move a from table3 to table1',
            'preconds': [
                'space on a',
                'space on table1',
                'a on table3'
            ],
            'add': [
		'space on table3',
                'a on table1'
            ],
            'delete': [
                'space on table1',
                'a on table3'
            ]
        },
        {
            'action': 'move a from table3 to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table3'
            ],
            'add': [
                'a on b',
                'space on table3'
            ],
            'delete': [
                'space on b',
                'a on table3'
            ]
        },
 	{
            'action': 'move a from table3 to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table3'
            ],
            'add': [
                'a on c',
                'space on table3'
            ],
            'delete': [
                'space on c',
                'a on table3'
            ]
        },
        {
            'action': 'move a from table2 to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on table2'
            ],
            'add': [
                'a on table3',
                'space on table2'
            ],
            'delete': [
                'space on table3',
                'a on table2'
            ]
        },
	{
            'action': 'move a from table1 to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on table1'
            ],
            'add': [
                'a on table3',
                'space on table1'
            ],
            'delete': [
                'space on table3',
                'a on table1'
            ]
        },
	    {
            'action': 'move a from b to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on b'
            ],
            'add': [
                'a on table3',
                'space on b'
            ],
            'delete': [
                'space on table3',
                'a on b'
            ]
        },
	    {
            'action': 'move a from c to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on c'
            ],
            'add': [
                'a on table3',
                'space on c'
            ],
            'delete': [
                'space on table3',
                'a on c'
            ]
        },
	    {
            'action': 'move a from table2 to table1',
            'preconds': [
                'space on a',
                'space on table1',
                'a on table2'
            ],
            'add': [
                'a on table1',
                'space on table2'
            ],
            'delete': [
                'space on table1',
                'a on table2'
            ]
        },
        {
            'action': 'move a from table2 to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table2'
            ],
            'add': [
                'a on b',
                'space on table2'
            ],
            'delete': [
                'space on b',
                'a on table2'
            ]
        },
        {
            'action': 'move a from table2 to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table2'
            ],
            'add': [
                'a on c',
                'space on table2'
            ],
            'delete': [
                'space on c',
                'a on table2'
            ]
        },
    	{
            'action': 'move a from table1 to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on table1'
            ],
            'add': [
                'a on table2',
                'space on table1'
            ],
            'delete': [
                'space on table2',
                'a on table1'
            ]
        },
        {
            'action': 'move a from b to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on b'
            ],
            'add': [
                'a on table2',
                'space on b'
            ],
            'delete': [
                'space on table2',
                'a on b'
            ]
        },
        {
            'action': 'move a from c to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on c'
            ],
            'add': [
                'a on table2',
                'space on c'
            ],
            'delete': [
                'space on table2',
                'a on c'
            ]
        },
        {
            'action': 'move a from b to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on b'
            ],
            'add': [
                'a on c',
                'space on b'
            ],
            'delete': [
                'a on b',
                'space on c'
            ]
        },
        {
            'action': 'move a from table1 to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table1'
            ],
            'add': [
                'a on b'
            ],
            'delete': [
                'a on table1',
                'space on b'
            ]
        },
        {
            'action': 'move a from b to table1',
            'preconds': [
                'space on a',
                'space on table1',
                'a on b'
            ],
            'add': [
                'a on table1',
                'space on b'
            ],
            'delete': [
                'a on b'
            ]
        },
        {
            'action': 'move a from c to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on c'
            ],
            'add': [
                'a on b',
                'space on c'
            ],
            'delete': [
                'a on c',
                'space on b'
            ]
        },
        {
            'action': 'move a from table1 to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table1'
            ],
            'add': [
                'a on c'
            ],
            'delete': [
                'a on table1',
                'space on c'
            ]
        },
        {
            'action': 'move a from c to table1',
            'preconds': [
                'space on a',
                'space on table1',
                'a on c'
            ],
            'add': [
                'a on table1',
                'space on c'
            ],
            'delete': [
                'a on c'
            ]
        },
        ### block B's moves ###
        {
            'action': 'move b from table3 to table2',
            'preconds': [
                'space on b',
                'space on table2',
                'b on table3'
            ],
            'add': [
                'b on table2',
                'space on table3'
            ],
            'delete': [
                'b on table3',
                'space on table2'
            ]
        },
        {
            'action': 'move b from table3 to table1',
            'preconds': [
                'space on b',
                'space on table1',
                'b on table3'
            ],
            'add': [
		'space on table3',
                'b on table1'
            ],
            'delete': [
                'space on table1',
                'b on table3'
            ]
        },
        {
            'action': 'move b from table3 to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on table3'
            ],
            'add': [
                'b on a',
                'space on table3'
            ],
            'delete': [
                'space on a',
                'b on table3'
            ]
        },
 	{
            'action': 'move b from table3 to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on table3'
            ],
            'add': [
                'b on c',
                'space on table3'
            ],
            'delete': [
                'space on c',
                'b on table3'
            ]
        },
        {
            'action': 'move b from table2 to table3',
            'preconds': [
                'space on b',
                'space on table3',
                'b on table2'
            ],
            'add': [
                'b on table3',
                'space on table2'
            ],
            'delete': [
                'space on table3',
                'b on table2'
            ]
        },
	{
            'action': 'move b from table1 to table3',
            'preconds': [
                'space on b',
                'space on table3',
                'b on table1'
            ],
            'add': [
                'b on table3',
                'space on table1'
            ],
            'delete': [
                'space on table3',
                'b on table1'
            ]
        },
	    {
            'action': 'move b from a to table3',
            'preconds': [
                'space on b',
                'space on table3',
                'b on a'
            ],
            'add': [
                'b on table3',
                'space on a'
            ],
            'delete': [
                'space on table3',
                'b on a'
            ]
        },
	    {
            'action': 'move b from c to table3',
            'preconds': [
                'space on b',
                'space on table3',
                'b on c'
            ],
            'add': [
                'b on table3',
                'space on c'
            ],
            'delete': [
                'space on table3',
                'b on c'
            ]
        },
	    {
            'action': 'move b from table2 to table1',
            'preconds': [
                'space on b',
                'space on table1',
                'b on table2'
            ],
            'add': [
                'b on table1',
                'space on table2'
            ],
            'delete': [
                'space on table1',
                'b on table2'
            ]
        },
        {
            'action': 'move b from table2 to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on table2'
            ],
            'add': [
                'b on a',
                'space on table2'
            ],
            'delete': [
                'space on a',
                'b on table2'
            ]
        },
        {
            'action': 'move b from table2 to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on table2'
            ],
            'add': [
                'b on c',
                'space on table2'
            ],
            'delete': [
                'space on c',
                'b on table2'
            ]
        },
    	{
            'action': 'move b from table1 to table2',
            'preconds': [
                'space on b',
                'space on table2',
                'b on table1'
            ],
            'add': [
                'b on table2',
                'space on table1'
            ],
            'delete': [
                'space on table2',
                'b on table1'
            ]
        },
        {
            'action': 'move b from a to table2',
            'preconds': [
                'space on b',
                'space on table2',
                'b on a'
            ],
            'add': [
                'b on table2',
                'space on a'
            ],
            'delete': [
                'space on table2',
                'b on a'
            ]
        },
        {
            'action': 'move b from c to table2',
            'preconds': [
                'space on b',
                'space on table2',
                'b on c'
            ],
            'add': [
                'b on table2',
                'space on c'
            ],
            'delete': [
                'space on table2',
                'b on c'
            ]
        },
        {
            'action': 'move b from a to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on a'
            ],
            'add': [
                'b on c',
                'space on a'
            ],
            'delete': [
                'b on a',
                'space on c'
            ]
        },
        {
            'action': 'move b from table1 to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on table1'
            ],
            'add': [
                'b on a'
            ],
            'delete': [{
            'action': 'move a from table3 to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on table3'
            ],
            'add': [
                'a on table2',
                'space on table3'
            ],
            'delete': [
                'a on table3',
                'space on table2'
            ]
        },
        {
            'action': 'move a from table3 to table1',
            'preconds': [
                'space on a',
                'space on table1',
                'a on table3'
            ],
            'add': [
		'space on table3',
                'a on table1'
            ],
            'delete': [
                'space on table1',
                'a on table3'
            ]
        },
        {
            'action': 'move a from table3 to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table3'
            ],
            'add': [
                'a on b',
                'space on table3'
            ],
            'delete': [
                'space on b',
                'a on table3'
            ]
        },
 	{
            'action': 'move a from table3 to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table3'
            ],
            'add': [
                'a on c',
                'space on table3'
            ],
            'delete': [
                'space on c',
                'a on table3'
            ]
        },
        {
            'action': 'move a from table2 to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on table2'
            ],
            'add': [
                'a on table3',
                'space on table2'
            ],
            'delete': [
                'space on table3',
                'a on table2'
            ]
        },
	{
            'action': 'move a from table1 to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on table1'
            ],
            'add': [
                'a on table3',
                'space on table1'
            ],
            'delete': [
                'space on table3',
                'a on table1'
            ]
        },
	    {
            'action': 'move a from b to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on b'
            ],
            'add': [
                'a on table3',
                'space on b'
            ],
            'delete': [
                'space on table3',
                'a on b'
            ]
        },
	    {
            'action': 'move a from c to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on c'
            ],
            'add': [
                'a on table3',
                'space on c'
            ],
            'delete': [
                'space on table3',
                'a on c'
            ]
        },
	    {
            'action': 'move a from table2 to table1',
            'preconds': [
                'space on a',
                'space on table1',
                'a on table2'
            ],
            'add': [
                'a on table1',
                'space on table2'
            ],
            'delete': [
                'space on table1',
                'a on table2'
            ]
        },
        {
            'action': 'move a from table2 to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table2'
            ],
            'add': [
                'a on b',
                'space on table2'
            ],
            'delete': [
                'space on b',
                'a on table2'
            ]
        },
        {
            'action': 'move a from table2 to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table2'
            ],
            'add': [
                'a on c',
                'space on table2'
            ],
            'delete': [
                'space on c',
                'a on table2'
            ]
        },
    	{
            'action': 'move a from table1 to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on table1'
            ],
            'add': [
                'a on table2',
                'space on table1'
            ],
            'delete': [
                'space on table2',
                'a on table1'
            ]
        },
        {
            'action': 'move a from b to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on b'
            ],
            'add': [
                'a on table2',
                'space on b'
            ],
            'delete': [
                'space on table2',
                'a on b'
            ]
        },
        {
            'action': 'move a from c to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on c'
            ],
            'add': [
                'a on table2',
                'space on c'
            ],
            'delete': [
                'space on table2',
                'a on c'
            ]
        },
                'b on table1',
                'space on a'
            ]
        },
        {
            'action': 'move b from a to table1',
            'preconds': [
                'space on b',
                'space on table1',
                'b on a'
            ],
            'add': [
                'b on table1',
                'space on a'
            ],
            'delete': [
                'b on a'
            ]
        },
        {
            'action': 'move b from c to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on c'
            ],
            'add': [
                'b on a',
                'space on c'
            ],
            'delete': [
                'b on c',
                'space on a'
            ]
        },
        {
            'action': 'move b from table1 to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on table1'
            ],
            'add': [
                'b on c'
            ],
            'delete': [
                'b on table1',
                'space on c'
            ]
        },
        ### block C's moves ####
        {
            'action': 'move c from table3 to table2',
            'preconds': [
                'space on c',
                'space on table2',
                'c on table3'
            ],
            'add': [
                'c on table2',
                'space on table3'
            ],
            'delete': [
                'c on table3',
                'space on table2'
            ]
        },
        {
            'action': 'move c from table3 to table1',
            'preconds': [
                'space on c',
                'space on table1',
                'c on table3'
            ],
            'add': [
		'space on table3',
                'c on table1'
            ],
            'delete': [
                'space on table1',
                'c on table3'
            ]
        },
        {
            'action': 'move c from table3 to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on table3'
            ],
            'add': [
                'c on a',
                'space on table3'
            ],
            'delete': [
                'space on a',
                'c on table3'
            ]
        },
 	{
            'action': 'move c from table3 to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on table3'
            ],
            'add': [
                'c on b',
                'space on table3'
            ],
            'delete': [
                'space on b',
                'c on table3'
            ]
        },
        {
            'action': 'move c from table2 to table3',
            'preconds': [
                'space on c',
                'space on table3',
                'c on table2'
            ],
            'add': [
                'c on table3',
                'space on table2'
            ],
            'delete': [
                'space on table3',
                'c on table2'
            ]
        },
	{
            'action': 'move c from table1 to table3',
            'preconds': [
                'space on c',
                'space on table3',
                'c on table1'
            ],
            'add': [
                'c on table3',
                'space on table1'
            ],
            'delete': [
                'space on table3',
                'c on table1'
            ]
        },
	    {
            'action': 'move c from a to table3',
            'preconds': [
                'space on c',
                'space on table3',
                'c on a'
            ],
            'add': [
                'c on table3',
                'space on a'
            ],
            'delete': [
                'space on table3',
                'c on a'
            ]
        },
	    {
            'action': 'move c from b to table3',
            'preconds': [
                'space on c',
                'space on table3',
                'c on b'
            ],
            'add': [
                'c on table3',
                'space on c'
            ],
            'delete': [
                'space on table3',
                'c on b'
            ]
        },
	    {
            'action': 'move c from table2 to table1',
            'preconds': [
                'space on c',
                'space on table1',
                'c on table2'
            ],
            'add': [
                'c on table1',
                'space on table2'
            ],
            'delete': [
                'space on table1',
                'c on table2'
            ]
        },
        {
            'action': 'move c from table2 to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on table2'
            ],
            'add': [
                'c on a',
                'space on table2'
            ],
            'delete': [
                'space on a',
                'c on table2'
            ]
        },
        {
            'action': 'move c from table2 to c',
            'preconds': [
                'space on c',
                'space on b',
                'c on table2'
            ],
            'add': [
                'c on b',
                'space on table2'
            ],
            'delete': [
                'space on b',
                'c on table2'
            ]
        },
    	{
            'action': 'move c from table1 to table2',
            'preconds': [
                'space on c',
                'space on table2',
                'c on table1'
            ],
            'add': [
                'c on table2',
                'space on table1'
            ],
            'delete': [
                'space on table2',
                'c on table1'
            ]
        },
        {
            'action': 'move c from a to table2',
            'preconds': [
                'space on c',
                'space on table2',
                'c on a'
            ],
            'add': [
                'c on table2',
                'space on a'
            ],
            'delete': [
                'space on table2',
                'c on a'
            ]
        },
        {
            'action': 'move c from b to table2',
            'preconds': [
                'space on c',
                'space on table2',
                'c on b'
            ],
            'add': [
                'c on table2',
                'space on b'
            ],
            'delete': [
                'space on table2',
                'c on b'
            ]
        },
        {
            'action': 'move b from c to table1',
            'preconds': [
                'space on b',
                'space on table1',
                'b on c'
            ],
            'add': [
                'b on table1',
                'space on c'
            ],
            'delete': [
                'b on c'
            ]
        },
        {
            'action': 'move c from a to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on a'
            ],
            'add': [
                'c on b',
                'space on a'
            ],
            'delete': [
                'c on a',
                'space on b'
            ]
        },
        {
            'action': 'move c from table1 to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on table1'
            ],
            'add': [
                'c on a'
            ],
            'delete': [
                'c on table1',
                'space on a'
            ]
        },
        {
            'action': 'move c from a to table1',
            'preconds': [
                'space on c',
                'space on table1',
                'c on a'
            ],
            'add': [
                'c on table1',
                'space on a'
            ],
            'delete': [
                'c on a'
            ]
        },
        {
            'action': 'move c from b to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on b'
            ],
            'add': [
                'c on a',
                'space on b'
            ],
            'delete': [
                'c on b',
                'space on a'
            ]
        },
        {
            'action': 'move c from table1 to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on table1'
            ],
            'add': [
                'c on b'
            ],
            'delete': [
                'c on table1',
                'space on b'
            ]
        },
        {
            'action': 'move c from b to table1',
            'preconds': [
                'space on c',
                'space on table1',
                'c on b'
            ],
            'add': [
                'c on table1',
                'space on b'
            ],
            'delete': [
                'c on b'
            ]
        }
    ]
}


if __name__ == '__main__':
    # Use GPS to solve the problem formulated above.
    problemA = copy.deepcopy(problem)
    problemB = copy.deepcopy(problem)

    problemA['initial'] = ['space on table1', 'b on table2', 'space on b', 'space on c', 'c on a', 'a on table3']
    problemB['initial'] = ['space on a', 'a on table1', 'space on b', 'b on table2', 'space on c', 'c on table3']

    problemA['goal'] = ['space on b', 'b on table1', 'space on a', 'a on table2', 'space on c', 'c on table3']
    problemB['goal'] = ['space on table3', 'space on table2', 'c on table1', 'b on c', 'a on b', 'space on a']

    actionSequence = [ 
        
        gps(
        problemA['initial'],
        problemA['goal'],
        problemA['actions']
        ),
        gps(
        problemB['initial'],
        problemB['goal'],
        problemB['actions']
        ),
    ]
    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print("*******")
            print(action)
            print("*******")
    else:
        print('plan failure...')
