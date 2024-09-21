import requests
from bs4 import BeautifulSoup
import csv

# Function to extract product data from Flipkart
def extract_flipkart_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting product names, prices, and ratings
    product_names = [name.get_text() for name in soup.find_all('a', class_='_4rR01T')]
    product_prices = [price.get_text() for price in soup.find_all('div', class_='_30jeq3 _1_WHN1')]
    product_ratings = [rating.get_text() for rating in soup.find_all('div', class_='_3LWZlK')]

    # Zip the data
    products = list(zip(product_names, product_prices, product_ratings))
    
    return products

# Function to save the product data to a CSV file
def save_to_csv(products, filename='flipkart_products.csv'):
    headers = ['Product Name', 'Price', 'Rating']

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(products)
    
    print(f"Data saved to {filename} successfully!")

# Main function
def main():
    url = 'https://dl.flipkart.com/s/LrizY1uuuN'
    
    print("Scraping Flipkart data...")
    products = extract_flipkart_data(url)
    
    if products:
        save_to_csv(products)
    else:
        print("No product data found.")

# Run the program
if __name__ == '__main__':
    main()
