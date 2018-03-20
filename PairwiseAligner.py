#import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

"""
Generates a Needleman-Wunch Dynamic Programming Matrix
This is a prototype, and not yet functional
Things to be fixed:
- implement pandas dataframe to replace matplotlib
- implement csv support to read scoring matrix from csv files
- implement smith-waterman alignment, possibly other alignment algorithms
- GUI?
"""
class PairwiseAligner:
    
    def createMat(width, height, gap):
        # Construct blank matrix using sequence length as dimensions
        matrix = np.zeros((height,width),dtype=int)
        # Fill in penalty rows and columns
        for i in range(1, height):
            matrix[i,0] = i*(gap)
        for j in range(1, width):
            matrix[0,j] = j*(gap)            
        return matrix 

    # Calculates values for Pairwise Alignment
    def calcPairWise(preMatrix, gap, width, height, sq1, sq2):
        postMatrix = preMatrix      # matrix to calculate values for
        # alignment values to calculate each step
        diag = 0                 
        up = 0
        left = 0    
        
        for i in range(1, height):              # calculate by column
            for j in range(1, width):           # calculate by row
                
                diag = postMatrix[i-1,j-1] + 1  # calc diagonal value
                up = postMatrix[i-1,j] + gap    # calc up value
                left = postMatrix[i,j-1] + gap  # calc left value
                
                postMatrix[i,j] = max(diag, up, left)   # final value is the max of the three values
        return postMatrix    

    def plotMatrix(matrix, s1, s2):
        # Format for Labels
        s1Label = ["Seq1"]
        s1Label = s1Label + s1
        s2Label = ["Seq2"]
        s2Label = s2Label + s2 
        
        fig, ax = plt.subplots()
        
        for i in range(len(s1Label)):
            for j in range(len(s2Label)):
                c = matrix[i][j]
                ax.text(i, j, str(c), va='center', ha='center') 
        ax.set_facecolor('white')
        ax.matshow(matrix)
        
        
        # Set Axis ticks to show nucleotide sequence
        x_pos = np.arange(len(s1Label)) 
        plt.xticks(x_pos, s1Label)          # X-axis uses Sequence 1 String
        y_pos = np.arange(len(s2Label))
        plt.yticks(y_pos, s2Label)          # Y-Axis uses Sequence 2 String    
                
        plt.show()
     
    """
    Main Program
    """           
        
    if __name__ == "__main__":

        # Sequences to be aligned
        seq1 = "ATCGTG"
        seq2 = "ATCGTC"
        seq1Row = [*seq1]   # sequence row
        seq2Col = [*seq2]   # sequence column

        gapPenalty = -5     # gap penalty

        # dimensions of the matrix based on sequence length
        mX = len(seq1) + 1   
        mY = len(seq2) + 1  

        # Generate Dynamic Programming Matrix
        dpMatrix = createMat(mX, mY, gapPenalty)
        dpMatrix = calcPairWise(dpMatrix, gapPenalty, mX, mY, seq1Row, seq2Col)

        # Display Matrix
        plotMatrix(dpMatrix, seq1Row, seq2Col)
