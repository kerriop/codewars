def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    # your code
    months = 0

    budget = startPriceOld

    while budget < startPriceNew:
        months += 1
        if months % 2 == 0:
            percentLossByMonth += 0.5

        startPriceOld *= (100 - percentLossByMonth) / 100
        startPriceNew *= (100 - percentLossByMonth) / 100
        budget = savingperMonth * months + startPriceOld

    return [months, round(budget - startPriceNew)]


print(nbMonths(2000, 8000, 1000, 1.5))  # , [6, 766])
