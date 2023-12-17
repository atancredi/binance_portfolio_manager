from typing import List, Dict

from constants import CoinPair

class Portfolio:

    defined_pairs: List[Dict[CoinPair, float]]

    def __init__(self, dict):
        self.defined_pairs = []
        for key in dict:
            self.defined_pairs.append({
                key: dict[key]
            })