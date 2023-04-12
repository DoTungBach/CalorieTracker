from django.shortcuts import render
import requests
import json
# vGNqnM7T5CUUeFZtR/hmzQ==XupRqVSXzj0HUJdM
# Create your views here.
def home(request):
    # query = '1lb brisket and fries'
    # api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    # response = requests.get(api_url, headers={'X-Api-Key': 'vGNqnM7T5CUUeFZtR/hmzQ==XupRqVSXzj0HUJdM'})
    # if response.status_code == requests.codes.ok:
    #     print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)

    if request.method == "POST":
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='.format(query)
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'vGNqnM7T5CUUeFZtR/hmzQ==XupRqVSXzj0HUJdM'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)

        return render(request,'hometest.html',{'api':api})
    else:
        return render(request,'hometest.html',{'query':'Enter a valid query'})

    