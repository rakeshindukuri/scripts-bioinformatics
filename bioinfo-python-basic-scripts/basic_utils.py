def dna_to_rna(dna):
    rna = ""
    for bp in dna:
        rna += bp.replace('T', 'U')
    return rna

def main():
    """
    Testing all functions in utils
    :return:
    """
    dna = "ATGC"
    rna = dna_to_rna(dna)
    print(rna)

if __name__ == "__main__":
    main()

# yet to include hamming and fib rabbit,