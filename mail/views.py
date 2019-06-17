from django.shortcuts import render
from django.core.mail import send_mail

from.forms import MailForm

def mailform(request):
	if(request.method =='POST'):

		form = MailForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			print("name", name)
			print("not cleaned", form['name'])

			email=form.cleaned_data['email']
			send_mail(
				'Title',
				'{} {}'.format(name,email),
				'konyrat89@gmail.com',
				['gabi_777@mail.ru', 'kairatawer@gmail.com', 'diana.omarova2013@gmail.com'],
				fail_silently=False,
			)
			return render(request, 'mail_sending/result.html',{
					'name': form.cleaned_data['name'],
					'email':form.cleaned_data['email'],
			})

	else:
		form=MailForm()
		return render(request,'mail_sending/index.html', {'form':form});
