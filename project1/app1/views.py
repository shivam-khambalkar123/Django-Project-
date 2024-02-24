from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tasks
from .serializers import TaskSerializers

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    task = Tasks.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TaskSerializers(task)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


