def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<=0:
        print("Freezing")
    if temp>=1 and temp<=10:
        print("Very Cold")
    if temp>=11 and temp<=20:
        print("Cold")
    if temp>=21 and temp<=30:
        print("Narmal")
    if temp>=31 and temp<=40:
        print("Hot")
    if temp>=40:
        print("Very Hot")
main(21)
main(-4)