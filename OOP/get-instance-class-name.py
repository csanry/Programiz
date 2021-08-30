
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')



c1 = ComplexNumber(2, 3)

c1.holy = 'This attr used to not exist but it does now'
