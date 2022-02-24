import requests
from .models import Ask, Job, Show, New
from celery import shared_task


@shared_task(queue='scraper', name='test_run')
def test_run(category_name, stories):
    print("Hello")
    stories_list = get_stories_list(stories)
    to_db = write_db(category_name, stories_list)


def get_stories_list(category_list):
    stories_list = []
    for story in category_list:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story}.json?print=pretty"
        story_response = requests.get(story_url)
        story_data = story_response.json()
        stories_list.append(story_data)
        print("hello")
    return stories_list


def write_db(category_name,stories_list):
    if category_name == "askstories":
        for story in stories_list:
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
            obj = New.objects.get_or_create(
                story_id = story.get('id'),
                story_type = story.get('type'),
                by = story.get('by'),
                timestamp = story.get('time'),
                title = story.get('title',),
                text = story.get('text'),
                url = story.get('url'),
                )
