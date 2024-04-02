fetch('/recipes')
  .then(response => response.json())
  .then(data => {
    const recipesDiv = document.getElementById('recipes');
    data.recipes.forEach(recipe => {
      const recipeDiv = document.createElement('div');
      recipeDiv.innerHTML = `<h2>${recipe.name}</h2><p>Ingredients: ${recipe.ingredients.join(', ')}</p>`;
      recipesDiv.appendChild(recipeDiv);
    });
  })
  .catch(error => {
    console.error('Error fetching recipes:', error);
  });