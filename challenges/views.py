from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import logging

monthly_challenges = {
    "january": "Eat no burger for the entire month",
    "february": "Walk for at least 30 minutes every day!",
    "march": "Learn Django for at least 2 hour every day!",
    "april": "Eat no burger for the entire month",
    "may": "Walk for at least 30 minutes every day!",
    "june": "Learn Django for at least 2 hour every day!",
    "july": "Eat no burger for the entire month",
    "august": "Walk for at least 30 minutes every day!",
    "september": "Learn Django for at least 2 hour every day!",
    "october": "Eat no burger for the entire month",
    "november": "Walk for at least 30 minutes every day!",
    "december": "Learn Django for at least 2 hour every day!",
}


def challenge_list(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("This month is not supported")
