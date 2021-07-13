from django.contrib import admin
from moviegeeks.models import Movie
from collector.models import Log
from analytics.models import Rating, Cluster
from recommender.models import MovieDescriptions, Similarity, Recs
# Register your models here.

admin.site.register(Movie)
admin.site.register(Log)
admin.site.register(Rating)
admin.site.register(Cluster)
admin.site.register(MovieDescriptions)
admin.site.register(Similarity)
admin.site.register(Recs)