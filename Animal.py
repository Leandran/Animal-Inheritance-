class Animal:

    """

    Animal class doctring

    """

    def __init__(self,numteeth,spots,weight):
         self.numteeth = numteeth
         self.spots = spots
         self.weight = weight




class Lion(Animal):

    def sound(self):    #expanding class to have feature specific to a lion
        print("A lion make a roar sound") 

#checking to see if the lion is cub, female or male lion based on their weight.

    def lion_type(self):

        if self.weight < 80:
            print('lion is a Cub')
        elif self.weight >= 80 and self.weight <= 120:
            print('lion is a Female')
        elif self.weight > 120:
            print('lion is a Male')




class Cheetah(Animal):
    def __init__(self,numteeth,weight,spots,retractableclaws,prey):  
        self.numteeth = numteeth
        self.weight = weight
        self.spots = spots
        self.retractableclaws = retractableclaws
        self.prey = prey

    

simba = Lion(50,False,150)
simba.lion_type()
simba.sound()
print(simba.spots)



cheetah_1 = Cheetah(48,70 ,True,False,['springbok','impala','duiker'])
print(cheetah_1.numteeth)
print(cheetah_1.spots)
print(cheetah_1.prey)
