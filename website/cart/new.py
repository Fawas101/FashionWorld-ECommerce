class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (pre-processing)
        print("Custom Middleware: Before View")
        
        response = self.get_response(request)
        
        # Code to be executed for each response after the view (post-processing)
        print("Custom Middleware: After View")

        return response