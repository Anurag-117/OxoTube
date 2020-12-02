from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'home/404.html', status = 404)


def handler500(request, *args, **argv):
    return render(request, 'home/500.html', status=500)


def home_view(request):
    return render(request, 'home/videoCatalog.html')

