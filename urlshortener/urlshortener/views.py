import hashlib
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from url.models import Url, AccessLog
from datetime import timedelta
from urllib.parse import urlparse

BASE_URL = "http://127.0.0.1:8000/" 

def index(request):
    if request.method == 'POST':
        input_url = request.POST.get('url')
        password = request.POST.get('password') 

        if not input_url or not is_valid_url(input_url):
            return render(request, 'index.html', {'error': 'Invalid URL provided'})

        expiry_hours_str = request.POST.get('expiry', '24') 
        try:
            expiry_hours = int(expiry_hours_str)
        except ValueError:
            expiry_hours = 24 

        hash_id = hashlib.md5(input_url.encode()).hexdigest()[:6] + str(random.randint(1000, 9999))  
        url, created = Url.objects.get_or_create(
            long_url=input_url,
            defaults={
                'short_url': hash_id,
                'expires_at': now() + timedelta(hours=expiry_hours),
                'password': password  
            }
        )

        new_url = BASE_URL + url.short_url
        return render(request, 'index.html', {'new_url': new_url, 'expires_at': url.expires_at})

    return render(request, 'index.html')


def shorten(request, short_id):
    url = get_object_or_404(Url, short_url=short_id)

    if now() > url.expires_at:
        return render(request, 'expired.html') 
    if url.password: 
        if request.method == 'POST': 
            entered_password = request.POST.get('password')
            if entered_password != url.password:  
                return render(request, 'password_required.html', {'short_url': short_id, 'error': 'Incorrect password'})
            else:
                url.access_count += 1
                url.save()

                ip_address = get_client_ip(request)
                AccessLog.objects.create(url=url, ip_address=ip_address)

                return redirect(url.long_url)

        return render(request, 'password_required.html', {'short_url': short_id})

    url.access_count += 1
    url.save()

    ip_address = get_client_ip(request)
    AccessLog.objects.create(url=url, ip_address=ip_address)

    return redirect(url.long_url)


def analytics(request, short_id):
    url = get_object_or_404(Url, short_url=short_id)
    logs = url.logs.all()

    return render(request, 'analytics.html', {'url': url, 'logs': logs})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def is_valid_url(url):
    """Validate the provided URL format."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
