from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json

from .restapis import get_request, analyze_review_sentiments, post_review
from .models import CarMake, CarModel
from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    """
    Handle user login requests. Returns JSON with authentication status.
    """
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)
    response_data = {"userName": username}

    if user is not None:
        login(request, user)
        response_data["status"] = "Authenticated"

    return JsonResponse(response_data)


def logout_user(request):
    """
    Handle user logout requests. Returns JSON indicating logout.
    """
    logout(request)
    return JsonResponse({"userName": ""})


@csrf_exempt
def registration(request):
    """
    Handle user registration requests. Returns JSON with authentication status.
    """
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    try:
        User.objects.get(username=username)
        username_exist = True
    except User.DoesNotExist:
        username_exist = False
        logger.debug(f"{username} is a new user")

    if not username_exist:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    else:
        return JsonResponse({"userName": username, "error": "Already Registered"})


def get_cars(request):
    """
    Returns a JSON response of all car models along with their makes.
    If database is empty, populate sample data.
    """
    if CarMake.objects.count() == 0:
        initiate()

    car_models = CarModel.objects.select_related('car_make')
    cars = [{"CarModel": cm.name, "CarMake": cm.car_make.name} for cm in car_models]

    return JsonResponse({"CarModels": cars})


def get_dealerships(request, state="All"):
    """
    Returns a list of all dealerships or filtered by state if provided.
    """
    endpoint = "/fetchDealers" if state == "All" else f"/fetchDealers/{state}"
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


def get_dealer_reviews(request, dealer_id):
    """
    Returns reviews of a dealer with sentiment analysis.
    """
    if dealer_id:
        endpoint = f"/fetchReviews/dealer/{dealer_id}"
        reviews = get_request(endpoint)
        for review_detail in reviews:
            sentiment_result = analyze_review_sentiments(review_detail['review'])
            review_detail['sentiment'] = (
                sentiment_result.get('sentiment', 'neutral') if sentiment_result else 'neutral'
            )
        return JsonResponse({"status": 200, "reviews": reviews})

    return JsonResponse({"status": 400, "message": "Bad Request"})


def get_dealer_details(request, dealer_id):
    """
    Returns details of a specific dealer using dealer_id.
    """
    if dealer_id:
        endpoint = f"/fetchDealer/{dealer_id}"
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})

    return JsonResponse({"status": 400, "message": "Bad Request"})


@csrf_exempt
def add_review(request):
    """
    Handles posting a dealer review. Only authenticated users can post.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"status": 403, "message": "Unauthorized"})

    try:
        data = json.loads(request.body)
        response = post_review(data)
        if response:
            return JsonResponse({
                "status": 200,
                "message": "Review added successfully",
                "response": response
            })
        else:
            return JsonResponse({"status": 500, "message": "Failed to add review"})

    except Exception as e:
        return JsonResponse({
            "status": 400,
            "message": f"Error in posting review: {e}"
        })
