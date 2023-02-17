from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 799826779},
        'instalacao-windows': {'titulo': 'Video Instalação Windows', 'vimeo_id': 799826679},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
