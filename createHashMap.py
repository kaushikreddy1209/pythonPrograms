
class HashTable:
    def __init__(self): # Initialize the hashtable with array size and perform list comprehension 
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]
    
    def get_hash(self,key): #Create a hash function to store alll the values
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    
    def __setitem__(self,key,val): #Fucntion to store the values of a key in the hashmap using the above hash funtion
        h=self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            print(idx, element)
            if len(element)==2 and element[0]==key:
                print(element)
                self.arr[h][idx]=(key,val)
                found=True
                break
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key): # Function to get valeus of a key
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
    
    def __delitem__(self,key): #Function to delete values for a key
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]



