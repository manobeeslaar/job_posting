from django.shortcuts import render, get_object_or_404

from .models import JobPosting

# Create your views here.
def index(request):
    active_postings = JobPosting.objects.filter(is_active=True)
    context = {
        'job_postings': active_postings,
    }
    print(context)
    return render(request, 'job_board/index.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id, is_active=True)
    context = {
        'posting': job,
    }
    return render(request, 'job_board/job_detail.html', context)