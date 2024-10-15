###when the same operator is allowed to have different meaning according to the context.

print([1,2,3,4] + [5,6,7,8]) #merge
print("zahid" + "saeed") # concatenate
### All of the above shows operator overloading

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()