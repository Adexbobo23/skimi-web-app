from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StatusUpdateForm

@login_required
def create_status(request):
    if request.method == 'POST':
        form = StatusUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            status_update = form.save(commit=False)
            status_update.user = request.user
            status_update.save()
            return redirect('core:feed')
    else:
        form = StatusUpdateForm()

    return render(request, 'status/create_status.html', {'form': form})
