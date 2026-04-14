import json

from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

client = OpenAI()


def index(request):
    return render(request, "index.html")


def generate_response(question):
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield (chunk.choices[0].delta.content)


@csrf_exempt
def answer(request):
    data = json.loads(request.body)
    message = data.get("message")

    response = StreamingHttpResponse(
        generate_response(message), status=200, content_type="text/plain"
    )
    return response
