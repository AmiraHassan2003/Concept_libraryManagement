
import mysql.connector
from mysql.connector import Error

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "", 
    "database": "LibraryManagementSystem"
}

class DatabaseConnection:
    @staticmethod
    def connect():
        try:
            connection = mysql.connector.connect(**db_config)
            # print("Connected to database!")
            return connection
        except Error as e:
            # print(f"Error: {e}")
            return None

############################# BasicFunction ##############################################3
class BasicFunction:

    @staticmethod
    def lenArr(arr): 
        if not arr:
            return 0
        else :
            return 1 + BasicFunction.lenArr(arr[1:])

    @staticmethod
    def addToEnd(arr, value): # append() [1 2 3 4] 5  =>  [1] + [2 3 4] => [1 2] + [3 4]
        if not arr:
            return [value]
        return [arr[0]] + BasicFunction.addToEnd(arr[1:], value)


    def getIndexFromList(self, arr, value, index=0):
        if index >= self.lenArr(arr):
            # print("Sorry, this ID is invalid.")
            return -1
        if arr[index] == value:
            return index
        return self.getIndexFromList(arr, value, index + 1)


    def getAllIndicesFromList(self, arr, value, index=0):
        if index >= self.lenArr(arr):
            return []
        if arr[index] == value:
            return [index] + self.getAllIndicesFromList(arr, value, index + 1)
        return self.getAllIndicesFromList(arr, value, index + 1)
    

    def custom_map(self, func, arr): 
        if not arr:
            return []        
        return [func(arr[0])] + self.custom_map(func, arr[1:])