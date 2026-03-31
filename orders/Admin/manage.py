from home.models import MenuItem

# Create an item: $20.00 with a 15% discount
item = MenuItem.objects.create(
    name="Truffle Pasta", 
    base_price=20.00, 
    discount_percentage=15.00
)

# Test the method
print(item.get_final_price()) 
# Expected Output: 17.0