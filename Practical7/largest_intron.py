seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re
matches = re.findall('GT[ACGT]*?AG', seq)
if matches:
    longest = max(matches, key=len)
    print("The longest intron is:", longest)
    print("Its length is:", len(longest))
else:
    print("No matching fragments were found.")