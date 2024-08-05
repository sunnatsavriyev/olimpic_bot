# import requests
# from pprint import pprint as print
# # Where USD is the base currency you want to use


# url = 'https://apis.codante.io/olympic-games/disciplines'

#     # Making our request
# response = requests.get(url)
# data = response.json()
    
# for i in range(45):
#     idsi= data['data'][i]['id']
#     nomi= data['data'][i]['name']

#     print(f' {i+1} - Ids: {idsi} , sport turi🎗: {nomi}')





import requests

def fetch_data3(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        items_to_process = min(45, len(data['data']))
        
        # Collect the information in a list
        result_lines = []
        for i in range(items_to_process):
            idsi = data['data'][i]['id']
            nomi = data['data'][i]['name']
            result_lines.append(f'{i + 1} - Ids:    {idsi},     Sport turi🎗:    {nomi}')
        
        # Join the results into a single string
        result_message = '\n'.join(result_lines)
        return result_message
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None