def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a%100==a and a%2==1:
        print("ikki xonali toq son")
    if a%100==a and a%2==0:
        print("ikki xonali juft son")
    if a%1000==a and a%2!=0:
        print("uch xonali toq son")
    if a%100==a and a%2==0:
        print("uch xonali juft son")
main(57)
main(124)