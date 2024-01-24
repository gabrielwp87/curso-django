from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='799826779?h=be5ee2d29c'),
    Video(slug='tempo-para-ser-programador', titulo='Tempo para ser programador', vimeo_id='799826679?h=728cbbb571'),
]

videos_dct = {v.slug: v for v in videos}


def indice(resquest):
    return render(resquest, 'aperitivos/indice.html', context={'videos': videos})


def video(resquest, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(resquest, 'aperitivos/video.html', context={'video': video})
