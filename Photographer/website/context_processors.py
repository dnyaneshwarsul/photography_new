from adminpanel.models import HomeService

def services_processor(request):
    try:
        services_list = HomeService.objects.all().order_by("id")
    except Exception:
        services_list = []
    return {
        'nav_services': services_list
    }
