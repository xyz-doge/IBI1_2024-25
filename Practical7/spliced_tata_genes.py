import re                        # Introduce necessary function libraries 
splicepattern = input("Enter splice site pattern (GTAG, GCAG, or ATAC): ") # Get user input
Original = open('tata_genes.fa', 'r')        # Read previous filtered file
output_filename = splicepattern + '_spliced_genes.fa'  # Create output file name
out = open(output_filename, 'w')             # Create a new file

genename = ""
sequence = ""                    # Variable initialization
for line in Original:            # Read line by line
    line = line.strip()          # Keep useful characters
    if line.startswith('>'):     # Judge whether the current line is a "gene name line"
        if sequence != '':       # If read the last sequence, process it
            has_splice = splicepattern in sequence  # Check if splice pattern exists
            if has_splice:       # Perform matching processing
                out.write(genename + '\n')
                out.write(sequence + '\n')
        genename = line          # gene name line already clean, no need to split
        sequence = ''            # Clear the old sequence for a new start
    else:
        sequence = sequence + line    # Splice the current line into the DNA sequence

#   Process the last line separately
if sequence != '':
    has_splice = splicepattern in sequence
    if has_splice:
        out.write(genename + '\n')
        out.write(sequence + '\n')

Original.close()
out.close()                      # Close both files