from collections import List, Tuple

class Calculator:
    def __init__(self, data = []):
        self.__data = data
        pass
    
    def __set_data(self, new_data, add_data):
        if new_data:
            self.__data = new_data
        if add_data:
            self.__data += add_data
        
    def mean(
        self, 
        new_data: List = None, 
        add_data = None):
        """
         平均
        """
        
        self.__set_data(new_data, add_data)
        pass
    
    def median(
            self,
            new_data: List = None, 
            add_data = None):
        """
         中央値
        """
        
        self.__set_data(new_data, add_data)
        pass
    
    def variance(
            self,
            new_data: List = None, 
            add_data = None):
        """
         分散
        """
        
        self.__set_data(new_data, add_data)
        pass


    def stdev(
            self,
            new_data: List = None, 
            add_data = None):
        """
         標準偏差
        """
        
        self.__set_data(new_data, add_data)
        pass
    
calculator: Calculator = Calculator()
