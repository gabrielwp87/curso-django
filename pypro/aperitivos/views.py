from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'youtube_id': 'watch?v=b899h0lNd7U'}
    return render(request, 'aperitivos/video.html', context={'video':video})
