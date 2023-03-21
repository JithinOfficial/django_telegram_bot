from .models import Button

def settings(request):
    return {'settings': Button.load()}