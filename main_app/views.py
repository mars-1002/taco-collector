from django.shortcuts import render


# Add the Taco class & list and view function below the imports
class Taco:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, meat, description, order):
    self.name = name
    self.meat = meat
    self.description = description
    self.order = order

tacos = [
  Taco('Chicken', 'Chicken', 'Kinda Bland.', 3),
  Taco('Carnitas', 'Pork', 'Looks like shredded meat.', 1),
  Taco('Lengua', 'Cow', 'Kind of Chewy', 4),
  Taco('Cecina', 'Pork', 'Thin and spicy', 6)
]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def taco_index(request):
  return render(request, 'tacos/index.html', { 'tacos': tacos })