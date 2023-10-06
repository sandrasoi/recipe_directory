from lib.recipe import Recipe
from lib.recipe_repository import RecipeDirectory

# #return list of all books

def test_get_all_recipes(db_connection):
    db_connection.seed('seeds/recipe_directory.sql')
    recipe_repository = RecipeDirectory(db_connection)
    recipes = recipe_repository.all()
    assert recipes == [Recipe(1, 'Pasta', '20', '5'), Recipe(2, 'Chicken', '10', '3'), Recipe(3, 'Beef', '40', '4')]

def test_find_first_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    recipe_repository = RecipeDirectory(db_connection)
    result = recipe_repository.find(1)
    assert result == Recipe(1, 'Pasta', '20', '5')