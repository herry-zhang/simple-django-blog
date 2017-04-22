from django.shortcuts import render


def markdown_edit(request):
    return render(request, 'api/markdown.html')
