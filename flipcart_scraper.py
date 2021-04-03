from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data_and_load_to_dataframes(anchors):
    mobile_data = []
    for anchor in anchors:
        r = requests.get('https://www.flipkart.com' + str(anchor['href']))
        soup = BeautifulSoup(r.content,'lxml')
        phone_name = soup.find('span',attrs={'class','B_NuCI'}).get_text(" ",strip=True).replace("\xa0"," ")
        price = soup.find('div', class_=['_30jeq3', '_16Jk6d']).get_text(" ",strip=True).replace("\xa0"," ")
        rating_star = soup.find('div', attrs={'class', '_3LWZlK'}).get_text(" ",strip=True).replace("\xa0"," ")
        rating_and_reviews = soup.find('span', attrs={'class', '_2_R_DZ'}).get_text(" ",strip=True).replace("\xa0"," ")

        mbl_data = {
            'phone_name' : phone_name,
            'price' : price,
            'rating_star' : rating_star,
            'rating_and_reviews' : rating_and_reviews
        }
        mobile_data.append(mbl_data)
        print(mbl_data['phone_name'])
        df = pd.DataFrame(mobile_data)
        df.to_csv("MyInfo.csv", index=False)

def get_url(base_url):
    for i in range(1,10):
        r = requests.get(f'{base_url}/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page={i}')
        soup = BeautifulSoup(r.content,'lxml')
        anchors = soup.find_all('a', {'class': '_1fQZEK', 'href': True})
        get_data_and_load_to_dataframes(anchors)
        print('Loop ' + str(i))

def main():
    base_url = 'https://www.flipkart.com/'
    get_url(base_url)

if __name__ == '__main__':
    main()
