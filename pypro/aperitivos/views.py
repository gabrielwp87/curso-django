from django.shortcuts import render


def video(resquest, slug):
    videos = {
        'motivacao': {'titulo': 'Aperitivo: Motivação', 'vimeo_id': '799826779?h=be5ee2d29c'},
        'tempo-para-ser-programador': {'titulo': 'Tempo para ser programador', 'vimeo_id': '799826679?h=728cbbb571'}
    }
    video = videos[slug]
    return render(resquest, 'aperitivos/video.html', context={'video': video})
