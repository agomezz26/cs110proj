import json

class person:
    def __init__(self,name,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10):
        self.name=name
        self.q1=q1
        self.q2=q2
        self.q3=q3
        self.q4=q4
        self.q5=q5
        self.q6=q6
        self.q7=q7
        self.q8=q8
        self.q9=q9
        self.q10=q10
        

    def __str__(self):
    	return str(self.q1)+str(self.q2)+str(self.q3)+str(self.q4)+str(self.q5)+str(self.q6)+str(self.q7)+str(self.q8)+str(self.q9)+str(self.q10)


    def match(self, date):
        num=0
        if(self.q1==date.q1):
            num+=1
        if(self.q2==date.q2):
            num+=1
        if(self.q3==date.q3):
            num+=1
        if(self.q4==date.q4):
            num+=1
        if(self.q5==date.q5):
            num+=1
        if(self.q6==date.q6):
            num+=1
        if(self.q7==date.q7):
            num+=1
        if(self.q8==date.q8):
            num+=1
        if(self.q9==date.q9):
            num+=1
        if(self.q10==date.q10):
            num+=1
       
        return str(((10000*(num/10))//1)/100)+"% Match"

def main():
    jfile=open('people.json','r').read()
    bfile=open('barb.json','r').read()
    adam = person("adam",jfile[2],jfile[7],jfile[12],jfile[17],jfile[22],jfile[27],jfile[32],jfile[37],jfile[42],jfile[47])
    barb = person("barb",bfile[2],bfile[7],bfile[12],bfile[17],bfile[22],bfile[27],bfile[32],bfile[37],bfile[42],bfile[47])
    print(adam)
    print(barb)
    print(adam.match(barb))
    

main()
