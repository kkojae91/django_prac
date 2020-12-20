from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from .models import Post
# Create your views here.

# ListView -> object_list
class PostLV(ListView):
  model = Post
  template_name = 'blog/post_all.html'
  context_object_name = 'posts'
  paginate_by = 2

# DetailView -> object
class PostDV(DetailView):
  model = Post

# ArchiveIndexView -> object_list, latest
class PostAV(ArchiveIndexView):
  model = Post
  date_field = 'modify_dt'

# object_list
class PostYAV(YearArchiveView):
  model = Post
  date_field = 'modify_dt'
  make_object_list = True

# object_list
class PostMAV(MonthArchiveView):
  model = Post
  date_field = 'modify_dt'

# object_list
class PostDAV(DayArchiveView):
  model = Post
  date_field = 'modify_dt'

# object_list
class PostTAV(TodayArchiveView):
  model = Post
  date_field = 'modify_dt'
  