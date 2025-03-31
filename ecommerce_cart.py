def valsum(d):
    if not d:
	print("cart is empty")
	return
    if len(d)<=5:
        print(f'Total Price:{sum(d.values())}')
    else:
        print(f'Total Price:{sum(d.values())*0.9}')
        
s=valsum({'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500,'Comp':30000})
