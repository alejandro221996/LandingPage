from django.shortcuts import redirect, render
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.


def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Success
            email = EmailMessage(
                "Busco informacion sobre una cita ",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "{}".format(email),
                ["alejandro1996221@gmail.com"],
                reply_to=[email]
            )

            try:
                # OK
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                # FAIL
                return redirect(reverse('contact')+'?fail')

        # return HttpResponse("Contacto")
    return render(request, "contact/contact.html", {'form': contact_form})
