import re                        # Introduce necessary function libraries
TATApattern = 'TATA[AT]A[AT]'    # Define the composition of TATA
Original = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') # Read original file
out = open('tata_genes.fa', 'w') # Create a new file
genename = ""
sequence = ""                    # Variable initialization
for line in Original:            # Read line by line
    line = line.strip()          # Keep useful characters
    if line.startswith('>'):     # Judge whether the current line is a "gene name line"
        if sequence != '':       # If read the last sequence, process it
            hastata = re.search(TATApattern, sequence)# If you have read the last sequence, process it
            if hastata:          # Perform matching processing
                out.write(genename + '\n')
                out.write(sequence + '\n')
        parts = line.split()     # Take apart the line of gene name
        genename = '>' + parts[0][1:] # Extract clean gene names
        sequence = ''            # Clear the old sequence for a new start
    else:
        sequence = sequence + line    # Splice the current line into the DNA sequence
Original.close()
out.close()                      # Close both files
