import json
import requests

bc_chain_url = "http://127.0.0.1:8000/"

def save_to_chain(data_dict):
    """
    Send data to add in chain 
    """
    
    payload={'data':json.dumps(data_dict)}
    mine_url = bc_chain_url+"mine_block"

    response = requests.request("POST", mine_url, data=payload)

    if response.status_code == 200:
        print("Block Successfully added to chain")
        #print("block details",response.json())



if __name__ == "__main__":
    save_to_chain( {"id":"1234","text":"2233ert","reg":"UP","lat":-37.840935,"log":144.946457})
    save_to_chain( {"id":"123","text":"2233ert","reg":"UP","lat":-35.850935,"log":144.946457})
    save_to_chain( {"id":"124","text":"2233ert","reg":"UP","lat":-39.870955,"log":144.946457})
    save_to_chain( {"id":"34","text":"2233ert","reg":"UP","lat":-38.780975,"log":144.946457})
    
    






