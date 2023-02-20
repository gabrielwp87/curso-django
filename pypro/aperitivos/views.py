from django.urls import reverse

from django.shortcuts import render


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))

videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', 799826779),
    Video('instalacao-windows', 'Video Instalação Windows', 799826679),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos':videos})


def video(request, slug):

    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
