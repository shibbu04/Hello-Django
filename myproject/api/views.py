from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connections

@api_view(['GET'])
def hello_world(request):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT 1')
            return Response({
                "message": "Hello World!",
                "database": "Successfully connected to MySQL"
            })
    except Exception as e:
        return Response({
            "message": "Hello World!",
            "database": f"Connection failed: {str(e)}"
        })