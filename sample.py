def dis_calc(unit_price,quantity):
    amount = quantity * unit_price
    if unit_price >= 500 :
        discount = 0.05 * amount
        f_amount = amount- discount
        return f_amount
    else:
        return amount
def gst_cal(amount,gst):
    gst = amount * float(gst/100)

    return gst

product_list = [["Leather wallet",1100,18,1],["Umbrella",900,12,4],["cigarette",200,28,3],["Honey",100,0,2]]
length = len(product_list)
fprice = []
mgst = []
final_amt = []
for i in range(length):
    #for j in range(i+1):
    result1 = dis_calc(product_list[i][1],product_list[i][3])
    result2 = gst_cal(result1,product_list[i][2])
    fprice1 = result1 + result2
    final_amt.append(fprice1)
    mgst.append(result2)
print("final amount to be payed",sum(final_amt))
print("maximum gst is ",max(mgst),"for the product",product_list[1][0])