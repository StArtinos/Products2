#importing required libraries
import streamlit as st
import json

#reading the json file
with open('database.json', 'r') as f:
    data = json.load(f)

#displaying input form
product_name = st.text_input('Enter Product Name')
ingredients = st.text_input('Enter Ingredients (separated by comma)')

#saving input to json file
if st.button('Save'):
    data[product_name] = ingredients.split(',')
    with open('database.json', 'w') as f:
        json.dump(data, f)

#displaying list of ingredient names
ingredient_names = list(data.keys())

#text input for filtering ingredient names
filter_text = st.text_input('Filter Ingredient Names')

#filtering ingredient names based on the input
filtered_ingredient_names = [name for name in ingredient_names if filter_text.lower() in name.lower()]

#displaying filtered ingredient names
selected_ingredient = st.selectbox('Select Ingredient', filtered_ingredient_names)

#displaying product name and its ingredients
if selected_ingredient:
    st.write('Product Name:', selected_ingredient)
    st.write('Ingredients:', ', '.join(data[selected_ingredient]))

def main():
    with open('database.json', 'r') as file:
        data = json.load(file)

    search_query = st.text_input('Search for a product', key='search_input')

    if search_query:
        search_results = [product for product in data.keys() if search_query.lower() in product.lower()]
        st.write('Search Results:', search_results)

    selected_products = st.multiselect('Select products', list(data.keys()), key='product_selector')

    if selected_products:
        joint_ingredients = list(set().union(*[data[product] for product in selected_products]))
        st.write(', '.join(joint_ingredients))
main()
