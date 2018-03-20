import numpy as np
import pandas as pd


class HiddenPathFinder:
    
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
            rawData = data[9+i]
            rawData = rawData.replace(letter, "")
            rawData = rawData.split()    
            
            for j in range(0,len(states)):    
                t_data[i][j] = rawData[j]
        
        # Build dataframe
        transition = pd.DataFrame(t_data, index=states, columns=states)
        return transition      
    
    
    """
    Build Emission Matrix
    Input: alpha, states, data
    Returns: emission (matrix dataframe)
    """    
    def buildEmission(alpha, states, data):
        # Initialize matrix 
        matX = len(alpha)
        matY = len(states)
        e_data = np.zeros((matY,matX))
        
        # Clean up the input
        for i in range(0, len(states)):  
            letter = states[i]
            rawData = data[9+i]
            rawData = rawData.replace(letter, "")
            rawData = rawData.split()    
            
            for j in range(0,len(alpha)):
                e_data[i][j] = rawData[j]   
                
        emission = pd.DataFrame(e_data, index=states, columns=alpha)      
   
        return emission
    
    """
    Main Program
    """
    if __name__ == "__main__":
        # Get file to work with
        data = []
        with open("C:/Users/Rob/Desktop/hmmtest.txt") as f:
            for line in f:
                data = data + [line.rstrip("\r\n")]
        
        # Read data from file
        emission = data[0]
        alpha = data[2].split()
        path = data[4]
        states = data[6].split()
        
        #Build transition matrix
        t_Mat = buildTransition(states, data)
        em_Mat = buildEmission(alpha, states, data)
                
        print(t_Mat)
        print(em_Mat)
    
    