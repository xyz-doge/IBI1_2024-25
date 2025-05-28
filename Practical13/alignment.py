#   Define the function for reading FASTA files
def read_fasta(filename):
    sequence = ""
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence

#   Define the function for reading the BLOSUM62 matrix
def read_blosum62(filename):
    blosum = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
    #   Find the header of the matrix
    header = []
    for line in lines:
        if line.startswith(" "):  #  Header row
            header = line.split()
            break
    #   Store data in a dictionary
    for line in lines:
        if line.startswith(" ") or line.startswith("#"):
            continue
        parts = line.split()
        row_aa = parts[0]
        scores = parts[1:]
        for col_aa, score in zip(header, scores):
            blosum[(row_aa, col_aa)] = int(score)
    return blosum

#   Define the function for performing sequence alignment
def align_sequences(seq1, seq2, blosum):
    score = 0
    matches = 0
    length = min(len(seq1), len(seq2))      #  Prevent errors caused by different lengths

    for i in range(length):
        aa1 = seq1[i]
        aa2 = seq2[i]
        if aa1 == aa2:
            matches += 1
        score += blosum.get((aa1, aa2), 0)  #  If encountering unknown characters, score 0

    identity = (matches / length) * 100
    return score, identity

#   Main program
def main():
    #  Read sequence
    human = read_fasta("human_sod2.fasta")
    mouse = read_fasta("mouse_sod2.fasta")
    random_seq = read_fasta("random_sequence.fasta")

    #  Read BLOSUM62 matrix
    blosum = read_blosum62("BLOSUM62.txt")

    #  Compare 3 sets of sequences
    pairs = [
        ("Human vs Mouse", human, mouse),
        ("Human vs Random", human, random_seq),
        ("Mouse vs Random", mouse, random_seq)
    ]

    for name, seq1, seq2 in pairs:
        score, identity = align_sequences(seq1, seq2, blosum)
        print(f"{name}:")
        print(f" BLOSUM62 score = {score}")
        print(f" Percentage of identical amino acids = {identity:.2f}%\n")
main()