 class Dataset:
    def __init__(self,name,data):
        self.name=name
        self.data=data
        
    def mean(self):
        result=sum(self.data)/len(self.data)
        print(f"The mean of the list of numbers is {result}")
    
    def max_value(self):
        print(f"Max Data= {max(self.data)}")
        
    def min_value(self):
        print(f"Min Data={min(self.data)}")

data=[10,20,30,40,50]
d1=Dataset("Mydata",data)
d1.mean()
d1.max_value()
d1.min_value()

