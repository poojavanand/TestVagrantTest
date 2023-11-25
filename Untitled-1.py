import numpy
i=0
pro=input("product name")
unit=[1100,900,200,100]
gst=[18,12,28,0]
quantity=[1,4,3,2]
for i in pro:
    s=5%unit[i]
    while unit>500:
        a=gst[i]-s[i]
        b=print(max(gst))
print("product which paid max:",b)
for i in b:
        total=unit[i]*gst[i]*quantity[i]
print("total amount to be paid is:",total)
        
