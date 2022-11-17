def reverse_comp(seq):

    seq = seq.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
    seq = seq.upper()
    seq = seq[::-1]
    return seq

def main():
    seq = input("Enter/ Paste the sequence to calculate reverse complement:\n")
    print("Your sequence: ", seq)
    # Add right aligned text to print seq
    print("Reverse complement of the sequence is: ", reverse_comp(seq))


if __name__ == "__main__":
    main()