from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def divide(request):

	from random import randint


	num1 = randint(0, 10)

	num2 = randint(1, 10)


	if request.method == 'POST':

		answer = request.POST['answer']

		oldnum1 = request.POST['oldnum1']

		oldnum2 = request.POST['oldnum2']

		correct_answer = round(float(oldnum1) / float(oldnum2), 2)

		error = 0

		if not answer:
			error = 1
			return render(request, 'divide.html', {
				'num1' : num1,
				'num2' : num2,
				'error' : error,
				})


		else:

			if float(answer) == round(correct_answer, 2):
				myanswer = "Correct!"
				color = 'success'

			else:
				myanswer = "Incorrect"
				color = 'danger'


			return render(request, 'divide.html', {
				'answer' : answer,
				'myanswer' : myanswer,
				'num1' : num1,
				'num2' : num2,
				'correct_answer' : correct_answer,
				'color' : color,
					})


	return render(request, 'divide.html', {
		'num1' : num1,
		'num2' : num2,
		})


	return render(request, 'divide.html', {})

def add(request):

	from random import randint


	num1 = randint(0, 10)

	num2 = randint(0, 10)


	if request.method == 'POST':

		answer = request.POST['answer']

		oldnum1 = request.POST['oldnum1']

		oldnum2 = request.POST['oldnum2']

		correct_answer = int(oldnum1) + int(oldnum2)

		error = 0

		if not answer:
			error = 1
			return render(request, 'add.html', {
				'num1' : num1,
				'num2' : num2,
				'error' : error,
				})
		
		else:

			if int(answer) == correct_answer:
				myanswer = "Correct!"
				color = 'success'

			else:
				myanswer = "Incorrect"
				color = 'danger'


			return render(request, 'add.html', {
				'answer' : answer,
				'myanswer' : myanswer,
				'num1' : num1,
				'num2' : num2,
				'correct_answer' : correct_answer,
				'color' : color,
					})


	return render(request, 'add.html', {
		'num1' : num1,
		'num2' : num2,
		})

def subtract(request):
	from random import randint

	num1 = randint(0, 10)

	num2 = randint(0, 10)


	if request.method == "POST":

		answer = request.POST['answer']

		oldnum1 = request.POST['oldnum1']

		oldnum2 = request.POST['oldnum2']

		correct_answer = int(oldnum1) - int(oldnum2)

		error = 0

		if not answer:

			error = 1

			return render(request, 'subtract.html', {
				'num1' : num1,
				'num2' : num2,
				'error' : error,
				})
		
		else:


			if int(answer) == correct_answer:
					myanswer = "Correct!"
					color = 'success'

			else:
				myanswer = "Incorrect"
				color = 'danger'


			return render(request, 'subtract.html', {
				'answer' : answer,
				'myanswer' : myanswer,
				'num1' : num1,
				'num2' : num2,
				'correct_answer' : correct_answer,
				'color' : color,
					})


	return render(request, 'subtract.html', {
		'num1' : num1,
		'num2' : num2,
		})

def multiply(request):
	from random import randint


	num1 = randint(0, 10)

	num2 = randint(0, 10)


	if request.method == 'POST':

		answer = request.POST['answer']

		oldnum1 = request.POST['oldnum1']

		oldnum2 = request.POST['oldnum2']

		correct_answer = int(oldnum1) * int(oldnum2)

		error = 0

		if not answer:
			error = 1
			return render(request, 'multiply.html', {
				'num1' : num1,
				'num2' : num2,
				'error' : error,
				})
		
		else:

			if int(answer) == correct_answer:
				myanswer = "Correct!"
				color = 'success'

			else:
				myanswer = "Incorrect"
				color = 'danger'


			return render(request, 'multiply.html', {
				'answer' : answer,
				'myanswer' : myanswer,
				'num1' : num1,
				'num2' : num2,
				'correct_answer' : correct_answer,
				'color' : color,
					})


	return render(request, 'multiply.html', {
		'num1' : num1,
		'num2' : num2,
		})
	

