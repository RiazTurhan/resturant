from django.shortcuts import render

def calculator(request):
  output = ''
  first = ''
  last = ''
  opr = ''
  
  if request.method == 'POST':
    first = eval(request.POST.get('n1'))
    last = eval(request.POST.get('n2'))
    opr = request.POST.get('operator')

    if opr == '+':
        output = first + last
    elif opr == '-':
        output = first - last
    elif opr == '*':
        output = first * last
    elif opr == '/':
        output = first / last

  return render(request, 'calculator.html', {'result': output, 'n1': first ,'n2': last, 'opr': opr})