from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LostItemForm

@login_required
def report_lost_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST)
        if form.is_valid():
            lost_item = form.save(commit=False)
            lost_item.user = request.user
            lost_item.save()
            return redirect('home')
    else:
        form = LostItemForm()
    return render(request, 'items/report_lost_item.html', {'form': form})
