




class DivisionMachine(object):
    '''
    A representation of a finite state machine. This machine takes a number represented
    as a binary string and returns the remainder of input / 3
    For this machine, we will treat the first state as the start state, and all states
    are valid accepting states
    '''

    def __init__(self):
        self.state_transitions = {
            'S0': {
                '0': 'S0',
                '1': 'S1',
            },
            'S1': {
                '0': 'S2',
                '1': 'S0',
            },
            'S2': {
                '0': 'S1',
                '1': 'S2',
            },
        }

        self.outputs = {
            'S0': 0,
            'S1': 1,
            'S2': 2,
        }
        self.initial_state = 'S0'

    def evaluate(self, input):
        '''
        runs an input string through the finite state machine, computing the remainder
        of the input divided by 3

        :param input: binary string representation of an integer
        :return: input modulo 3
        '''

        if not isinstance(input, str):
            raise ValueError('Expected String input, got {}'.format(type(input)))
        current_state = self.initial_state
        for char in input:
            try:
                current_state = self.state_transitions[current_state][char]
            except KeyError:
                raise ValueError('Illegal input: {}'.format(char))
        return self.outputs[current_state]





