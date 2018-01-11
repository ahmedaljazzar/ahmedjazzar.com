from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView

from secretballot.models import Vote

from ahmedjazzarcom import models


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogView(ListView):
    model = models.Blog
    template_name = 'blog.html'


@method_decorator(csrf_exempt, name='dispatch')
class BlogPostView(DetailView):
    template_name = 'blog_post.html'
    model = models.Blog

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)

        context['voted'] = self.did_vote()
        return context

    def post(self, request, *args, **kwargs):
        voted = self.did_vote()

        if voted:
            return JsonResponse({'state': 'Already voted'}, status=406)

        obj = self.get_object()
        token = request.secretballot_token
        obj.add_vote(token=token, vote='+1')

        return JsonResponse({'state': 'Successfully voted'}, status=200)

    def did_vote(self):
        content_type = ContentType.objects.get_for_model(self.model).id
        token = self.request.secretballot_token

        return Vote.objects.filter(
            content_type=content_type,
            token=token).exists()


class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self, request, **kwargs):
        data = request.POST
        name = data['name']
        email = data['email']
        message = data['message']

        if message and email:
            models.ContactRequest.objects.create(
                name=name, email=email, message=message)

        return redirect(reverse('home'))


class HomeView(TemplateView):
    template_name = 'home.html'


class WorksView(ListView):
    template_name = 'works.html'
    model = models.Work


class WorkView(DetailView):
    template_name = 'work.html'
    model = models.Work
