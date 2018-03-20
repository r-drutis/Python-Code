
"""
ClumpFinder
Finds clumps of k-mers, generates a frequency index to decrease runtime
Input: A DNA sequence or genome, k-mer of length k, reading frame, clump size t
Output: K-mers which occur more than t times in a frame
"""

class ClumpFinder:

	# Convert nucleotide sequence to index number
	def patternToNumber(pattern):
	    
	    if not pattern: # base case
	        return 0
	    symbol = pattern[-1:]
	    prefix = pattern[0:-1]
	    # recursively strip symbol from end of string
	    return 4 * patternToNumber(prefix) + symbolToNumber(symbol)

	# Convert nucleotide to base 4 number
	def symbolToNumber(char):
	    
	    if char == 'A':
	        return 0
	    if char == 'C':
	        return 1
	    if char == 'G':
	        return 2
	    if char == 'T':
	        return 3

	# Convert number to sequence of nucleotides
	def numberToPattern(index, k):
	    
	    if k == 1:  # base case
	        return numberToSymbol(index)
	    prefixIndex = index // 4
	    remainder = index % 4
	    symbol = numberToSymbol(remainder)
	    prefixPattern = numberToPattern(prefixIndex, k-1)
	    return str(prefixPattern) + str(symbol)
	    
	# Convert number to nucleotide
	def numberToSymbol(num):
	    
	    if num == 0:
	        return 'A'
	    if num == 1:
	        return 'C'
	    if num == 2:
	        return 'G'
	    if num == 3:
	        return 'T'
	    
	# Generate Frequency Array for sequence given k-mer length
	def computeFrequencies(text, k): 
	    frequencyArray = []
	    t_length = len(text) - k + 1
	    
	    for i in range(4**k):   # generate blank frequency index
	        frequencyArray.append(0)
	    # store the occurence of each k-mer in its corresponding index
	    for i in range(t_length):
	        pattern = text[i:k+i]
	        j = patternToNumber(pattern)
	        frequencyArray[j] += 1
	    return frequencyArray
	            
	    
	# Compute clumps in a given sequence given k-mer length
	def findClumps(genome, k, frame, t):
	    frequentPatterns = set()
	    clump = [] 
	    r_length = len(genome) - frame + 1
	    
	    # generate frequency array for clump
	    for i in range(4**k):
	        clump.append(0)
	    # move across genome and index clumps
	    text = genome[0:frame]
	    frequencyArray = computeFrequencies(text,k)
	    for i in range(4**k):
	        if frequencyArray[i] >= t:
	                clump[i] = 1
	    for i in range(1, r_length):
	        firstPattern = genome[i-1:i-1+k]
	        index = patternToNumber(firstPattern)
	        frequencyArray[index] -= 1
	        
	        lastPattern = genome[i+frame-k:i+frame]
	        index = patternToNumber(lastPattern)
	        frequencyArray[index] += 1
	        
	        if frequencyArray[index] >= t:
	            clump[index] = 1
	    
	    for i in range(4**k):
	        if clump[i] == 1:
	            pattern = numberToPattern(i, k)
	            frequentPatterns.add(pattern)
	    return(frequentPatterns)

	result = str(findClumps('', 9, 500, 3))
	result = result.strip('{}')
	result = result.replace(',', '')
	result = result.replace("'", "")
	print(result)
        
    
    