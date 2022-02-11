from django.http import HttpResponse
from django.shortcuts import render
from personal.utils import send_mail_async
from django.template.loader import render_to_string
from core.models import User, Career
import json

user = User.objects.get(email="ps.sukhwani@gmail.com")


def home_page(request):
    data = {"user": user}
    return render(request, "home.html", data)


def load_tabs_send_mail(request):
    data = {"user": user,
            "result": False}
    for image in data["user"].gallery.all():
        if image.caption == "about":
            data["about_pic"] = image.pic.url
        if image.caption == "time_line":
            data["time_line_pic"] = image.pic.url
        if image.caption == "contact":
            data["contact_pic"] = image.pic.url
    if request.GET.get("about"):
        data["result"] = True
        return render(request, "about.html", data)
    if request.GET.get("time_line"):
        career_list = []
        career = Career.objects.all().order_by("-start_date")
        for count, career_data in enumerate(career):
            career_dict = {}
            count += 1
            if count % 2 == 0:
                career_dict["right_side"] = career_data
            else:
                career_dict["left_side"] = career_data
            career_list.append(career_dict)
        data["career"] = career_list
        data["result"] = True
        return render(request, "time_line.html", data)
    if request.GET.get("contact"):
        data["result"] = True
        return render(request, "contact.html", data)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        note = request.POST.get("note")
        email_template = render_to_string('send_email.html', {"name": name, "note": note, "email": email})
        # send_mail_async.apply_async(args=[subject, email_template, email, ["ps.sukhwani@gmail.com"]])
        send_mail_async(subject, email_template, email, ["ps.sukhwani@gmail.com"])
        data = {"sent": True}
        return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, "base.html", data)
