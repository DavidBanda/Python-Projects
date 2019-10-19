from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponseServerError
from django.views.decorators import gzip
import cv2
from videoStream.firebase.firebaseExampleGet import FirebaseConn

# Create your views here.


def login(request):
    return render(request, 'videoStream/login.html')


def home(request):
    obj = FirebaseConn()
    context = {
        'Data': obj.getData()
    }
    return render(request, 'videoStream/home.html', context)


class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # self.cascade = cv2.CascadeClassifier("/Users/DavidBanda/PycharmProjects/djangoStreamVideo/videoStream/haarcascade_frontalface_alt.xml")

    def __del__(self):
        self.video.release()

    # def get_frame(self):
    #     ret, image = self.video.read()
    #     ret, jpeg = cv2.imencode('.jpg', image)
    #     return jpeg.tobytes()

    def get_frame(self):
        ret, image = self.video.read()
        # self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # self.rects = self.cascade.detectMultiScale(self.gray, scaleFactor=1.2, minNeighbors=3,
        #                                  minSize=(50, 50))
        # for (x,y,w,h) in self.rects:
        #     image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def index(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted")



