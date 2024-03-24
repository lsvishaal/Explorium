from django.http import JsonResponse

def get_random_activity(request):
    # Implement your logic to get a random activity
    data = {
        "activity": "Do something interesting",
    }
    return JsonResponse(data)

def filter_activities(request):
    # Implement your logic to filter activities
    data = {
        "activities": ["Activity 1", "Activity 2"],
    }
    return JsonResponse(data)

def get_activity_by_key(request, key):
    # Implement your logic to get an activity by key
    data = {
        "activity": "Activity with key: " + key,
    }
    return JsonResponse(data)
