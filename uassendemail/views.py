from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
import os
from .models import Guest

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nama = request.POST.get('nama')
        message = request.POST.get('message')

        if email:
            guest = Guest(email=email)
            guest.save()

            # Buat isi email dengan informasi tambahan
            email_body = f"Hay {nama},\n\nSelamat Anda Telah Menjadi Peserta Yuk Langsung Cek BIB Anda."

            # Buat email dengan gambar terlampir
            email_message = EmailMessage(
                'Selamat Anda Telah Menjadi Peserta!',  # Subjek email
                email_body, # Isi email
                settings.EMAIL_HOST_USER,  # Dari (email pengirim)
                [email]  # Ke (email penerima)
            )

            # Tentukan path gambar yang akan dilampirkan
            image_path = os.path.join(settings.BASE_DIR, 'image.jpeg')

            # Buka file gambar dan tambahkan sebagai lampiran
            with open(image_path, 'rb') as image_file:
                email_message.attach('image.png', image_file.read(), 'image/jpeg')

            # Kirim email
            email_message.send(fail_silently=False)

            # Redirect dengan parameter sukses
            return redirect(f'/uassendemail/?success=True&email={email}')
    return render(request, 'uassendemail/index.html')
