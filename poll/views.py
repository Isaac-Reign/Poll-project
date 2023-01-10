from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . forms import PollForm
from . models import Poll

def home(request):
	poll = Poll.objects.all()
	context = {"poll": poll}
	return render(request, 'home.html', context)

def vote(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	if request.method == "POST":
		selected_option = request.POST['poll']
		if selected_option == 'option1':
			poll.option_one_count += 1
		elif selected_option == 'option2':
			poll.option_two_count += 1
		elif selected_option == 'option3':
			poll.option_three_count += 1
		else:
			return HttpResponse(400, "Invalid form")
		poll.save()
		return redirect('result', poll.id)

	context = {"poll": poll}
	return render(request, 'vote.html', context)

def result(request, poll_id):
	poll = Poll.objects.get(id=poll_id)
	context = {"poll": poll}
	return render(request, 'result.html', context)

def create(request):
	form = PollForm
	if request.method == "POST":
		form = PollForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {"form": form}
	return render(request, 'create.html', context)

