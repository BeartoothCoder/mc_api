import json
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Recipe


HEADERS = {
    'Content-Type': 'application/json',
}


def _serialize(recipe:Recipe):
    return {
        "id": recipe.id,
        "data": recipe.data,
        "img_link": recipe.img_link,
    }
def _serialize_all(recipes:list[Recipe]):
    return [_serialize(r) for r in recipes]


@require_http_methods(['GET'])
def recipe_list(request:HttpRequest):
    # If query param was provided
    if (query := request.GET.get('q')) != None:
        query = query.lower().replace(' ', '_')
        recipes = Recipe.objects.raw("""
            SELECT * FROM recipes_recipe
            WHERE data -> '$."minecraft:recipe_shaped".result.item' LIKE %s
               OR data -> '$."minecraft:recipe_shapeless".result.item' LIKE %s
               OR data -> '$."minecraft:recipe_furnace".output' LIKE %s
               OR data -> '$."minecraft:recipe_brewing_container".output' LIKE %s
               OR data -> '$."minecraft:recipe_brewing_mix".output' LIKE %s
               OR data -> '$."minecraft:recipe_smithing_transform".result' LIKE %s
        """, [f'%{query}%']*6) # Ignore armor trims. There's 1 weird recipe that makes no sense.
        # Return a 404 if there were no matches
        if len(recipes) < 1:
            return HttpResponseNotFound()
    # No query param; get index of all items
    else:
        recipes = Recipe.objects.all()
    return HttpResponse(json.dumps(_serialize_all(recipes)), headers=HEADERS)



@require_http_methods(['GET', 'PATCH'])
@csrf_exempt
def recipe_detail(request:HttpRequest, id:int):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'PATCH':
        # Update the resource before returning it
        patch:dict = json.loads(request.body)
        img_link = patch.get('img_link')
        if img_link is not None:
            recipe.img_link = img_link
            recipe.save()
    response = HttpResponse(json.dumps(_serialize(recipe)), headers=HEADERS)
    return response