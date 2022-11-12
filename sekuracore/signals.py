import django.dispatch

access_team_found = django.dispatch.Signal()
access_found = django.dispatch.Signal()
no_more_accesses_found = django.dispatch.Signal()
