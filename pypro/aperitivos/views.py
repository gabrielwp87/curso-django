from django.shortcuts import render

def video(resquest, slug):
    video={'titulo':'Aperitivo: Motivação', 'vimeo_id':'799826779?h=be5ee2d29c'}
    return render(resquest, 'aperitivos/video.html', context={'video':video})
