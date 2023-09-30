def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2==0:
        print("musbat juft son ")
    if a>0 and a%2==1:
        print("musbat toq son ")
    if a<0 and a%2==0:
        print("manfiy juft son ")
    if a<0 and a%2==1:
        print("manfiy toq son ")
    if a==0:
        print("son 0 ga teng")
main(57)
main(-24)
main(0)