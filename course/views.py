from django.views.generic import ListView
from .models import CoursePost, Column
class CourseIndex(ListView):
    template_name = 'course/index.html'
    queryset = Column.objects.all()
    context_object_name = 'columns'

