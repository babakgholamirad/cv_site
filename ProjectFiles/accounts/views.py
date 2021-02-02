from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from cv.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from .forms import SignupForm
from .tokens import account_activation_token
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    template_name = 'accounts/login.html'

class DashboardView(LoginView):
    template_name = 'accounts/dashboard-base.html'

class ProjectsView(LoginView):
    template_name = 'accounts/dashboard-projects.html'


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            message = render_to_string('accounts/active_emails.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email_from = settings.EMAIL_HOST_USER
            send_mail(mail_subject,message,email_from,[to_email],html_message=message)
            # email = EmailMessage(
            #     mail_subject, message, to=[to_email],html_message=message
            # )
            # email.send()
            return render(request, 'accounts/message.html', {'icon': 'mail.gif','message':'Please confirm your email address to complete the registration'})
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return render(request, 'accounts/message.html', {'icon': 'failure.svg','message':'Thank you for your email confirmation. Now you can login your account.'})
    else:
        return render(request, 'accounts/message.html', {'icon': 'checked.svg','message':'Activation link is invalid!'})
