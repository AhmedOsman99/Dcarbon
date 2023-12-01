from rest_framework import status


def get_by_id(model, id):
    try:
        instance = model.objects.get(id=id)
        return instance, None   
    except Exception as e:
        data = {"Error": f"An error occurred => {e}"}
        # http_status = status.HTTP_404_NOT_FOUND
        # return data, http_status
        return None, data