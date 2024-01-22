from django.shortcuts import render


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', '799826779?h=be5ee2d29c'),
    Video('tempo-para-ser-programador', 'Tempo para ser programador', '799826679?h=728cbbb571'),
]

videos_dct = {v.slug: v for v in videos}


def indice(resquest):
    return render(resquest, 'aperitivos/indice.html', context={'videos': videos})


def video(resquest, slug):
    video = videos_dct[slug]
    return render(resquest, 'aperitivos/video.html', context={'video': video})
