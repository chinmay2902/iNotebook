from django.http.response import HttpResponse
from django.shortcuts import render

from inotebook.models import Notes
from inotebook.serializer import NotesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def index(request):
    notes=Notes.objects.all()
    serialized=NotesSerializer(notes,many=True)
    return  Response(serialized.data)

@api_view(["POST"])
def createNotes(request):
    serialized=NotesSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)

@api_view(["PUT","POST"])
def updateNotes(request,pk):
    note=Notes.objects.get(id=pk)
    # print(request.body)
    serialized=NotesSerializer(note,data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response("Done Update")
    return Response(serialized.data)

@api_view(["DELETE"])
def deleteNotes(request,pk):
    note=Notes.objects.get(id=pk)
    note.delete()
    return Response("Deleted record"+str(pk))