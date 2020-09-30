import os

class FileDict(dict):
    """
    File based dict sub-class
    filepath [str]: path to the core file of the dict
    """
    #defines the separator for all FileDict objects
    SEP = ":" 
    def __init__(self,filepath,**kwargs):
        """Constructor method"""
        #defines the variables
        self.filepath = filepath
        self.dict = {}

        file = open(self.filepath, 'r')
        
        file_text = file.read()
        lines = file_text.split("\n")
        lines.remove("")
        
        for line in lines:
            key, value = line.split(self.SEP)
            self.dict[key] = value
        
    def __setitem__(self, key, value):
        """Creates a new item in the dict"""
        '''self.dict[key] = value
    
        file = (self.filepath, 'a')
        
        file_text = file.read()
        lines = file_text.split("\n")
        lines.remove("")
        '''
        
    
    def pop(self,key):
        """Removes an item by the key"""
        pass
    
    def __del__(self):
        """Delete the dict and the file"""
        pass

file_dict = FileDict("dicio.txt")
#print(file_dict.dict['chave1'])
print(file_dict)
#print(dickt.file_text)
