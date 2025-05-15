from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LostItemForm
from .models import LostItem

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

def item_list(request):
    query = request.GET.get('q')
    status_filter = request.GET.get('status')

    items = LostItem.objects.all()

    if query:
        items = items.filter(title__icontains=query)

    if status_filter and status_filter != 'all':
        items = items.filter(status=status_filter)

    items = items.order_by('-created_at')

    return render(request, 'items/item_list.html', {
        'items': items,
        'query': query,
        'status_filter': status_filter,
    })