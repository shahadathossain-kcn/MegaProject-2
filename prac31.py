#WAP using function to convert Celcius to Fahrenheit.

def convert_ctf(celcius):
    fahrenheit = 1.8* celcius + 32
    print(fahrenheit)

convert_ctf(int(input("Enter celcius temp. : ")))