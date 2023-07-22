from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
        return Post.objects.all()


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vote_count"] = (
            self.object.vote_set.filter(vote_type="up").count()
            - self.object.vote_set.filter(vote_type="down").count()
        )

        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post_update.html"
    form_class = PostForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_object(self, queryset=None):
        post_pk = self.kwargs.get("pk")
        return get_object_or_404(Post, pk=post_pk)


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


@login_required
def vote(request, pk, vote_type):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if vote_type in ["up", "down"]:
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


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()

    return render(request, "add_comment.html", {"form": form})
