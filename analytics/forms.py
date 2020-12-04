from django import forms
from django.forms import ModelForm
from home.models import VideoItem
from embed_video.fields import EmbedVideoFormField


class VideoAddForm(ModelForm):
    url = EmbedVideoFormField()

    class Meta:
        model = VideoItem
        fields = ('url',)
