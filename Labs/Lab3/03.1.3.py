long_chain: str = input("Input long chain of DNA : ")
short_chain: str = input("Input short chain of DNA : ")

long_lenght: int = 20
short_lenght: int = 3 

def DNA_letters(DNA: str) -> bool:
    '''
    Checks if a given string is a DNA sequence
    '''
    nucleotide_check: bool = True
    nucleotides: list[str] = ["A", "C", "T", "G"]
    for char in DNA:
        if (char not in nucleotides):
            nucleotide_check = False
    return nucleotide_check


def check_DNA (DNA: str, lenght: int) -> bool:
    lenght_check: bool = len(DNA) == lenght
    letters_check: bool = DNA_letters(DNA)
    return lenght_check and letters_check

if(not check_DNA(long_chain,long_lenght)):
    raise ValueError  ("Wrong dna sequence,\n\
                        long chain should have lenght 20 instead of {}\n\
                        valid characters : 'A', 'C', 'T', 'G' ".format(len(long_chain)))
if(not check_DNA(short_chain,short_lenght)):
    raise ValueError  ("Wrong dna sequence,\n\
                        short chain should have lenght 3 instead of {}\n\
                        valid characters : 'A', 'C', 'T', 'G' ".format((len(short_chain))))

short_chain_found = long_chain.find(short_chain)

if(short_chain_found != -1): 
    print ("The long chain of DNA contains the short chain of DNA in position {}\n\
            The short chain is found {} times in the long chain".format(short_chain_found,long_chain.count(short_chain)))