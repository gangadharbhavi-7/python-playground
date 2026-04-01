class Complex:
    def __init__(self,real,imaginary):

        self.real=real
        self.imaginary=imaginary
def add_complex(c1, c2):
    real_sum = c1.real + c2.real
    imag_sum = c1.imaginary + c2.imaginary
    return Complex(real_sum, imag_sum)
def main():
    N = int(input("Enter the number of complex numbers (N >= 2): "))
    if N < 2:
        print("You must enter at least 2 complex numbers.")
        return

    # Read first complex number
    real = int(input("Enter real part of complex number 1: "))
    imag = int(input("Enter imaginary part of complex number 1: "))
    total = Complex(real, imag)

    # Read remaining complex numbers and add them
    for i in range(2, N+1):
        real = int(input(f"Enter real part of complex number {i}: "))
        imag = int(input(f"Enter imaginary part of complex number {i}: "))
        c = Complex(real, imag)
        total = add_complex(total, c)

    print("Sum of complex numbers =", total)

# Run program
main()

    