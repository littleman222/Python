actual_cost = float(Input(" Please enter the Actual Product Price: "))
sale_amount =float(input(" Please Enter the Sales Amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost 
    print("Total Profit = {0}".format(amount))
else:
    print("no Profit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")