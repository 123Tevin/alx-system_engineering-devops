import requests

def number_of_subscribers(subreddit):
    #Define the Reddit API URL for the given subreddit
url = f'https://www.reddit.com/r/{subreddit}/about.json'

    #Define a custom User-Agent to avoid being rate-limited or blocked
headers = {'User-Agent': 'python:subscribers_query:v1.0 (by /u/yourusername)'}

try :
    #Send a Get request to the Reddit API 
    response = requests.get(url, headers=headers)

    #Check if the request was successful (status code 200)
    if  response.status_code == 200:
        #Parse the JSON response 
        data = response.json()
        #Extract the number of subscribers
        subscribers = data.get('data',{}).get('subscribers',0)
        return suscribers
    else:
        #Return 0 if the subreddit is invalid or other errors occur
        return 0
    except requests.RequestException:
        #Return 0 if there's an issue with the request
        return 0

    #Example usage:
    print(number_of_subscribers('python')) #Should print the number of subscribers for /r/python
    print(number_of_subscribers('notrealsubreddit')) #Should print 0
