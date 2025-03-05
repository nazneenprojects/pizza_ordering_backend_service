# pizza_api/views.py
import json
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Load pizza menu from JSON file
with open('/home/zermatt/Documents/pizza_order_backend_service/pizza_project/data.json', 'r') as f:
    PIZZA_MENU = json.load(f)['pizza_menu']


def get_menu(request):
    """
    Fetch menu items.
    Supports querying by pizza name.
    """
    pizza_name = request.GET.get('name')

    if pizza_name:
        # Find pizza by name (case-insensitive)
        pizza = next((p for p in PIZZA_MENU if p['name'].lower() == pizza_name.lower()), None)

        if pizza:
            return JsonResponse(pizza)
        else:
            return JsonResponse({'error': 'Pizza not found'}, status=404)

    # If no name provided, return full menu
    return JsonResponse(PIZZA_MENU, safe=False)


@csrf_exempt
def place_order(request):
    """
    Place an order for pizzas.
    Expects a JSON body with pizza IDs and quantities.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)

    try:
        # Parse the request body
        order_items = json.loads(request.body)

        # Calculate total price
        total_price = 0
        for item in order_items:
            pizza = next((p for p in PIZZA_MENU if p['id'] == item['id']), None)

            if not pizza:
                return JsonResponse({'error': f'Pizza with ID {item["id"]} not found'}, status=400)

            total_price += pizza['price'] * item['quantity']

        # Generate a random order ID
        order_id = random.randint(10000, 99999)

        return JsonResponse({
            'order_id': order_id,
            'price': round(total_price, 2)
        })

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except KeyError:
        return JsonResponse({'error': 'Missing pizza ID or quantity'}, status=400)
