import datetime

from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        "id": 1,
        "title": "HTML in a nutshell",
        "content": "Unfeeling so rapturous discovery he exquisite. Reasonably so middle-tons or impression by "
                   "terminated. "
                   "Old pleasure required removing elegance him had. Down she bore sing saw calm high."
                   " Of an or game gate west face shed. no great but music too old found arose.",
        "date": datetime.datetime.now(),
        "author": "Eden Lovely"

    },
    {
        "id": 2,

        "title": "JavaScript",
        "content": "Marianne or husbands if at stronger ye. Considered is as middletons uncommonly. "
                   "Promotion perfectly ye consisted so. His chatty dining for effect ladies active. "
                   "Equally journey wishing not several behaved chapter she two sir. Deficient procuring favourite "
                   "extensive you two. "
                   "Yet diminution she impossible understood age",
        "date": datetime.datetime.now(),
        "author": "Tman Nonsense"

    },
    {
        "id": 3,
        "title": "Truth",
        "content": "Civility vicinity graceful is it at. Improve up at to on mention perhaps raising. "
                   "Way building not get formerly her peculiar. Up uncommonly prosperous sentiments simplicity "
                   "acceptance to so. "
                   "Reasonable appearance companions oh by remarkably me invitation understood. Pursuit elderly ask "
                   "perhaps all.",
        "date": datetime.datetime.now(),
        "author": "Dee Excellent"
    }
]


def index(request):
    return render(request, "posts/index.html", context={"posts": posts})


def post_detail(request, post_id):
    post = posts[post_id - 1]
    return render(request, "posts/post-detail.html", context={"post": post})
