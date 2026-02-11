from FiniteAutomaton import FiniteAutomaton

# -----------------------------
# FSM Configuration
# -----------------------------
def create_mod_three_fsm():
    """
    Creates a FiniteAutomaton to compute modulo 3 for a binary string.
    """
    S0, S1, S2 = "S0", "S1", "S2"

    states = {S0, S1, S2}
    input_symbols = {"0", "1"}
    initial_state = S0
    accepting_states = states  # All states are valid final states for modulo computation

    def transition(state, symbol):
        if state == S0:
            return S0 if symbol == "0" else S1
        elif state == S1:
            return S2 if symbol == "0" else S0
        elif state == S2:
            return S1 if symbol == "0" else S2

    return FiniteAutomaton(states, input_symbols, initial_state, accepting_states, transition)

# -----------------------------
# Mod-3 Logic
# -----------------------------

STATE_TO_REMAINDER = {"S0": 0, "S1": 1, "S2": 2}
mod_three_fsm = create_mod_three_fsm()

def mod_three(binary_str):
    """
    Compute the remainder when a binary string is divided by 3.

    Args:
        binary_str (str): Binary string (e.g., "1101")

    Returns:
        int: Remainder modulo 3
    """
    
    # validate input before passing to FSM
    if not all(c in "01" for c in binary_str):
        raise ValueError("Input must be a binary string containing only '0' or '1'.")

    final_state = mod_three_fsm.run(list(binary_str))
    return STATE_TO_REMAINDER[final_state]

# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print(mod_three("1101"))  # => 1
    print(mod_three("1110"))  # => 2
    print(mod_three("1111"))  # => 0
