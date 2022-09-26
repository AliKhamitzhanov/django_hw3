from django.shortcuts import render
from models.models import Model, Series
from brands.models import Brand
# Create your views here.


def brand_cars(request, id):
    brand = Brand.objects.get(id=id)
    models = Model.objects.filter(brand=brand)

    data = {
        'brand': brand,
        'models': models,
    }

    return render(request, 'brand_cars.html', context=data)


def series_models(request, brand_id, model_id):
    brand = Brand.objects.get(id=brand_id)
    model = Model.objects.get(id=model_id)
    series = Series.objects.filter(model=model)

    data = {
        'brand': brand,
        'model': model,
        'seriess': series,
    }

    return render(request, 'models_series.html', context=data)
