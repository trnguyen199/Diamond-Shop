from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsArticle
from .forms import NewsArticleForm

# Hiển thị danh sách bài viết
def news_list(request):
    articles = NewsArticle.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'articles': articles})

# Hiển thị chi tiết bài viết
def news_detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    return render(request, 'news/news_detail.html', {'article': article})

# Tạo bài viết mới
def news_create(request):
    if request.method == "POST":
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsArticleForm()
    return render(request, 'news/news_form.html', {'form': form})

# Cập nhật bài viết
def news_update(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == "POST":
        form = NewsArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsArticleForm(instance=article)
    return render(request, 'news/news_form.html', {'form': form})

# Xóa bài viết
def news_delete(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('home')
    return render(request, 'news/news_confirm_delete.html', {'article': article})
