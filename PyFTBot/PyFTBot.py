import requests
        
def postbot(token,method,arg):
    url = "https://script.google.com/macros/s/AKfycbzxgX8puIgB5uXelJ2wNzxa8VbheV463rBm6_SpEau-D2v4g0q1/exec?bot_token=" + token + "&method=" + method + "&args=" + arg

    payload = {}
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    return response.text.encode('utf8')

def getbot(token,method):
    url = "https://script.google.com/macros/s/AKfycbzxgX8puIgB5uXelJ2wNzxa8VbheV463rBm6_SpEau-D2v4g0q1/exec?bot_token=" + token +"&method=" + method

    payload = {}
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    return response.text.encode('utf8')
    
