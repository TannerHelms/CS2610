import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.timezone import make_aware

import shootout.models
from shootout.models import Expressions
from django.shortcuts import render


# Create your views here.
def index(request):
    expressions = Expressions.objects.order_by('id').reverse()[:5]
    context = {'expressions': expressions}
    return render(request, 'shootout/index.html', context)

def plan(request):
    return render(request, 'shootout/plan.html')


def recent_expressions(request):
    expressions = Expressions.objects.order_by('id').reverse()
    context = {'expressions': expressions}
    return render(request, 'shootout/recentExpressions.html', context)


def undefined_expressions(request):
    expressions = Expressions.objects.order_by('id').reverse()
    undefinedExpressions = []
    for e in expressions:
        if e.total is None:
            undefinedExpressions.append(e)
    context = {'expressions': undefinedExpressions}
    return render(request, 'shootout/undefinedExpressions.html', context)


def disagreeing_results(request):
    expressions = Expressions.objects.order_by('id').reverse()
    disagreeing_expressions = []
    for e in expressions:
        match e.operator:
            case '+':
                if e.firstOperand + e.secondOperand != e.total:
                    disagreeing_expressions.append([e, e.firstOperand + e.secondOperand])
            case '-':
                if e.firstOperand - e.secondOperand != e.total:
                    disagreeing_expressions.append([e, e.firstOperand - e.secondOperand])
            case '*':
                if e.firstOperand * e.secondOperand != e.total:
                    disagreeing_expressions.append([e, e.firstOperand * e.secondOperand])
            case '/':
                if e.secondOperand == 0:
                    continue
                if e.firstOperand / e.secondOperand != e.total:
                    disagreeing_expressions.append([e, e.firstOperand / e.secondOperand])
            case '%':
                if e.firstOperand % e.secondOperand != e.total:
                    disagreeing_expressions.append([e, e.firstOperand % e.secondOperand])
            case '**':
                if e.firstOperand ** e.secondOperand != float(e.total):
                    disagreeing_expressions.append([e, e.firstOperand ** e.secondOperand])
    context = {'expressions': disagreeing_expressions}
    return render(request, 'shootout/disagreeingResults.html', context)


def expressions_operator(request):
    expressions = Expressions.objects.order_by('id').reverse()
    expressionDictionary = {}
    plus = []
    minus = []
    mult = []
    div = []
    mod = []
    ex = []
    for e in expressions:
        match e.operator:
            case '+':
                plus.append(e)
            case '-':
                minus.append(e)
            case '*':
                mult.append(e)
            case '/':
                div.append(e)
            case '%':
                mod.append(e)
            case '**':
                ex.append(e)
    context = {'expressions': [[plus, "green", "Addition Expressions (+)"],
                               [minus, "blue", "Subtraction Expressions (-)"],
                               [mult, "cyan", "Multiplication Expressions (*)"],
                               [div, "white", "Division Expressions (/)"],
                               [mod, "black", "Remainder Expressions (%)"],
                               [ex, "blue", "Exponentiation Expressions (**)"]]}
    return render(request, 'shootout/expressionsByOperator.html', context)


def save(request):
    first_op = float(request.POST['firstop'])
    second_op = float(request.POST['secondop'])
    operator = request.POST['operator']
    total = request.POST['total']
    expression = Expressions()
    expression.firstOperand = first_op
    expression.secondOperand = second_op
    if total != "Undefined":
        expression.total = float(total)
    expression.operator = operator
    expression.date_created = make_aware(datetime.datetime.now())
    expression.save()
    return HttpResponseRedirect(reverse('shootout:index'))


def delete(request, expression_id):
    Expressions.objects.filter(id=expression_id).delete()
    return HttpResponseRedirect(reverse('shootout:index'))
