#   Define the function for identifying the restriction enzyme cut sites
def find_cut_sites(DNA, site):
    #   Check that both sequences contain only valid characters
    for base in DNA + site:
        if base not in "ATCG":
            return "Error: Sequence contains invalid characters (only A/T/C/G allowed)"
    
    positions = []  #   Create an empty list to store match positions

    #   Search for recognition site in the DNA sequence
    for i in range(len(DNA) - len(site) + 1):
        if DNA[i:i+len(site)] == site:
            positions.append(i + 1)  #   Change from 0-based to 1-based index

    return positions

#   Example usage: collect user input
DNAseq = input("Please enter the DNA sequence (including only A/T/C/G):")
cut_site = input("Please enter the enzyme recognition site sequence:")
print("The location where the locus appears:", find_cut_sites(DNAseq, cut_site))
