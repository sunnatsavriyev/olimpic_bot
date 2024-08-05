# import requests
# from pprint import pprint as print
# # Where USD is the base currency you want to use


# url = 'https://apis.codante.io/olympic-games/countries'

#     # Making our request
# response = requests.get(url)
# data = response.json()
    
# for i in range(5):
#     rank = data['data'][i]['rank']
#     name = data['data'][i]['name']
#     gold_medal=data['data'][i]['gold_medals']
#     silver=data['data'][i]['silver_medals']
#     bronza = data['data'][i]['bronze_medals']
#     total = data['data'][i]['total_medals']


#     print(f"{rank} - Davlat: {name} - oltinmedal: {gold_medal}ta - kumush: {silver}ta - bronza: {bronza}ta - umumiy: {total}ta ")

import requests

def fetch_data1(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # Initialize an empty list to store the formatted strings
        results = []

        # Header row
        header = "Rank | Davlat      | Gold🥇 | Silver🥈 | Bronze🥉 | Total"
        separator = "-" * len(header)
        results.append(f"```\n{header}\n{separator}")

        # Process the top 5 items
        for i in range(min(30, len(data['data']))):
            rank = data['data'][i]['rank']
            name = data['data'][i]['id']
            gold_medal = data['data'][i]['gold_medals']
            silver = data['data'][i]['silver_medals']
            bronza = data['data'][i]['bronze_medals']
            total = data['data'][i]['total_medals']

            # Format each row
            result_string = (f"{rank:<5}    |    {name:<5}   |    {gold_medal:<5}    |    "
                             f"{silver:<5}       |      {bronza:<5}           |      {total:<5}")
            results.append(result_string)

        results.append("```")

        return '\n'.join(results)

    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None
