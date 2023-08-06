from django.shortcuts import render, redirect, get_object_or_404
from .models import Entries
from .forms import EntryForm


def index(request):
    entries = Entries.objects.order_by('-date_posted')

    context = {'entries': entries}
    return render(request, 'entries/index.html', context)


def add(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            form.save()
            return redirect('home')
    else:
        form = EntryForm()

    context = {'form': form}
    return render(request, 'entries/add.html', context)


def edit(request):
    return render(request, 'entries/edit.html')


def delete_entry(request, entry_id):
    entry = get_object_or_404(Entries, id=entry_id)
    if request.method == 'POST':
        entry.delete()
    return redirect('home')


def edit_entry(request, entry_id):
    entry = get_object_or_404(Entries, id=entry_id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm(instance=entry)

    context = {'form': form}
    return render(request, 'entries/edit.html', context)


def detail_entry(request, entry_id):
    entry = get_object_or_404(Entries, id=entry_id)
    context = {'entry': entry}
    return render(request, 'entries/detail.html', context)
