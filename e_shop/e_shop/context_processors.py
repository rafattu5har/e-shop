from category.models import Category

def cat_list(request):

    categories = Category.objects.all()
    return {
        'category_list': categories
    }