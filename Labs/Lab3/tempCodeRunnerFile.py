def DNA_letters(DNA: str) -> bool:
    '''
    Checks if a given string is a DNA sequence
    '''
    nucleotide_check: bool = True
    nucleotides: list[str] = ["A", "C", "T", "G"]
    for char in DNA:
        if (not (char == nucleotide for nucleotide in nucleotides)):
            nucleotide_check = False
    return nucleotide_check