#Author : Sriram Muralidharan
from functools import lru_cache
import requests
import base64
import sys
import time
from concurrent.futures import ThreadPoolExecutor

@lru_cache(maxsize=100)
def api_call(id):
    auth = base64.b64encode(id.encode('ascii')).decode('ascii') # convert the id into base64 as the authentication
    headers = {'Authorization': auth}
    response = requests.get("https://challenges.qluv.io/items/" + id, headers=headers)
    response.close()
    if response.status_code == 200:
        return(response.content)
    else:
        return(response.status_code)

if __name__ == "__main__":

    s = time.time()
    processes=[]
    with open(sys.argv[1], 'r') as inputfile:
        with ThreadPoolExecutor(max_workers=5) as executor:
            for line in inputfile:
                line = line.replace("\n", "")
                processes.append(executor.submit(api_call, line))  
    result = []
    for i in processes:
        result.append(i.result())   
    print(result)        
    print(f"Time taken is {time.time() - s}")
