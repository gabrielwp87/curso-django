from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video


def indice(resquest):
    videos = Video.objects.order_by('creation').all()
    return render(resquest, 'aperitivos/indice.html', context={'videos': videos})


def video(resquest, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(resquest, 'aperitivos/video.html', context={'video': video})
