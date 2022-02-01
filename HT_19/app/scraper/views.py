import requests

from django.shortcuts import render
from django.http import HttpResponse

from scraper.models import Ask, Job, Show, New


def index(request):
	category_name = request.POST.get('category')
	print(category_name)
	stories = get_stories(category_name)
	print(stories)
	stories_list = get_stories_list(stories)
	values_to_db = write_db(category_name, stories_list)
	print("All is done! Thank you!")
	return render(request, 'scraper/index.html')

def get_stories(category_name):
	url = f"https://hacker-news.firebaseio.com/v0/{category_name}.json?print=pretty"
	r = requests.get(url)
	response_value = r.json()
	return response_value

def get_stories_list(category_list):
	stories_list = []
	for story in category_list:
		story_url = f"https://hacker-news.firebaseio.com/v0/item/{story}.json?print=pretty"
		story_response = requests.get(story_url)
		story_data = story_response.json()
		stories_list.append(story_data)
	return stories_list


def write_db(category_name,stories_list):
	if category_name == "askstories":
		for story in stories_list:
			print(story.get('id'))
			obj = Ask.objects.get_or_create(
				story_id = story.get('id'),
				story_type = story.get('type'),
				by = story.get('by'),
				timestamp = story.get('time'),
				title = story.get('title'),
				text = story.get('text'),
				url = story.get('url'),
				)

	elif category_name =="showstories":
		for story in stories_list:
			print(story.get('id'))
			obj = Show.objects.get_or_create(
				story_id = story.get('id'),
				story_type = story.get('type'),
				by = story.get('by'),
				timestamp = story.get('time'),
				title = story.get('title'),
				text = story.get('text'),
				url = story.get('url'),
				)

	elif category_name =="jobstories":
		for story in stories_list:
			print(story.get('id'))
			obj = Job.objects.get_or_create(
				story_id = story.get('id'),
				story_type = story.get('type'),
				by = story.get('by'),
				timestamp = story.get('time'),
				title = story.get('title'),
				text = story.get('text'),
				url = story.get('url'),
				)

	elif category_name == "newstories":
		for story in stories_list:
			print(story.get('id'))
			obj = New.objects.get_or_create(
				story_id = story.get('id'),
				story_type = story.get('type'),
				by = story.get('by'),
				timestamp = story.get('time'),
				title = story.get('title',),
				text = story.get('text'),
				url = story.get('url'),
				)
