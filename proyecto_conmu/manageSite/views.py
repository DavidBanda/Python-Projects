# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators import gzip
from django.contrib.auth.models import User
from django.http import StreamingHttpResponse, HttpResponseServerError
import cv2

# Create your views here.

context = {
        'title': 'Home'
    }


@login_required
def index(request):
    return render(request, 'manageSite/index.html', context)


@login_required
def eliminar(request):
    return render(request, 'manageSite/eliminar.html', {'title': 'Eliminar Usuario', 'users': User.objects.all()})


@login_required
def grabacion(request):
    return render(request, 'manageSite/grabacion.html', {'title': 'Grabaciones'})


@login_required
def monitoreo(request):
    return render(request, 'manageSite/monitoreo.html', {'title': 'Monitoreo'})


@login_required
def Pruebamonitoreo(request):
    return render(request, 'manageSite/Pruebamonitoreo.html', {'title': 'Monitoreo'})


class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.cascade = cv2.CascadeClassifier("/Users/DavidBanda/PycharmProjects/proyecto_conmu/manageSite/haarcascade/"
                                             "haarcascade_frontalface_alt.xml")

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_frame(self):
        ret, image = self.video.read()
        self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.rects = self.cascade.detectMultiScale(self.gray, scaleFactor=1.2, minNeighbors=3,
                                                   minSize=(50, 50))
        for (x, y, w, h) in self.rects:
            image = cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def video(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted", e)




