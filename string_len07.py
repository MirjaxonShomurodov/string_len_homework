def main(x1,x2,x3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    n1=len(x1)
    n2=len(x2)
    n3=len(x3)

    s="["
    if n1%2==1:
        s+=x1+","
    if n2%2==1:
        s+=x2+","
    if n3%2==1:
        s+=x3+","

    s=s.strip(",")
    s+="]"
    return s
s1="coodeschool.uz"
s2="example"
s3="python"
print(main(s1,s2,s3))