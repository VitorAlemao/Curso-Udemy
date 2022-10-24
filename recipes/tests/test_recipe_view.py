
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from recipes.models import Category, Recipe


class RecipeViewTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:home')
        )
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 2})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create(
            first_name='Vitor',
            last_name='Hugo',
            username='Vitoralemão',
            password='Vitoralemao1',
            email='vitorhugoalenão@gmail.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Description Recipe',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porçoes',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        )
        assert 1 == 1

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_recipe_home_shows_no_recipe_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
        )

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
