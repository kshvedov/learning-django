from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from classroom.models import Teacher
from classroom.forms import ContactForm

# Create your views here.
# def home_view(request):
#     return render(request, "classroom/home.html")

class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"

class TeacherCreatView(CreateView):
    model =  Teacher
    fields = "__all__"
    #success_url = reverse_lazy("classroom:thank_you")
    success_url = reverse_lazy("classroom:list_teacher")
    
class TeacherListView(ListView):
    model =  Teacher
    queryset = Teacher.objects.order_by("first_name")
    context_object_name = "teacher_list"
    #fields = "__all__"
    #success_url = reverse_lazy("classroom:thank_you")

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ["last_name", "subject"]
    success_url = reverse_lazy("classroom:list_teacher")

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy("classroom:list_teacher")

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"

    # URL? URL NOT A TEMPLATE FILE
    #success_url = "/classroom/thank_you/"
    success_url = reverse_lazy("classroom:thank_you")

    # What to do with form
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
