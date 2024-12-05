import re
from typing import Dict, Tuple, Optional


class TrieNode:
    """A single node in the Trie."""

    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.price: Optional[float] = None


class Trie:
    """A Trie data structure for storing prefixes and their prices."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefix: str, price: float):
        """Insert a prefix and its associated price into the Trie."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.price = price

    def find_longest_prefix_price(self, phone_number: str) -> Optional[float]:
        """
        Find the price of the longest matching prefix for a given phone number.
        Returns None if no prefix matches.
        """
        node = self.root
        longest_price = None

        for char in phone_number:
            if char in node.children:
                node = node.children[char]
                if node.price is not None:
                    longest_price = node.price
            else:
                break

        return longest_price


class OperatorTrie:
    """Handles multiple operators using Tries."""

    def __init__(self):
        self.tries: Dict[str, Trie] = {}

    def add_operator(self, operator_name: str, price_list: Dict[str, float]):
        """Add an operator and its price list."""
        trie = Trie()
        for prefix, price in price_list.items():
            trie.insert(prefix, price)
        self.tries[operator_name] = trie

    def is_valid_phone_number(self, phone_number: str) -> bool:
        """Validate if the phone number contains only digits."""
        return bool(re.match(r"^\d+$", phone_number))

    def find_cheapest_operator(self, phone_number: str) -> Optional[Tuple[str, float]]:
        """
        Find the cheapest operator for a given phone number.
        Returns None if no operator has a matching prefix.
        """
        if not self.is_valid_phone_number(phone_number):
            return None

        cheapest_operator = None
        cheapest_price = float("inf")

        for operator_name, trie in self.tries.items():
            price = trie.find_longest_prefix_price(phone_number)
            if price is not None and price < cheapest_price:
                cheapest_operator = operator_name
                cheapest_price = price

        return cheapest_operator


if __name__ == "__main__":
    operator_trie = OperatorTrie()
    operator_trie.add_operator(
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
    operator_trie.add_operator(
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
    result = operator_trie.find_cheapest_operator("4673212345")
    print(result)
