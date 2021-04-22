from django.views.generic import TemplateView
from category.models import Category

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_cat = Category
        query = Category.objects.all()
        print(query)
        context['category_list'] = query
        return context
