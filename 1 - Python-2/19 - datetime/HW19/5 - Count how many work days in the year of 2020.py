holidays = """
    New Year's Day                Wed, Jan 1, 2020
    Martin Luther King Jr. Day    Mon, Jan 20, 2020
    Memorial Day                    Mon, May 25, 2020
    Independence Day                Fri, Jul 3, 2020
    Labor Day                      Mon, Sep 7, 2020
    Veterans Day                    Wed, Nov 11, 2020
    Thanksgiving                    Thu, Nov 26, 2020
    Christmas Day                  Fri, Dec 25, 2020
    """

holidays = holidays.split("   ")
holidays = [el.strip() for el in holidays ]
print(holidays)