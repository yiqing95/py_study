# Create your views here.
from django.http import HttpResponse
from django.views.generic import (
    View , ListView,CreateView,UpdateView,DeleteView
    ,DetailView
)

from django.core.urlresolvers import reverse
from contacts.forms import ContactForm

from contacts.models import Contact

from contacts import forms

class ContactView(DetailView):
    model = Contact
    template_name = 'contact.html'

class MyView(View):
    # get map to the http method name
    def get(self,request,*args,**kwargs):
        return HttpResponse('Hello World')

class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'

    def get_hi(self, request, *args, **kwargs):
        return HttpResponse('Hello World')


class CreateContactView(CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contacts-new')

    def get_context_data(self, **kwargs):
        context = super(CreateContactView,self).get_context_data()
        context['target'] = reverse('contacts-edit',
                                    kwargs={
                                        'pk':self.get_object().id
                                    })
        return context

class UpdateContactView(UpdateView):
    model = Contact
    template_name = 'edit_contact.html'
     # 不需要自定义也行哦！
     # form_class = ContactForm

    def get_success_url(self):
        return reverse('contacts-list')


class DeleteContactView(DeleteView):
    model = Contact
    template_name = 'delete_contact.html'
    def get_success_url(self):
        return reverse('contacts-list')