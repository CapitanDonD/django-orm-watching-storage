from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.models import is_visit_long
from datacenter.storage_information_view import get_duration

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        visit_duration = get_duration(visit)
        passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': is_visit_long(visit_duration)
        }
        this_passcard_visits.append(passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)