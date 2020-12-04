from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from django.utils import formats
from django.utils import timezone
from django.contrib.auth import get_user_model

from home.models import VideoItem


class DasboardData(APIView):
    authentication_classes = []
    permission_classes = []
    user = get_user_model()
    date_joined = datetime.now()

    def get(self, request, format=None):
        users = self.user.objects.all()
        user_count = users.count()
        users_data = []
        for usr in users:
            users_data.append({
                'First name': usr.first_name,
                'Last name': usr.last_name,
                'Email': usr.userEmail,
                'Active': usr.is_active,
                'Superuser': usr.is_superuser,
                'Staff': usr.is_staff,
                'Joined date': formats.date_format(timezone.localtime(usr.timeStamp), "SHORT_DATETIME_FORMAT",)
            })

        embed_videos = VideoItem.objects.all()
        embed_videos_data = []
        for video in embed_videos:
            embed_videos_data.append({
                'url': video.url,
                'timeStamp': formats.date_format(timezone.localtime(video.timestamp), "SHORT_DATETIME_FORMAT")
            })
        labels = ['Users', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default = [user_count, 3, 5, 2, 0.2, 6, 3]
        data = {
            'labels': labels,
            'default': default,
            'userdata': users_data,
            'videodata': embed_videos_data
        }
        return Response(data)


def get_data(request, *args, **kwargs):

    data = {
        'sales': 100,
        'customers': 10,
    }
    return JsonResponse(data)
