from .models import School

def school_info(request):
    try:
        school = School.objects.latest('id')
    except School.DoesNotExist:
        school = None
    return {'school': school}