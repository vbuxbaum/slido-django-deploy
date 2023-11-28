from django.shortcuts import render, redirect
from slido_app.forms import CreateVisitorForm
from slido_app.models import Visitor, Question


def index(request):
    visitor_id = request.session.get("visitor_id")

    if visitor_id:
        visitor = Visitor.objects.get(id=visitor_id)

        context = {"visitor": visitor, "questions": Question.objects.all()}

        return render(request, "index.html", context)
    else:
        return redirect("login")


def register_visitor(request):
    formulario = CreateVisitorForm()
    context = {"form": formulario}
    return render(request, "login.html", context)


def create_visitor(request):
    formulario = CreateVisitorForm(request.POST)
    if formulario.is_valid():
        formulario.save()
        request.session["visitor_id"] = formulario.instance.id
        return redirect("homepage")
    else:
        return redirect("login")


def create_question(request):
    question_text = request.POST.get("question-text")
    visitor_id = request.session.get("visitor_id")

    Question.objects.create(
        question=question_text,
        visitor=Visitor.objects.get(id=visitor_id),
    )

    return redirect("homepage")
