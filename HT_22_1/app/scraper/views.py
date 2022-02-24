import requests

from django.shortcuts import render

from .tasks import test_run
from .models import Ask, Job, Show, New


def get_stories(category_name):
    url = f"https://hacker-news.firebaseio.com/v0/{category_name}.json?print=pretty"
    r = requests.get(url)
    response_value = r.json()
    verified_response = []
    if category_name == "askstories":
        for s_id in response_value:
            try:
                story_in_db_check = Ask.objects.get(story_id = s_id)
            except:
                verified_response.append(s_id)
    elif category_name =="showstories":
        for s_id in response_value:
            try:
                story_in_db_check = Show.objects.get(story_id = s_id)
            except:
                verified_response.append(s_id)
    elif category_name =="jobstories":
        for s_id in response_value:
            try:
                story_in_db_check = Job.objects.get(story_id = s_id)
            except:
                verified_response.append(s_id)
    elif category_name == "newstories":
        for s_id in response_value:
            try:
                story_in_db_check = New.objects.get(story_id = s_id)
            except:
                verified_response.append(s_id)

    return verified_response


def index(request):
    category_name = request.POST.get('category')
    print(category_name)
    stories = get_stories(category_name)
    if len(stories)==0:
        print("There is nothing to add to DB")
        return render(request, 'scraper/index.html')
    else:
        print(stories)
        values_to_db = test_run.delay(category_name, stories)
        print("All is done! Thank you!")
        return render(request, 'scraper/index.html')








