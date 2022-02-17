from apps.models import MyUser, Product
from django.views.generic import CreateView
from apps.forms import UserForm, ProductForm
from django.contrib.auth.mixins import PermissionRequiredMixin


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


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_superuser'
    model = Product
    form_class = ProductForm
    success_url = '/create_product/'
    template_name = 'create_product.html'