from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import QuestionSerializer
from .models import Question
from helper.crud import getAll, getById, addInstance, editInstance, deleteInstance
from django.shortcuts import get_object_or_404
from rest_framework import status



# Create your views here.
@api_view(['post'])
@permission_classes([IsAuthenticated])
def add_question(request):
    data, http_status = addInstance(request, QuestionSerializer)
    return Response(data=data, status=http_status)


@api_view(['get'])
def get_questions(request):
    data, http_status = getAll(Question, QuestionSerializer)
    return Response(data=data, status=http_status)

@api_view(['put'])
@permission_classes([IsAuthenticated])
def add_answer(request):
    print(request.data)
    for question in request.data:
        try:            
            instance = get_object_or_404(Question, id=question['id'])
        except Exception as e:
                data = {"Error": f"An error occurred => {e}"}
                http_status = status.HTTP_404_NOT_FOUND
                return Response(data=data, status=http_status)
        else:
            model_serializer = QuestionSerializer(instance=instance, data=question)
            if model_serializer.is_valid():
                model_serializer.save()
            else:
                data = model_serializer.errors
                http_status = status.HTTP_400_BAD_REQUEST
                return Response(data=data, status=http_status)
    data = "Data is updated successfully"
    http_status = status.HTTP_202_ACCEPTED
    return Response(data=data, status=http_status)