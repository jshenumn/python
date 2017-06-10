#Python Experiment


###================== Example of class ===============###
class OilMarket:
    """A simple class example"""
    #private member variable
    __inventory = 100
    __price     = 48.29

    #public methods
    def __init__(self, inventory, price):
        self.__inventory = inventory
        self.__price     = price

    def getInventory(self):
        return self.__inventory

    def getPrice(self):
        return self.__price




if __name__ == "__main__":
   midEast = OilMarket(89, 51.32)
   print(midEast.getInventory())
   print(midEast.getPrice())

