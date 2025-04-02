import django

from django.shortcuts import render

from datacenter.models import Visit

def get_duration(visit):
    entered_time = django.utils.timezone.localtime(visit.entered_at)
    if visit.leaved_at:
        time_of_stay = (django.utils.timezone.localtime(visit.leaved_at) - entered_time).seconds
        return time_of_stay
    else:
        now = django.utils.timezone.localtime()
        return (now - entered_time).total_seconds()

def format_duration(duration):
    formated_duration = (f'{int((duration // 3600))}ч {int((duration % 3600 // 60))}м')
    return formated_duration

def storage_information_view(request):
    not_closed_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in not_closed_visits:
        visit_information = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit))
        }
        non_closed_visits.append(visit_information)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
