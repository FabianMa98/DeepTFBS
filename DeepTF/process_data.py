import numpy as np

class protein_seq_ohe():

    def __init__(self, sequence):
        self._sequence = sequence

        self.alphabet = ['-', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                          'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                            'V', 'W', 'Y']
        self.mask = '-'
        self.MAX_LENGTH = 1000

        self._pad_sequence()
        self.encoder_table()

    @property
    def sequence(self):
        return self._sequence
    
    @sequence.setter
    def sequence(self, other_seq):
        self._sequence = other_seq

    def _pad_sequence(self):
        assert type(self._sequence) == str
        assert type(self._mask) == str
        self.padded_sequence = self._sequence[:self.MAX_LENGTH] if len(self._sequence) > self.MAX_LENGTH else self._sequence + self.mask * (self.MAX_LENGTH - len(self._sequence))

        return self.padded_sequence

    def encoder_table(self):
        onehot_encoder_identity = np.eye(N = len(self.padded_sequence))
        if self.mask:
            idx = self.alphabet.index(self.mask)
            for i, elem in enumerate(onehot_encoder_identity[idx]):
                if elem == 1:
                    onehot_encoder_identity[idx][i] = 0
        self.encode_lookup = {}
        for i, item in enumerate(self.alphabet):
            self.encode_lookup[item] = list(onehot_encoder_identity[i])

        return self.encode_lookup
    
    def ohe_padded_sequence(self):
        
        seq = seq.upper()
        self.encoded_seq = np.zeros(shape = (len(seq), len(self.encode_lookup)))
        for i, item in enumerate(seq):
            if item in self.encode_lookup.keys():
                self.encoded_seq[i] = self.encode_lookup[item]
            else:
                self.encoded_seq[i] = self.encode_lookup[self.mask] # replace with mask

        return self.encoded_seq
