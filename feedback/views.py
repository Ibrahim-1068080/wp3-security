from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.shortcuts import render
from .models import Feedback
from django.contrib.auth.decorators import login_required

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thanks')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

from django.shortcuts import render

def feedback_thanks(request):
    return render(request, 'bedank.html')

@login_required
def view_feedback(request):
    if not request.user.organisatie:
        return redirect('some_other_page')

    feedback_list = Feedback.objects.all()
    return render(request, 'view_feedback.html', {'feedback_list': feedback_list})

