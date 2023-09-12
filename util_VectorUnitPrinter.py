import numpy as np

def MakeStringWithUnits(arr, unit):
    
    try:
        vals = ""
        
        for i in range(len(arr)):
            vals += str(arr[i])
            if (isinstance(arr[0], np.int32)):
                vals += unit
            else:
                vals += (" " + unit)

            if (i < len(arr)-1):
                vals += ", "

        return ("[" + vals + "]")
    
    except:
        print(Error)
        return None

def PrintWithUnits(arr, unit):
    
    try:
        
        string = MakeStringWithUnits(arr, unit)
        
        print(string)
        
    except:
        print("Error")