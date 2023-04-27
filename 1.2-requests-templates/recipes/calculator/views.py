from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'strawberry yoghurt':{
        'молоко, л': 1,
        'закваска, шт': 1,
        'клубничное пюре, г': 50,
    }
}

def dish_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    name = ''
    if dish in DATA:
        ingredients = {k: (v * servings) for k, v in DATA[dish].items()}
        name = dish
    context = {'recipe': ingredients,
               'name': name}
    return render(request, 'calculator/index.html', context)
