from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ("title", "body", "tags")


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


@login_required
def vote(request, pk, vote_type):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if vote_type in ["up", "down"]:
        # Check if the user has already voted on this post
        existing_vote = post.vote_set.filter(user=user).first()
        if existing_vote:
            existing_vote.vote_type = vote_type
            existing_vote.save()
            messages.success(request, "Vote updated successfully.")
        else:
            post.vote_set.create(user=user, vote_type=vote_type)
            messages.success(request, "Vote added successfully.")
    else:
        messages.error(request, "Invalid vote type.")

    return redirect("post_detail", pk=pk)
