
print(42)
print("42")
print(42.0)

# ALL written in strings with the same name _text at the end
product_name = "Wireless Mouse"
price_text = "29.99"
quantity_text = "3"
tax_rate_text = "0.08"

# convert above into each type (from being strings)
price = float(price_text)
quantity = int(quantity_text)
tax_rate = float(tax_rate_text)

#calculation after the conversion 
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# check to see if the conversion and calculation is working fine.
print(f"Product: {product_name}")
print(f"Price: ${price} * {quantity}")
print(f"Subtotal: ${subtotal:.2f}") # :.2f meaning two demical places
print(f"Tax ${tax_rate * 100}%): ${tax:.2f}")
print(f"Total: ${total:.2f}")