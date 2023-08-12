from asgiref.sync import async_to_sync
from django.core.mail import send_mail
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from blogs.forms import BlogsCommentForm, SendMessageForm
from blogs.models import Blogs, Comment, Portfolio, Skills, Services, Messages
from PIL import Image

from django.conf import settings

from users.models import Testimonials


class HomeView(ListView):
    model = Blogs
    template_name = 'blogs/home_page.html'
    ordering = ['-id']

    def get_queryset(self):
        queryset = super(HomeView, self).get_queryset()
        blogs_id = self.kwargs.get('blog_id')
        if blogs_id:
            queryset = queryset.filter(blogs_id=blogs_id).annotate(num_comments=Count('comment'))
            return queryset.filter(blogs_id=blogs_id)
        else:
            queryset = queryset.annotate(num_comments=Count('comment'))
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["portfolio"] = Portfolio.objects.all()
        context["skills"] = Skills.objects.all()
        context["services"] = Services.objects.all()
        context['form'] = SendMessageForm()
        context['testimonials'] = Testimonials.objects.all()
        context['clients_with_images'] = Testimonials.objects.filter(image__isnull=False)
        return context


class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs/blogs.html'
    paginate_by = 8
    ordering = ['-id']

    def get_queryset(self):
        queryset = super(BlogsListView, self).get_queryset()
        blogs_id = self.kwargs.get('blog_id')
        if blogs_id:
            queryset = queryset.filter(blogs_id=blogs_id).annotate(num_comments=Count('comment'))
            return queryset.filter(blogs_id=blogs_id)
        else:
            queryset = queryset.annotate(num_comments=Count('comment'))
            return queryset

    # def get_context_data(self, *, object_list=None, **kwargs):
    # context = super(BlogsListView, self).get_context_data()
    # context['blogs'] = Blogs.objects.all()
    # return context


def BlogsDetailView(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id)
    next_blog = Blogs.objects.filter(id=blog_id + 1)
    previous_blog = Blogs.objects.filter(id=blog_id - 1)
    comments = Comment.objects.filter(
        Q(blog=blog) & (Q(parent_comment__isnull=True))
    ).prefetch_related('child_comments')

    context = {
        'blog': blog,
        'blog_id': blog_id,
        'comments': comments
    }

    if next_blog:
        context['next_blog'] = next_blog[0]
    if previous_blog:
        context['previous_blog'] = previous_blog[0]

    if request.method == 'POST':
        form = BlogsCommentForm(request.POST)
        if form.is_valid():
            parent_comment_id = request.POST.get('parent_comment_id', None)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']

            comment = Comment(
                parent_comment_id=parent_comment_id,
                blog=blog,
                name=name,
                email=email,
                text=text,
            )
            comment.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = BlogsCommentForm()

    context['form'] = form
    return render(request, 'blogs/blog-details.html', context=context)


def CommentDeleteView(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class CreateMessageView(CreateView):
    model = Messages
    form_class = SendMessageForm
    template_name = "blogs/home_page.html"

    def get_success_url(self):
        return reverse_lazy('home_page', )

    def form_valid(self, form):
        # Save the form instance to get the object
        self.object = form.save()

        # Sending the email
        subject = 'Новое сообщение.'
        message = f'Привет\n\nУ вас новое сообщение от {self.object.name} ({self.object.email}).\n\nСообщение: \n{self.object.message}'
        from_email = settings.EMAIL_HOST_USER  # Replace with your email
        recipient_list = ['storeserver065@gmail.com']  # Replace with the recipient's email address

        # Send the email
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False
        )

        return super().form_valid(form)





# def SendMessageView(request):
#     if request.method == 'POST':
#         form = SendMessageForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#
#             # Здесь можно добавить логику для отправки письма
#             # Ниже пример отправки через функцию send_mail Django
#             subject = f'Сообщение от {name}'
#             from_email = email
#             recipient_list = ['shavkatkurbanov065@gmail.com']
#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#
#             # Дополнительная логика, если необходимо, например, перенаправление на другую страницу
#             return render(request, 'blogs/home_page.html')
#
#         else:
#             form = SendMessageForm()
#     return render(request, 'blogs/home_page.html')

# def LikeBlog(request, blog_id):
#     if request.method == 'POST':
#         try:
#             blog = Blogs.objects.get(pk=blog_id)
#         except Blogs.DoesNotExist:
#             return JsonResponse({'error': 'Blog not found'}, status=404)
#
#         user_id = request.COOKIES.get('liked_user_id')
#
#         if user_id and user_id in blog.liked_by_user_ids():
#             return JsonResponse({'error': 'Already liked'}, status=400)
#
#         blog.likes += 1
#         if user_id:
#             blog.liked_by_user_ids.append(user_id)
#         blog.save()
#
#         response = JsonResponse({'likes': blog.likes})
#         if not user_id:
#             response.set_cookie('liked_user_id', value=str(request.user.id), max_age=365 * 24 * 60 * 60)
#
#         return response
#     else:
#         return JsonResponse({'error': 'Invalid request'}, status=400)

# class BLogsDetailView(TitleMixin, TemplateView):
#     template_name = 'blogs/blog-details.html'
#
#     def get_queryset(self):
#         queryset = super(BLogsDetailView, self).get_queryset()
#         blog_id = self.kwargs.get('blog_id')
#         return queryset.filter(blog_id=blog_id)

# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super(ProductsListView, self).get_context_data()
#     context['categories'] = ProductCategory.objects.all()
#     return context
