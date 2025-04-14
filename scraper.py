import requests
from bs4 import BeautifulSoup

def get_gpu_prices():
    url = "https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-1?Tid=7709&Order=BESTSELLING"
    
    try:
        response = requests.get(url) # get all the html from the url
                
        soup = BeautifulSoup(response.text, 'html.parser') # parse the html
                
        gpus = soup.find_all('div', class_='item-cell') # find all the divs with the class item-cell
        
        for gpu in gpus[:5]: # loop through the first 5 gpus
            name_element = gpu.find('a', class_='item-title') # find the a tag with the class item-title
            name = name_element.text.strip() if name_element else "Unknown GPU" # get the text of the a tag, this is our gpu name
            
            price_element = gpu.find('li', class_='price-current') # find the li tag with the class price-current
            price = price_element.text.strip() if price_element else "Price not available" # get the text of the li tag, this is our gpu price
            
            # print that stuff out
            print(f"\n{name}")
            print(f"Price: {price}")
            print("-" * 60)
            
    # always good to add error handling
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_gpu_prices()
