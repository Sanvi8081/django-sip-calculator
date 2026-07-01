from django.shortcuts import render


def home(request):

    invested = returns = maturity = None

    if request.method == "POST":

        try:
            monthly = float(request.POST.get("monthly_investment", 0))
            annual = float(request.POST.get("annual_return", 0))
            years = int(request.POST.get("years", 0))

            monthly_rate = annual / 12 / 100
            months = years * 12

            if monthly_rate != 0:
                maturity = monthly * (
                    ((1 + monthly_rate) ** months - 1)
                    / monthly_rate
                ) * (1 + monthly_rate)
            else:
                maturity = monthly * months

            invested = monthly * months
            returns = maturity - invested

            invested = round(invested)
            returns = round(returns)
            maturity = round(maturity)

        except:
            invested = returns = maturity = None

    # ✅ IMPORTANT: ALWAYS RETURN RESPONSE
    return render(request, "home.html", {
        "invested": invested,
        "returns": returns,
        "maturity": maturity
    })