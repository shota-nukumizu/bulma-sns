from django.contrib import admin
from .models import *

admin.site.register(ArticleModel)
admin.site.register(TagModel)
admin.site.register(CommentModel)