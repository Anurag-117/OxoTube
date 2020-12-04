from django.http import JsonResponse
from django.shortcuts import render
from home.models import VideoItem
from .forms import VideoAddForm
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required()
def dashboard_view(request):
    form = VideoAddForm()
    if request.method == 'POST':
        video_add_form = VideoAddForm(request.POST)
        if video_add_form.is_valid():
            try:
                VideoItem.objects.get(url=video_add_form.cleaned_data['url'])
                print('Video Already Embedded')
            except VideoItem.DoesNotExist:
                video_add_form.save()
                print('Video Added Successfully')
        else:
            print('invalid form')
    context = {'video_add_form': form}
    return render(request, 'analytics/dashboard.html', context)


