import unittest
from FiniteAutomaton import FiniteAutomaton

class TestFiniteAutomaton(unittest.TestCase):

    def setUp(self):
        # Simple FSM for testing: toggles between A and B on '0' and '1'
        self.A, self.B = "A", "B"
        self.states = {self.A, self.B}
        self.input_symbols = {"0", "1"}
        self.initial_state = self.A
        self.accepting_states = self.states

        def transition(state, symbol):
            if state == self.A:
                return self.B
            else:
                return self.A

        self.fsm = FiniteAutomaton(
            states=self.states,
            input_symbols=self.input_symbols,
            initial_state=self.initial_state,
            accepting_states=self.accepting_states,
            transition_function=transition
        )

    def test_run_normal(self):
        # A -> B -> A
        self.assertEqual(self.fsm.run(["0", "1"]), self.A)
        # B -> A -> B
        self.assertEqual(self.fsm.run(["1", "0", "1"]), self.B)

    def test_is_accepting(self):
        self.assertTrue(self.fsm.is_accepting(self.A))
        self.assertTrue(self.fsm.is_accepting(self.B))
        self.assertFalse(self.fsm.is_accepting("C"))

    def test_invalid_input_symbol(self):
        with self.assertRaises(ValueError):
            self.fsm.run(["0", "2"])  # '2' is invalid

    def test_incomplete_transition(self):
        # FSM with missing transition
        def bad_transition(state, symbol):
            if state == self.A and symbol == "0":
                return self.B
            # Missing other transitions
            return None

        fsm_bad = FiniteAutomaton(
            states=self.states,
            input_symbols=self.input_symbols,
            initial_state=self.A,
            accepting_states=self.accepting_states,
            transition_function=bad_transition
        )

        with self.assertRaises(ValueError):
            fsm_bad.run(["0", "1"])  # 1 -> None should raise

    def test_invalid_configuration(self):
        # initial_state not in states
        with self.assertRaises(ValueError):
            FiniteAutomaton(
                states=self.states,
                input_symbols=self.input_symbols,
                initial_state="C",
                accepting_states=self.accepting_states,
                transition_function=lambda s, c: s
            )

        # accepting_states not subset
        with self.assertRaises(ValueError):
            FiniteAutomaton(
                states=self.states,
                input_symbols=self.input_symbols,
                initial_state=self.A,
                accepting_states={"A", "C"},
                transition_function=lambda s, c: s
            )


if __name__ == "__main__":
    unittest.main()
