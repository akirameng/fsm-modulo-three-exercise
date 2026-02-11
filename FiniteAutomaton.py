class FiniteAutomaton:
    """
    Generic Finite State Machine (FSM).

    A reusable finite automaton implementation that can be configured
    with arbitrary states, input symbols, initial state, accepting states and transition logic.

    Example:
        # States
        S0, S1, S2 = "S0", "S1", "S2"

        # Transition function
        def transition(state, symbol):
            transitions = {
                (S0, "0"): S0, (S0, "1"): S1,
                (S1, "0"): S2, (S1, "1"): S0,
                (S2, "0"): S1, (S2, "1"): S2,
            }
            return transitions[(state, symbol)]

        fsm = FiniteAutomaton(
            states={S0, S1, S2},
            input_symbols={"0", "1"},
            initial_state=S0,
            accepting_states={S0, S1, S2},
            transition_function=transition,
        )

        final_state = fsm.run("1101")
    """

    def __init__(
        self,
        states,
        input_symbols,
        initial_state,
        accepting_states,
        transition_function
    ):
        """
        Initialize a finite automaton.

        Args:
            states (set): All possible states.
            input_symbols (set): Valid input symbols.
            initial_state: Starting state.
            accepting_states (set): Valid final states.
            transition_function (callable): (state, symbol) -> next_state
        """
        self.states = states
        self.input_symbols = input_symbols
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transition_function = transition_function

        self._validate_configuration()

    def run(self, inputs):
        """
        Process a sequence of input symbols and return the final state.
        Raises:
            ValueError: If an input symbol is invalid or the transition
                    function is undefined for a given (state, symbol) pair.
        """
        current_state = self.initial_state

        for symbol in inputs:
            self._validate_input_symbol(symbol)

            # safely attempt to get next state
            try:
                next_state = self.transition_function(current_state, symbol)
            except Exception as e:
                raise ValueError(
                    f"Transition undefined for state={current_state}, symbol={symbol}"
                ) from e
            
            # validate that the transition function returned a valid state
            if next_state not in self.states:
                raise ValueError(
                        f"Transition returned invalid state '{next_state}' "
                        f"for state={current_state}, symbol={symbol}"
                ) 
            current_state = next_state

        return current_state

    def is_accepting(self, state):
        """
        Return True if the given state is an accepting state.
        """
        return state in self.accepting_states

    # -----------------------------
    # Internal validation helpers
    # -----------------------------

    def _validate_configuration(self):
        if self.initial_state not in self.states:
            raise ValueError("Initial state must be a valid state.")

        if not self.accepting_states.issubset(self.states):
            raise ValueError("Accepting states must be a subset of states.")

    def _validate_input_symbol(self, symbol):
        if symbol not in self.input_symbols:
            raise ValueError(f"Invalid input symbol: {symbol}")
