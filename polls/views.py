from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Questions
from django.utils import timezone

# Create your views here.
def index(request):
    # q = models.Questions(question_text="What is your name", pub_date=timezone.now())
    # return HttpResponse(vars(q))

    # latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    # output = ",".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/detail.html', {"question": question})

def results(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")