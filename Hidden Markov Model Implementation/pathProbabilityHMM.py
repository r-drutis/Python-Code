import numpy as np
import pandas as pd


class PathProbability:
    
    """
    Build Transition Matrix
    Input: states, data
    Returns: transition (matrix dataframe)
    """
    def buildTransition(states, data):
        # Initialize matrix 
        matSize = len(states)
        t_data = np.zeros((matSize,matSize))
        
        # Clean up the input
        for i in range(0, len(states)):  
            letter = states[i]
            rawData = data[3+i]
            rawData = rawData.replace(letter, "")
            rawData = rawData.split()
            
            for j in range(0,len(states)):    
                t_data[i][j] = rawData[j]
        
        # Build dataframe
        transition = pd.DataFrame(t_data, index=states, columns=states)
        return transition          
    
    """
    Main Program
    """
    if __name__ == "__main__":
        # Get file to work with
        data = []
        with open("C:/Users/Rob/Desktop/hmmProbability.txt") as f:
            for line in f:
                if "-" not in line:
                    data = data + [line.rstrip("\r\n")]    
        
        # Read data from file
        path = data[0]
        states = data[1].split()
                
        #Build transition matrix
        t_Mat = buildTransition(states, data)
        
        # Calculate probability of Hidden Path
        path_prob = 0.5
        
        for i in range(0, len(path)-1):
            # Get current state and next state
            stNow = path[i]         # current state
            stNext = path[i+1]      # next state
            
            # Calculate the probability of moving from current to next
            path_prob *= t_Mat.get_value(stNow, stNext)
        
        # Print result
        print(path_prob)