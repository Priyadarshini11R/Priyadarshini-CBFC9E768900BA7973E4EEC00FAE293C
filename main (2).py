def linear_search_product(product_list, target_product):
  indices = []

  for i, product in enumerate(product_list):
      if product == target_product:
          indices.append(i)

  return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Banana", "Grapes", "Banana", "Apple"]
target_product = "Banana"

result = linear_search_product(products, target_product)

if result:
  print(f"The product '{target_product}' was found at indices: {result}")
else:
  print(f"The product '{target_product}' was not found.")

