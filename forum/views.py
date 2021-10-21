from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Topic


def index(request):
    latest_topics_list = Topic.objects.order_by('-pub_date')[:10]
    context = {'latest_topics_list': latest_topics_list}
    return render(request, 'forum/index.html', context)

def comments(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic does not exist")
    return render(request, 'forum/comments.html', {'topic': topic})