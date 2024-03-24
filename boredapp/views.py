from django.shortcuts import render
import requests
from .models import ActivitySuggestion
from django.http import HttpResponse

def empty_favicon(request):
    return HttpResponse(status=204)

def index(request):
    return render(request, 'boredapp/index.html')

def suggest_activity(request):
    activity = None
    activity_type = "recreational"
    participants = "1"  # Default values
    error_message = ""

    if request.method == 'POST':
        activity_type = request.POST.get('activity_type')
        participants = request.POST.get('participants')

        # Check if participants is greater than 1
        if participants and int(participants) > 1:
            error_message = "No activities that match your criteria (more than 1 participant not supported)."
        else:
            base_url = "https://www.boredapi.com/api/activity"
            params = {"type": activity_type, "participants": participants}
            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                activity_data = response.json()

                if 'activity' in activity_data:
                    activity = activity_data['activity']
                    suggestion = ActivitySuggestion(
                        activity=activity,
                        participants=participants,
                        activity_type=activity_type
                    )
                    suggestion.save()

    return render(request, 'boredapp/index.html', {'activity': activity, 'activity_type': activity_type, 'participants': participants, 'error_message': error_message})
