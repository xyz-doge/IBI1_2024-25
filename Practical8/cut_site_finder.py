#   Define the function for identifying the identification site
def find_cut_sites(DNA, site):
    for base in DNA + site:
#   Exclude characters that do not comply with biological regulations
        if base not in "ATCG":
            return "The sequence does not conform to biological laws" 
    positions = []                          # Create an empty list
#   Starting from scratch, detect the given sequence according to the required cutting template
    for i in range(len(DNA) - len(site) + 1):
        if DNA[i:i+len(site)] == site:
            positions.append(i)
    return positions
#   Collect user input data
DNAseq = input("Please enter the DNA sequence (including only A/T/C/G):")
cut_site = input("Please enter the enzyme recognition site sequence:")
print("The location where the locus appears:", find_cut_sites(DNAseq, cut_site))