# import pytube
# from pytube import Playlist
# DOWNLOAD_FOLDER = "C:\\Users\\HJ.Kim\\Videos"
# p = Playlist('https://www.youtube.com/watch?v=5NBAtp-kTWY&list=PLrpXwtuxGqcLXzZ5pchcprhqx_dignFiS')
# for video in p.videos:
#     video.download_ALL(DOWNLOAD_FOLDER)

# from pytube import Playlist
# pl = Playlist("https://www.youtube.com/watch?v=5NBAtp-kTWY&list=PLrpXwtuxGqcLXzZ5pchcprhqx_dignFiS")

# # pl.download_all() #파이썬 파일과 같은 위치
# pl.download_all("C:\\Users\\HJ.Kim\\Videos") #저장위치

# from pytube import Playlist, YouTube 
# from moviepy.editor import * 
# fpath = lambda x: './src/' + x 
# def ydown(url: str, prefix: str = "https://www.youtube.com/watch?v=5NBAtp-kTWY&list=PLrpXwtuxGqcLXzZ5pchcprhqx_dignFiS"): 
#     yt = YouTube(url) 
#     vpath = ( 
#              yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True) 
#              .order_by("resolution") 
#              .desc() .first() 
#              .download(output_path=fpath("C:\\Users\\HJ.Kim\\Videos"), filename_prefix=f"{prefix} ") 
#              ) 
#     apath = ( 
#              yt.streams.filter(adaptive=True, file_extension="mp4", only_audio=True) 
#              .order_by("abr") 
#              .desc() 
#              .first() 
#              .download(output_path=fpath("C:\\Users\\HJ.Kim\\audio"), filename_prefix=f"{prefix} ") 
#              ) 
#     v = VideoFileClip(vpath) 
#     a = AudioFileClip(apath) 
#     v.audio = a 
#     v.write_videofile(fpath(f"1080/{vpath.split('/')[-1]}")) 
    
#     def playlistdown(url: str, prefix: str = ""): 
#         pl = Playlist(url) 
#         for v in pl.video_urls: 
#             try: 
#                 ydown(v, prefix) 
#             except: 
#                 continue

# import http
# from requests_html import HTMLSession
# import pytube 
# from pytube.cli import on_progress 

# def download(url, id, save_dir="C:\\Users\\HJ.Kim\\Videos"):
#     yt = pytube.YouTube(url, on_progress_callback=on_progress) # youtube 오브젝스 생성, on_progess_callback은 video stream 의 chunk 가 다운로드 됐을때 마다 실행되는 함수. 여기서는 프로그래서 바를 그리는 용도
#     stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()# progressive는 스트리밍 서비스의 종류. mp4 포멧의 비디오 파일만 필터링.
#     filepath = stream.download(save_dir) #다운로드.
    
# if __name__=='__main__':
#     s = HTMLSession()
#     urls = ['https://www.youtube.com/watch?v=5NBAtp-kTWY&list=PLrpXwtuxGqcLXzZ5pchcprhqx_dignFiS']
#     total=0
#     i=0
#     save_dir = 'C:\\Users\\HJ.Kim\\Videos'
#     for url in urls:
#         r = s.get(url) # 원하는 url에 GET request 를 보낸다. 
#         r.html.render(sleep=0, keep_page = True, scrolldown = 10) # get 한 웹페이지를 해석하는 부분이라고 생각하면 됨
#         length= len(r.html.find('a#video-title'))
#         total+=length
#         for links in r.html.find('a#video-title'): #위 url 페이지에 리스팅된 제목에 해당하는 영상들의 정보를 검색
#             link = next(iter(links.absolute_links)) # 각 리스팅된 영상중 하나의 url을 받음
#             print('link:{}'.format(link))
#             try:
#                 download(link,i,save_dir) # 다울로드
#                 i+=1
#                 print(fr' number of videos:{i}/{total}')
#             except http.client.IncompleteRead as e:
#                 print('fail: {} \n'.format(link))
                    
#         print(fr'total videos:{i}/{total}')