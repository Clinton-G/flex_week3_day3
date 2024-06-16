descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
elec_keywords = ['smartphone', 'tablet', 'laptop']
apar_keywords = ['t-shirt', 'shirt', 'pants', 'dress']
h_k_keywords = ['kitchen', 'knife', 'cookware', 'appliance']

def tag_product(description):
    if any(keyword in description for keyword in ['smartphone', 'tablet', 'laptop']):
        return 'Electronics'
    
    elif any(keyword in description for keyword in ['t-shirt', 'shirt', 'pants', 'dress']):
        return 'Apparel'
    
    elif any(keyword in description for keyword in ['kitchen', 'knife', 'cookware', 'appliance']):
        return 'Home & Kitchen'
    
    else:
        return 'Other'

tagged_products = [tag_product(desc) for desc in descriptions]

for i, desc in enumerate(descriptions):
    print(desc, 'tag: ', tagged_products[i])