from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
import youtube_dl


# Create your views here.
def home_page(request):
    return render(request, 'ytd_app/ytd.html', {'dic': 'youtube downloader'})


def down_video(request):
    if request.method == 'POST':
        vid_url = request.POST['url']
        if vid_url:
            ydl_opts = {'outtmp1':'D:/'}
            with youtube_dl.YoutubeDL(ydl_opts) as down_link:
                down_link.download([vid_url])
            messages.success(request, 'Hi, your Video Downloaded successfull')
            return redirect('YouTube_DownApp:home_page')
            
        else:
            messages.warning(request, 'You should enter your video link')
            return redirect('YouTube_DownApp:home_page')
    return redirect('YouTube_DownApp:home_page')



# def upload_video(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         desc = request.POST['desc']
#         video_file = request.FILES['fileName']
#         thumb_nail = request.FILES['thumbnail_img']
#         cate = request.POST['category']
#         user_obj = User.objects.get(username=request.user)
#         upload_video = VideoPost(user=user_obj, title=title, desc=desc, video_file=video_file, thumbnail=thumb_nail, category=cate)
#         upload_video.save()
#         messages.success(request, 'Video has been uploaded.')

#     return render(request, 'upload_video.html')
