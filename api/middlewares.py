from flask import request

def setup_middlewares(app):
    @app.before_request
    def before_request():
        print(f"Incoming request: {request.method} {request.path}")

    @app.after_request
    def after_request(response):
        print(f"Response status: {response.status}")
        return response
