import json

class Person3:
    def __init__(self, dictionary):
        self.dict = dictionary
        self.name = self.dict["Full Name: "]
        del self.dict["Full Name: "]
        self.gender = self.dict["Gender: "]
        del self.dict["Gender: "]
        self.state = self.dict["What state are you from? (state abbreviation): "]
        del self.dict["What state are you from? (state abbreviation): "]
        self.age = self.dict["Age: "]
        del self.dict["Age: "]
        self.bio = self.dict["Leave a personal message, or brief description of yourself"]
        del self.dict["Leave a personal message, or brief description of yourself"]


    def __str__(self):
    	return str(self.name)+str(self.gender)+str(self.state)+str(self.age)+str(self.bio)


    def match(self, date):
        num=0
        for i in self.dictionary:
            if self.dictionary[i] == other.dictionary[i]
            num += 1
        return num
    
        return str(((10000*(num/20))//1)/100)+"% Match"


