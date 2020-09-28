import os

class FileDict(dict):
  """
  File based dict sub-class
  filepath [str]: path to the core file of the dict
  """
    def __init__(self,filepath,**kwargs):
      """Constructor method"""
      pass
        
    def __setitem__(self, key, value):
      """Creates a new item in the dict"""
      pass

    def pop(self,key):
      """Removes an item by the key"""
      pass

    def __del__(self):
      """Delete the dict and the file"""
      pass
