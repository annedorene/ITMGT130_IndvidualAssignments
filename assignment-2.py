
'''Assignment 2
This assignment covers your proficiency with Python's data structures.
It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
'''

def relationship_status(from_member, to_member, social_graph):
    '''
    Item 1.
    Relationship Status. 10 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-2-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Write your code below this line

def relationship_status(from_member, to_member, social_graph):
	to_follows_from = False;
	from_follows_to = False;
	#from_member is in following list of to
	if from_member in social_graph[to_member]["following"]:
		to_follows_from = True;
	#to_member is in following list of from
	if to_member in social_graph[from_member]["following"]:
		from_follows_to= True;

	if from_follows_to and to_follows_from:
		return "friends"
	elif from_follows_to:
		return "follower"
	elif to_follows_from:
		return "followed by"
	else:
		return "no relationship"

def tic_tac_toe(board):
    '''
    Item 2.
    Tic Tac Toe. 10 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-2-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Write your code below this line

def tic_tac_toe(board):
    l = len(board)

    if l == 3:
        for i in range(l):
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]

        for i in range(l):
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]

        if board[0][0] == board[1][1] == board[2][2]:

            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:

            return board[1][1]
        else:
            return "NO WINNER"

    if l == 4:
        for i in range(l):
            if board[i][0] == board[i][1] == board[i][2] == board[i][3]:
                return board[i][0]

        for i in range(l):
            if board[0][i] == board[1][i] == board[2][i] == board[3][i]:
                return board[0][i]

        if board[0][0] == board[1][1] == board[2][2] == board[3][3]:

            return board[0][0]
        elif board[0][3] == board[1][2] == board[2][1] == board[3][0]:

            return board[0][3]
        else:
            return "NO WINNER"

    if l == 5:
        for i in range(l):
            if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4]:
                return board[i][0]

        for i in range(l):
            if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i]:
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]:

            return board[0][0]
        elif board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]:

            return board[0][4]
        else:
            return "NO WINNER"

    if l == 6:
        for i in range(l):
            if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == board[i][5]:
                return board[i][0]

        for i in range(l):
            if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == board[5][i]:
                return board[0][i]

        if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == board[5][5]:

            return board[0][0]
        elif board[0][5] == board[1][4] == board[2][3] == board[3][2] == board[4][1] == board[5][0]:

            return board[0][5]
        else:
            return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''
    Item 3.
    ETA. 10 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "assignment-2-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Write your code below this line


def eta(first_stop, second_stop, route_map):
    i = 0
    first_stop_found = False
    second_stop_found = False

    total_eta = 0
    keys = list(route_map.keys())
    while not (first_stop_found and second_stop_found):
        if i >= len(keys):
            i = 0

        if keys[i][0] == first_stop:
            first_stop_found = True
            total_eta = route_map[keys[i]]['travel_time_mins']
            print('First stop: %s %d' % (keys[i][0] + '-' + keys[i][1], route_map[keys[i]]['travel_time_mins']))
        elif first_stop_found:

            if keys[i][1] == second_stop:
                total_eta += route_map[keys[i]]['travel_time_mins']
                second_stop_found = True
                print('Last stop: %s %d' % (keys[i][0] + '-' + keys[i][1], route_map[keys[i]]['travel_time_mins']))
            else:
                total_eta += route_map[keys[i]]['travel_time_mins']
                print('Next stop: %s %d' % (keys[i][0] + '-' + keys[i][1], route_map[keys[i]]['travel_time_mins']))
        i += 1
    return total_eta








