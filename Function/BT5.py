def Calculate_discounted_price(price,percent):
    return price+price*(percent/100)

price = int(input("Nhập giá: "))
percent = int(input("Nhập chiết khấu: "))

print(f"Giá sau khi chiết khấu là {Calculate_discounted_price(price,percent)}")