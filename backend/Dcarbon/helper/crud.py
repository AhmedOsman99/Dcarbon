from rest_framework import status


def getAll(model, modelSerializer):
    try:
        all_instances = model.objects.all()
    except Exception as e:
        data = {"Error": f"An error occurred => {e}"}
        http_status = status.HTTP_404_NOT_FOUND
    else:
        model_serializer = modelSerializer(
            all_instances, many=True)
        data = model_serializer.data
        http_status = status.HTTP_200_OK
    return data, http_status


def getById(id, model, modelSerializer):
    try:
        instance = model.objects.get(id=id)
    except Exception as e:
        data = {"Error": f"An error occurred => {e}"}
        http_status = status.HTTP_404_NOT_FOUND
    else:
        model_serializer = modelSerializer(
            instance)
        data = model_serializer.data
        http_status = status.HTTP_200_OK
    return data, http_status


def addInstance(request, modelSerializer):
    try:
        model_serializer = modelSerializer(data=request.data, context={'request':request})
    except Exception as e:
        data = {"Error": f"An error occurred => {e}"}
        http_status = status.HTTP_400_BAD_REQUEST
    else:
        if model_serializer.is_valid():
            model_serializer.save()
            data = model_serializer.data
            http_status = status.HTTP_201_CREATED
        else:
            data = model_serializer.errors
            http_status = status.HTTP_400_BAD_REQUEST
    return data, http_status


def editInstance(request, id, model, modelSerializer):
    try:
        instance = model.objects.get(id=id)
    except Exception as e:
        data = {"Error": f"An error occurred => {e}"}
        http_status = status.HTTP_404_NOT_FOUND
    else:
        model_serializer = modelSerializer(instance=instance, data=request.data)
        if model_serializer.is_valid():
            model_serializer.save()
            data = model_serializer.data
            http_status = status.HTTP_202_ACCEPTED
        else:
            data = model_serializer.errors
            http_status = status.HTTP_400_BAD_REQUEST
    return data, http_status
    

def deleteInstance(request, id, model):
    try:
        instance = model.objects.get(id=id)
    except Exception as e:
        data = {"Error": f"An error occurred => {e}"}
        http_status = status.HTTP_404_NOT_FOUND
    else:
        instance.delete()
        data = {"message": "Instance deleted successfully"}
        http_status = status.HTTP_200_OK
    return data, http_status
    

