from models import RequestStore
from django.db import connection
from datetime import datetime

class RequestHistory(object):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        start = datetime.now()
        response = view_func(request, *view_args, **view_kwargs)
        totalTime = (datetime.now() - start).total_seconds()
        query_count = len(connection.queries)
        RequestStore.objects.create(path=request.path,
                                    time=totalTime,
                                    query_coount=query_count)
        return response