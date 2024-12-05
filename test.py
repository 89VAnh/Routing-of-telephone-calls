import unittest

from main import OperatorTrie


class TestOperatorTrie(unittest.TestCase):
    def setUp(self):
        """Set up the test environment with operators and their price lists."""
        self.operator_trie = OperatorTrie()
        self.operator_trie.add_operator(
            "Operator A",
            {
                "1": 0.9,
                "268": 5.1,
                "46": 0.17,
                "4620": 0.0,
                "468": 0.15,
                "4631": 0.15,
                "4673": 0.9,
                "46732": 1.1,
            },
        )
        self.operator_trie.add_operator(
            "Operator B",
            {
                "1": 0.92,
                "44": 0.5,
                "46": 0.2,
                "467": 1.0,
                "48": 1.2,
                "46731": 0.9,
                "2384": 0.32,
            },
        )

    def test_cheapest_operator(self):
        """Test finding the cheapest operator for valid numbers."""
        self.assertEqual(
            self.operator_trie.find_cheapest_operator("4673212345"), "Operator B"
        )
        self.assertEqual(
            self.operator_trie.find_cheapest_operator("4681234567"),
            "Operator A",
        )
        self.assertEqual(
            self.operator_trie.find_cheapest_operator("44123456789"),
            "Operator B",
        )

    def test_no_matching_prefix(self):
        """Test handling of phone numbers without any matching prefix."""
        self.assertIsNone(self.operator_trie.find_cheapest_operator("9991234567"))

    def test_edge_cases(self):
        """Test edge cases like empty phone numbers and prefixes."""
        self.assertIsNone(self.operator_trie.find_cheapest_operator(""))
        self.assertIsNone(self.operator_trie.find_cheapest_operator("000"))

    def test_invalid_phone_number(self):
        """Test handling of phone numbers with non-numeric characters."""
        self.assertIsNone(self.operator_trie.find_cheapest_operator("4673ABC1234"))
        self.assertIsNone(self.operator_trie.find_cheapest_operator("4673#1234"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
