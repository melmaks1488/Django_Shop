from apps.models import MyUser
from django.views.generic import CreateView
from apps.forms import UserForm

class UserCreateView(CreateView):
    model = MyUser
    form_class = UserForm
    success_url = '/login/'
    template_name = 'registration.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return super().form_valid(form)