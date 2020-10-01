import os

'''
chave1:elemento1
chave2:elemento2
chave2:elemento3
chave4:elemento4
'''

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
        try:
            self.filepath = filepath
            super().__init__(kwargs)
    
            file = open(self.filepath, 'r')
            
            file_text = file.read()
            lines = file_text.split("\n")
            
            #the doc may have a empty line, this would generate an error
            try:
                lines.remove("")
            except ValueError:
                pass

            for line in lines:
                try:
                    key, value = line.split(self.SEP)
                    self[key] = value
                except ValueError:
                    pass
                    
            file.close()
             
        except FileNotFoundError:
            file = open(self.filepath, "w")
            file.close()
            #print("File not found")
            pass

        #add the kwargs to the file      
        if kwargs != {}:

            file = open(self.filepath, "r")
            file_text = file.read()
            file.close()

            file = open(self.filepath, 'w')
            for key in kwargs:
                file_text += str("\n" + key + self.SEP + kwargs.get(key, None))
                
            file.write(file_text)        
            file.close()
            
        
        
    def __setitem__(self, key, value):
        """Creates a new item in the dict"""
        super().__setitem__(key, value)
        #self[key] = value

        file = open(self.filepath, 'r')
            
        file_text = file.read()
        lines = file_text.split("\n")
        file.close()

        dict_element = str(key + self.SEP + value)

        if dict_element not in lines:
            file = open(self.filepath, 'a')
            file.write("\n" + dict_element)
            file.close()
        
        
    def pop(self,key):
        """Removes an item by the key"""
        try:
            value = super().pop(key)
        
            file = open(self.filepath, 'r')
            file_text = file.read()
            lines = file_text.split("\n")
            file.close()
            file_text = ""
            for i in lines:
                if key in i:
                    pass
                else:
                    file_text += i + "\n"
                    file
            file = open(self.filepath, 'w')
            file.write(file_text)
            file.close()

            return value
        except KeyError:
            print("KeyError")

    def __del__(self):
        """Delete the dict and the file"""
        #Se tiver comentado é porque esqueci de tirar o comentário#tive que comentar pra testar se o resto estava funcionando

        os.remove(self.filepath)
        del self
        
        

#TESTES

file_dict = FileDict("dicio.txt", chave6 = "elemento6") # -->(1)
print(file_dict)
file_dict["chave5"] = "elemento5" # -->(2)
print(file_dict)
file_dict.pop('chave1') # -->(3)
print(file_dict)
file_dict = FileDict("dicioo.txt", chave6 = "elemento6")

'''
(1) Cria o dicionário
(2) Adiciona 'chave5:elemento5' ao documento e ao dicionário
(3) Remove o 'chave1:elemento1' do documento e do dicionário

'''