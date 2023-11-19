import re
from collections import defaultdict
import pandas as pd
import numpy as np



class SimpleTokenizer:
    def __init__(self):
        self.token_to_id = defaultdict(lambda: len(self.token_to_id))
        self.token_to_id['<PAD>'] = 0  # Padding token

    def tokenize(self, text):
        # Simple tokenization by splitting on non-word characters
        tokens = re.findall(r'\w+|\S', text)
        return tokens
    
    def merge_strings(self, input_values):
        target_array = []
        for i in input_values:
            result = " ".join(i)
            target_array.append(i)

        return target_array

    def convert_tokens_to_ids(self, tokens):
        return [self.token_to_id[token] for token in tokens]

    def tokenize_column(self, series):
        # Apply tokenization to each row in the pandas series
        tokenized = series.apply(self.tokenize)
        return tokenized
    
    def run_convert(self):
        pass

