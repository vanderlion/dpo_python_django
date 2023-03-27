from datetime import time

from django.http import HttpRequest
from django.shortcuts import render


def set_useragent_on_request_middleware(get_response):
    print("initial call")

    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response

    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exeptions_count = 0
        self.requests_time = {}

    def __call__(self, request: HttpRequest):
        time_delay = 10
        if not self.requests_time:
            print("This is first request. Dictionary is empty!")
        elif (round(time.time()) * 1) - self.requests_time['time'] < time_delay \
                and self.requests_time['ip_address'] == request.META.get('REMOTE_ADDR'):
            print("less than 10 seconds have passed since the last request from your ip-address")
            return render(request, 'requestdataapp/error-request.html')

        self.requests_time = {'time': round(time.time()) * 1, 'ip_adress': request.META.get('REMOTE_ADDR')}

        self.requests_count += 1
        print("requests count", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("response count", self.responses_count)
        return response

    def process_exeption(self, request: HttpRequest, exeption: Exception):
        self.exeptions_count += 1
        print("got", self.exeptions_count, "exeptions so far")
