def DNA_strand(dna):
    return dna.replace("A", "t")\
              .replace("T", "a")\
              .replace("C", "g")\
              .replace("G", "c").upper()