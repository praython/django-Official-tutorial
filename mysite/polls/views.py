from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    """
     * ListView generic view uses a default template called <app name>/<model name>_list.html
    """
    # we use template_name to tell ListView to use our existing "polls/index.html" template
    template_name = 'polls/index.html'
    # for ListView, the automatically generated context variable is question_list. 
    # To override this we provide the context_object_name attribute, specifying that 
    # we want to use latest_question_list instead
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """
     * Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.
     * The DetailView generic view expects the primary key value captured from the URL to be called "pk", 
       so we’ve changed question_id to pk for the generic views.
     * By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html
    """
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    