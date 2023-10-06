from lib.recipe import Recipe

def test_a_recipe_construct():
    recipe = Recipe(1, 'Pasta', 20, 5)
    assert recipe.id == 1
    assert recipe.name == 'Pasta'
    assert recipe.cooking_time == 20
    assert recipe.rating == 5
    
def test_compare_identical_recipes():
    recipe1 = Recipe(1, 'Pasta', 20, 5)
    recipe2 = Recipe(1, 'Pasta', 20, 5)
    assert recipe1 == recipe2

# def test_format_recipes():
#     recipe = Recipe(1, 'Pasta', 20, 5)
#     assert str(recipe) == "1 - Pasta - 20 - 5"
