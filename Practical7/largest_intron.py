seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'    # Define the sequence that needs to be processed
import re                                     # Introduce necessary function libraries
matches = re.findall('GT[ACGT]*?AG', seq)     # Match the target sequence
if matches:
    longest = max(matches, key=len)           # Find the longest one among these sequences
    print("The longest intron is:", longest)
    print("Its length is:", len(longest))
else:
    print("No matching fragments were found.")# Output results for two different scenarios