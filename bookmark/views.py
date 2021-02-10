from django.views.generic import ListView, DetailView
from django.shortcuts import render
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark