import re                        # Introduce necessary function libraries 
GCpattern = 'GGGCGG'             # Define the composition of GC box
Original = open('tata_genes.fa', 'r') # Read previous filtered file
out = open('tata_gc_genes.fa', 'w')   # Create a new file
genename = ""
sequence = ""                    # Variable initialization
for line in Original:            # Read line by line
    line = line.strip()          # Keep useful characters
    if line.startswith('>'):     # Judge whether the current line is a "gene name line"
        if sequence != '':       # If read the last sequence, process it
            hasgc = re.search(GCpattern, sequence)# If you have read the last sequence, process it
            if hasgc:            # Perform matching processing
                out.write(genename + '\n')
                out.write(sequence + '\n')
        genename = line          # gene name line already clean, no need to split
        sequence = ''            # Clear the old sequence for a new start
    else:
        sequence = sequence + line    # Splice the current line into the DNA sequence
#   Process the last line separately
if sequence != '':
    has_gc = re.search(GCpattern, sequence)
    if has_gc:
        out.write(genename + '\n')
        out.write(sequence + '\n')
Original.close()
out.close()                      # Close both files