import re                        # Introduce necessary function libraries 
TATApattern = 'TATA[AT]A[AT]'    # Define the composition of TATA box
splicepattern = input("Enter splice site pattern (GTAG, GCAG, or ATAC): ") # Get user input
Original = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') # Read original file
output_filename = splicepattern + '_spliced_genes.fa'  # Create output file name
out = open(output_filename, 'w') # Create a new file
genename = ""
sequence = ""                    # Variable initialization
for line in Original:            # Read line by line
    line = line.strip()          # Keep useful characters
    if line.startswith('>'):     # Judge whether the current line is a "gene name line"
        if sequence != '':       # If read the last sequence, process it
            hastata = re.search(TATApattern, sequence)  # Check for TATA box
            has_splice = re.search(f'{splicepattern[:2]}[ATGC]*{splicepattern[2:]}', sequence) # Check if splice pattern exists
            if hastata and has_splice:          # Perform double matching
                out.write(f'{genename} count: {len(re.findall(TATApattern, sequence))}' + '\n')
                out.write(sequence + '\n')
        parts = line.split()     # Take apart the line of gene name
        genename = '>' + parts[0][1:] # Extract clean gene names
        sequence = ''            # Clear the old sequence for a new start
    else:
        sequence = sequence + line              # Splice the current line into the DNA sequence
#   Process the last line separately
if sequence != '':
    hastata = re.search(TATApattern, sequence)  # Check for TATA box
    has_splice = re.search(f'{splicepattern[:2]}[ATGC]*{splicepattern[2:]}', sequence) # Check if splice pattern exists
    if hastata and has_splice:                  # Final double matching
        out.write(f'{genename}  count: {len(re.findall(TATApattern, sequence))}' + '\n')
        out.write(sequence + '\n')
Original.close()
out.close()                      # Close both files