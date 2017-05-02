from ..models import Request


class RequestRecorder:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        req = Request(
            scheme=request.scheme,
            path=request.path,
            method=request.method,
            content_type=request.content_type,
        )
        req.save()

        response = self.get_response(request)
        # print(request.path)
        return response
