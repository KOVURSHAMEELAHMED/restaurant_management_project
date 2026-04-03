from django.test import TestCase

# Replace 'Mexican' with a cuisine type in your database
mexican_items = MenuItem.get_items_by_cuisine('Mexican')

print(f"Found {mexican_items.count()} items.")
for item in mexican_items:
    print(item.name)