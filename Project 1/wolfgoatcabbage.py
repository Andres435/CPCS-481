from search import Problem, depth_first_graph_search, breadth_first_graph_search

class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset(('F', 'W', 'G', 'C')), goal=set()):
        # Define the initial and goal states as frozensets.
        super().__init__(initial, goal)

    def goal_test(self, state):
        return True if state==set(self.goal) else False

    def result(self, state, action):
        # Calculate the new state based on the action
        if action.issubset(state):
            new_state = state - action
        else:
            new_state = state | action
        return frozenset(new_state)

    def actions(self, state):
        # Set the given state to a set for easy manipulation
        state=set(state)

        # Algo to solve the W-G-C problem 
        possible_actions = [{'F'}, {'F','G'}, {'W','F'}, {'C','F'}] 
        if state == {'F', 'G', 'W', 'C'}:
            possible_actions = [{'F','G'}]
        elif state == {'F', 'C', 'W'}:
            possible_actions = [{'F', 'W'}, {'F','C'}]
        elif state == {'F', 'G', 'W'}:
            possible_actions = [{'F','W'}]
        elif state == {'W', 'C'}:
            possible_actions = [{'F'}]
        elif state == {'W', 'G'}:
            possible_actions = [{'F'}]
        elif state == {'F', 'G'}:
            possible_actions = [{'F', 'G'}]
        elif state == {'F', 'C'}:
            possible_actions = [{'F'}, {'F','C'}] 
        elif state == {'F', 'W'}:
            possible_actions = [{'F'}, {'F','W'}]
        elif state == {'W'}:
            possible_actions = [{'F', 'G'}]
        elif state == {'G'}:
            possible_actions = [{'F'}, {'F','W'}, {'F','C'}]
        elif state == {'C'}:
            possible_actions = [{'F','G'}]
        elif state == {'F'}:
            possible_actions = [{'F'}]

        return possible_actions


if __name__ == '__main__':
    wgc = WolfGoatCabbage()

    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)