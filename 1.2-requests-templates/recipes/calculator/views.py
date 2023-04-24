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

def calculate_omlet(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for el in DATA.get('omlet').items():
        recipe[el[0]] = el[1] * servings
    context =    {
        'name': 'Омлет',
        'recipe': recipe,
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)

def calculate_pasta(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for el in DATA.get('pasta').items():
        recipe[el[0]] = el[1] * servings
    context =    {
        'name': 'Паста',
        'recipe': recipe,
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)


def calculate_buter(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for el in DATA.get('buter').items():
        recipe[el[0]] = el[1] * servings
    context =    {
        'name': 'Бутерброд',
        'recipe': recipe,
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)

def calculate_strawberry_yoghurt(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for el in DATA.get('strawberry yoghurt').items():
        recipe[el[0]] = el[1] * servings
    context =    {
        'name': 'Клубничный йогурт',
        'recipe': recipe,
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)

