from django.views import generic
from category.models import Category

class HomePage(generic.TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category_list'] = Category.objects.all()
    #     return context


# class CatView(generic.ListView):
#     model = Category
#     template_name = 'base.html'
#     context_object_name = 'category_list'

#     def get_queryset(self):
#         return Category.objects.all()