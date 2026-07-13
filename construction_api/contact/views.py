from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from core.context import site_context

from .forms import ContactMessageForm
from .models import ContactMessage


def contact_page(request):
    context = site_context()

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            saved_message = form.save()

            recipients = {settings.CONTACT_NOTIFICATION_EMAIL, settings.ADMIN_EMAIL}
            recipients.discard('')

            email_subject = f"New contact message from {saved_message.name}"
            email_body = (
                f"Name: {saved_message.name}\n"
                f"Email: {saved_message.email}\n"
                f"Phone: {saved_message.phone or 'Not provided'}\n\n"
                f"Message:\n{saved_message.message}"
            )

            try:
                if recipients:
                    send_mail(
                        email_subject,
                        email_body,
                        settings.DEFAULT_FROM_EMAIL,
                        list(recipients),
                        fail_silently=False,
                    )
                messages.success(request, 'Your message has been sent successfully and emailed to the configured inbox.')
            except Exception:
                messages.warning(request, 'Your message was saved, but the email could not be sent. Check email settings.')
            return redirect('contact')
    else:
        form = ContactMessageForm()

    context['form'] = form
    context['recent_messages'] = ContactMessage.objects.order_by('-created_at')[:5]
    return render(request, 'pages/contact.html', context)

