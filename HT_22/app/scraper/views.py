from django.shortcuts import render
from .tasks import test, get_stories


def stories_scraper(request):
	category_name = request.POST.get('category')
	print(category_name)
	stories = get_stories(category_name)
	if len(stories) == 0:
		print("There is nothing to add to DB")
	else:
		print(len(stories))
		stories_to_db = test.delay(category_name, stories)
		print(stories_to_db.id)

	return render(request, 'scraper/index.html')