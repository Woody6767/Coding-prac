#this is my first ever solo attempted code, lets see
#used to find PV, FV, PMT, I/Y

#def get_inputs():
FV = int(input("Please enter the future value: "))
I = float(input("Please enter the interest rate: "))
Y = int(input("Please enter the years it will be invested for: "))
k = int(input("Enter how frequently this is compounded (enter 1 for annually; 2 for semi-annual; and 4 for quarterly): "))


def pv(FV, Y, I, k):
    r = float(I/k)/100
    t = k * Y
    PV = FV/(1+r)**t
    return PV

def main():
    PV = pv(FV, Y, I, k)
    print(round(PV, 2))
    
main()
