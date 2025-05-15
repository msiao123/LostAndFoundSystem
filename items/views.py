from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LostItemForm
from .models import LostItem

@login_required
def report_lost_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
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

from django.shortcuts import get_object_or_404

def item_detail(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)
    return render(request, 'items/item_detail.html', {'item': item})

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import LostItemForm  # We'll create this next

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)

    if request.user != item.user:
        return HttpResponseForbidden("You are not allowed to edit this item.")

    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = LostItemForm(instance=item)

    return render(request, 'items/edit_item.html', {'form': form, 'item': item})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)

    if request.user != item.user:
        return HttpResponseForbidden("You are not allowed to delete this item.")

    if request.method == 'POST':
        item.delete()
        return redirect('item_list')

    return render(request, 'items/delete_item.html', {'item': item})

from django.views.decorators.http import require_POST

@login_required
@require_POST
def mark_as_returned(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)

    if request.user != item.user:
        return HttpResponseForbidden("You are not allowed to update this item.")

    item.status = 'returned'
    item.save()
    return redirect('item_detail', item_id=item.id)
