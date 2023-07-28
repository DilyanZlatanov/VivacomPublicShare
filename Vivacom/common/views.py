from django.shortcuts import render


def base_page(request):
    return render(request, template_name='common/base.html')
