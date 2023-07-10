
import requests
import json
import sys

def get_UMLS(search_term, UMLS_API_KEY):

    
    url = f"https://uts-ws.nlm.nih.gov/rest/search/current?string={search_term}&pageNumber=1&searchType=exact&apiKey={UMLS_API_KEY}"
    response = requests.get(url, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"})
    
    data = json.loads(response.text)

    result = data['result']

    uis = []    
    if "results" in result:
        for i in result["results"]:
            ui = i['ui']
            uis.append(ui)

    return uis


if __name__ == "__main__":
    #print (get_UMLS('Breast Cancer'))
    print (get_UMLS(sys.argv[1], UMLS_API_KEY=sys.argv[2]))