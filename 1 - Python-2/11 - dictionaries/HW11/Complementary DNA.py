def DNA_strand(dna):
    dct = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return "".join([dct[letter] for letter in dna])