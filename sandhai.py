import streamlit as st
import pandas as pd

# Sample Farmer Data (can be stored in a CSV or database)
farmer_data = {
    'Farmer Name': ['SELVARAJ', 'SAMANDHI', 'MOORTHY'],
    'Product': ['Apples', 'Tomatoes', 'Rice'],
    'Price per kg': [50, 30, 90],
    'Quantity Available': [100, 150, 100],
    'Contact': ['9876543210', '9876543211', '7010629198'],
}

# Convert to a DataFrame for displaying
df_farmer = pd.DataFrame(farmer_data)

# Header for the App
st.title('MM_SANDHAI')
st.title('FARMERS MARKET')
st.text('Direct from Farm to Your Home')

# Add a section for farmer registration and product listing
st.header('Farmer Registration and Product Listing')

# Farmer Registration Form
with st.form(key='farmer_form'):
    farmer_name = st.text_input('Farmer Name')
    product_name = st.text_input('Product Name')
    price_per_kg = st.number_input('Price per kg', min_value=0)
    quantity_available = st.number_input('Quantity Available (kg)', min_value=0)
    contact = st.text_input('Contact Number')

    # Submit button
    submit_button = st.form_submit_button(label='List Product')

    if submit_button:
        new_product = pd.DataFrame({
            'Farmer Name': [farmer_name],
            'Product': [product_name],
            'Price per kg': [price_per_kg],
            'Quantity Available': [quantity_available],
            'Contact': [contact]
        })
        # Append the new product to the farmer data (you can save to a CSV or database in a real app)
        df_farmer = pd.concat([df_farmer, new_product], ignore_index=True)
        st.success(f'Product {product_name} listed successfully!')

# Show available products to buyers
st.header('Available Products')
search_term = st.text_input('Search for products (e.g., Apples, Tomatoes)', '')
filtered_data = df_farmer[df_farmer['Product'].str.contains(search_term, case=False)]

# Display products
if not filtered_data.empty:
    st.dataframe(filtered_data)
else:
    st.write('No products found.')

# Contact Farmer Button (Optional)
if not filtered_data.empty:
    for index, row in filtered_data.iterrows():
        if st.button(f'Contact {row["Farmer Name"]} for {row["Product"]}', key=index):
            st.write(f'Contact {row["Farmer Name"]} at {row["Contact"]} for more details or to place an order.')
else:
    st.write('Search for products to contact farmers.')

st.text('Powered By MUKESH MOORTHY')

