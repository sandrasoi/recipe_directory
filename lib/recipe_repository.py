from lib.recipe import Recipe

class RecipeDirectory:
    def __init__(self, _connection):
        self._connection = _connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes = []
        for row in rows:
            item = Recipe(row['id'], row['name'], row['cooking_time'], row['rating'])
            recipes.append(item)
        return recipes
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM recipes WHERE id=%s", [id])
        row = rows[0]
        return Recipe(row['id'], row['name'], row['cooking_time'], row['rating'])