from django.views.generic import ListView
from .models import Post

class HomepageWiev(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new
