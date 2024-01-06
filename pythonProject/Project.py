import requests
from bs4 import BeautifulSoup

products_to_track=[
    {
        "product_url": "https://www.flipkart.com/samsung-galaxy-s21-fe-5g-graphite-128-gb/p/itm7be0f72fff180?pid=MOBGBPFZSPRG8GSU&lid=LSTMOBGBPFZSPRG8GSUHAU48C&marketplace=FLIPKART&q=samsung+5g+mobile&store=tyy%2F4io&srno=s_1_9&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=organic&iid=5f05eba9-b1d2-4d2d-a494-24b24a5f5564.MOBGBPFZSPRG8GSU.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=zhioyq1w8g0000001704518514228&qH=2c67e5ea833d3cc7",
        "name": "SAMSUNG Galaxy S21 FE 5G",
        "target_price":20000
    },
    {
        "product_url":"https://www.flipkart.com/samsung-galaxy-m14-5g-icy-silver-128-gb/p/itme53601886b5d9?pid=MOBGZWRQNHGDF7SA&lid=LSTMOBGZWRQNHGDF7SAFQZ8PW&marketplace=FLIPKART&q=samsung+5g+mobile&store=tyy%2F4io&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=organic&iid=5f05eba9-b1d2-4d2d-a494-24b24a5f5564.MOBGZWRQNHGDF7SA.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=zhioyq1w8g0000001704518514228&qH=2c67e5ea833d3cc7",
        "name": "SAMSUNG Galaxy M14 5G",
        "target_price":14000
    },
    {
        "product_url": "https://www.flipkart.com/samsung-galaxy-a15-5g-light-blue-128-gb/p/itm7ebaa454bf5cb?pid=MOBGWD85TPKVHRUA&lid=LSTMOBGWD85TPKVHRUAJQPLRQ&marketplace=FLIPKART&q=samsung+5g+mobile&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=organic&iid=5f05eba9-b1d2-4d2d-a494-24b24a5f5564.MOBGWD85TPKVHRUA.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=zhioyq1w8g0000001704518514228&qH=2c67e5ea833d3cc7",
        "name": "SAMSUNG Galaxy A15 5G",
        "target_price":19500
    },
    {
        "product_url": "https://www.flipkart.com/mi-x-series-108-cm-43-inch-ultra-hd-4k-led-smart-android-tv-2022-4k-dolby-vision-hdr10-hlg-audio-dts-virtual-dts-hd-vivid-picture-engine/p/itmd3e561fa04588?pid=TVSGHEQVGZVTSEBT&lid=LSTTVSGHEQVGZVTSEBTYWBRXG&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_0698c40d-b5a7-4eb5-b1a3-be6e610efa8b_13_QCN7Q2H8RICT_MC.TVSGHEQVGZVTSEBT&ppt=clp&ppn=mobile-phones-store&otracker=clp_pmu_v2_Top%2B4K%2BTV%2BDeals_2_13.productCard.PMU_V2_Mi%2BX%2BSeries%2B108%2Bcm%2B%252843%2Binch%2529%2BUltra%2BHD%2B%25284K%2529%2BLED%2BSmart%2BAndroid%2BTV%2B2022%2BEdition%2Bwith%2B4K%2BDolby%2BVision%2B%257C%2BHDR10%2B%257C%2BHLG%2B%257C%2BDolby%2BAudio%2B%257C%2BDTS%253A%2BVirtual%2BX%2B%257C%2BDTS-HD%2B%257C%2BVivid%2BPicture%2BEngine_television-store_TVSGHEQVGZVTSEBT_neo%2Fmerchandising_1&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Top%2B4K%2BTV%2BDeals_LIST_productCard_cc_2_NA_view-all&cid=TVSGHEQVGZVTSEBT",
        "name": "Mi X Series 108 cm (43 inch) Ultra HD (4K) LED Smart Android TV 2022",
        "target_price":26000
    },
    {
        "product_url": "https://www.flipkart.com/powermax-fitness-x-marvel-mt-1a-4hp-peak-smart-folding-multifunction-home-gym-cardio-training-treadmill/p/itmcf4a8e0426903?pid=TRDG6ZFJZEB2QHQC&lid=LSTTRDG6ZFJZEB2QHQCQQSEQU&marketplace=FLIPKART&store=qoc%2Famf%2Foyq&srno=b_1_5&otracker=clp_omu_Cardio%2BFitness_1_2.dealCard.OMU_exercise-fitness-essentials-store_exercise-fitness-essentials-store_Z1J4SJL8ZYZB_2&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Cardio%2BFitness_NA_dealCard_cc_1_NA_view-all_2&fm=neo%2Fmerchandising&iid=5ea2739a-fc60-4c9e-bd8d-6d9875746d32.TRDG6ZFJZEB2QHQC.SEARCH&ppt=browse&ppn=browse&ssid=h67dqbeks00000001704530256367",
        "name": "Powermax Fitness X Marvel MT-1A (4HP Peak) Smart Folding, Multifunction, Home-Gym Cardio Training Treadmill",
        "target_price":30000
    }
]

def gives_product_price(URL):
    headers ={
        "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    # print(page)
    product_price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
    return product_price

result_file = open('my_python_project_result.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = gives_product_price(every_product.get("product_url"))
        current_price_str = product_price_returned.string.strip('₹').replace(',', '')  # Remove ₹ and commas
        my_product_price = int(current_price_str)  # Convert price to integer
        print(f"{every_product.get('name')} - {my_product_price}")

        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get("name") + '-\t' + 'available at Target Price\t' + 'current price - ' + str(my_product_price)+'\n')
        else:
            print("still the same price value")

finally:
    result_file.close()


