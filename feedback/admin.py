from django.contrib import admin
from feedback.models import Like, Rating, Favorite
from feedback.models import Comment
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(Comment)


