class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
class LinkedList():
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def get_length(self):
        if self.head is None:
            print("Linked List is empty")
            return
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
    
        itr=self.head
        while itr.next:
            itr=itr.next
        
        itr.next=Node(data,None)
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->' if itr.next else str(itr.data)
            itr=itr.next
        print(llstr)

    def insert_values(self,dataList):
        self.head = None
        for data in dataList:
            self.insert_at_end(data)

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_beginning(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception ("Invalid index")
        
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    
    def remove_all(self):
        self.head=None
    
    def search_val(self,data):
        if self.head is None:
            raise Exception("Linked list is empty, value cannot be found")
        count=0
        itr=self.head
        while itr:
            if itr.data==data:
                return count
            count+=1
            itr=itr.next
    
    


# ll = LinkedList()
# ll.insert_values(["banana","mango","grapes","orange"])
# ll.print()
# ll.insert_at_beginning("apple")
# ll.print()
# ll.insert_at_end("jackfruit")
# ll.print()
# ll.insert_at(3,"guava")
# ll.print()
# ll.remove_at(3)
# ll.print()
# ll.remove_all()
# ll.print()
# ll.insert_values(["will","you","be","my","Valentine??", "Please say yes"])
# print(ll.search_val("Valentine"))
