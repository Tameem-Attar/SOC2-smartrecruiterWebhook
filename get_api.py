import requests
import json

 
def get_details(id,event_name):
    url = "https://api.smartrecruiters.com/jobs/{}".format(id)
    
    headers = {
        "accept": "application/json",
        "Accept-Language": "en",
        "x-smarttoken": "DCRA1-4a8c92b78aa5450b825e58d2bdcffe60"
    }
        
    response = requests.get(url, headers=headers)
    print(response.text)
    data = json.loads(response.text)
    
    # objective only return whats needed. 
    if event_name == "job.status.updated":
        status = data["status"]
        print("status is ::", status)
    elif event_name == "job.status.updated":
        pass
    
    return(status) 