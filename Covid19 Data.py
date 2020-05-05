"""Assignment 6 - 04 Jacob B."""
from statistics import mean
from matplotlib import style
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Api url and the key for the api
api_url = 'https://api.smartable.ai/coronavirus/stats/US'
api_params = {
    'Cache-Control': 'no-cache',
    'Subscription-Key': '614830dd64874f6ba6d1555f7c63429b'
}

# Requests to get response data from the API
response = requests.get(url=api_url, params=api_params)

# Turns data into text
json_data = response.text
stats = json.loads(json_data)

# Pinpoints the specific part that I want to analyze
stats1 = stats['stats']['history']

# Makes the data frame therefore making the table
df = pd.DataFrame(stats1)

json.dumps(stats1, indent=4)
print(df)


def covid_19_total_data():
    """Plots the Confirmed Deaths and Recovered cases of Covid-19 for CA"""
    df1 = df["confirmed"]
    df2 = df["deaths"]
    df3 = df["recovered"]

    figure, axes = plt.subplots(1, 3, sharex='all')
    figure.suptitle('CA Covid-19 Data')
    axes[1].set_title(' ')

    # Labels for x and y axis
    axes[0].set_ylabel('Confirmed')
    axes[1].set_ylabel('Deaths')
    axes[2].set_ylabel('Recovered')

    axes[0].set_xlabel('Days (Since 2020-01-22)')
    axes[1].set_xlabel('Days (Since 2020-01-22)')
    axes[2].set_xlabel('Days (Since 2020-01-22)')

    df1.plot(ax=axes[0])
    df2.plot(ax=axes[1])
    df3.plot(ax=axes[2])
    plt.tight_layout()
    plt.show()


def slope_of_confirmed():
    """Finds the slope of the confirmed cases"""

    # Specific x and y coordinates
    xs = np.array([4, 92, 95, 96], dtype=np.float64)
    ys = np.array([2, 39561, 43700, 45006], dtype=np.float64)

    def best_fit_line_and_slope(xs1, ys1):
        """Calculates the slope and the y-intercept"""
        slope = (((mean(xs1) * mean(ys1)) - mean(xs1 * ys1)) /
                 ((mean(xs1) * mean(xs1)) - mean(xs1 * xs1)))
        y = mean(ys1) - slope * mean(xs1)
        return slope, y

    m, b = best_fit_line_and_slope(xs, ys)

    # Makes the regression line
    regression_line = [(m * x) + b for x in xs]
    style.use('ggplot')
    plt.suptitle('Trendlines')
    plt.xlabel('Days (Since 2020-01-22')
    plt.ylabel("Cases")
    plt.plot(xs, regression_line, label='Confirmed')
    plt.legend()

    # "Predicts"  confirmed cases
    predict_confirmed = 100
    predict_y = m * predict_confirmed + b
    print(f"There will be about {predict_y} confirmed cases"
          f" at {predict_confirmed} days")


def slope_of_deaths():
    """Finds the slope for the total deaths"""

    # Specific x and y coordinates
    xs = np.array([4, 92, 95, 96], dtype=np.float64)
    ys = np.array([0, 1533, 1723, 1782], dtype=np.float64)

    def best_fit_line_and_slope2(xs2, ys2):
        """Finds the slope and y intercept of the deaths"""
        slope = (((mean(xs2) * mean(ys2)) - mean(xs2 * ys2)) /
                 ((mean(xs2) * mean(xs2)) - mean(xs2 * xs2)))
        y = mean(ys2) - slope * mean(xs2)
        return slope, y

    # Makes the regression line for the total deaths
    m, b = best_fit_line_and_slope2(xs, ys)
    regression_line = [(m * x) + b for x in xs]
    style.use('ggplot')
    plt.plot(xs, regression_line, label='Deaths')
    plt.legend()

    # "Predicts" deaths
    predict_deaths = 100
    predict_y = m * predict_deaths + b
    print(f"There will be about {predict_y} deaths at {predict_deaths} days")


def slope_of_recovered():
    """Finds the slope of the recovered cases"""

    # Specific x and y coordinates
    xs = np.array([4, 92, 95, 96], dtype=np.float64)
    ys = np.array([0, 3582, 3614, 3614], dtype=np.float64)

    def best_fit_line_and_slope3(xs3, ys3):
        """Finds the best fit line for the recovered cases """
        slope = (((mean(xs3) * mean(ys3)) - mean(xs3 * ys3)) /
                 ((mean(xs3) * mean(xs3)) - mean(xs3 * xs3)))
        y = mean(ys3) - slope * mean(xs3)
        return slope, y

    # Makes the regression line for recovered cases
    m, b = best_fit_line_and_slope3(xs, ys)
    regression_line = [(m * x) + b for x in xs]
    style.use('ggplot')
    plt.plot(xs, regression_line, label='Recovered')
    plt.legend()

    # Predicts Recovered Cases
    predict_recovered = 100
    predict_y = m * predict_recovered + b
    print(f"There will be about {predict_y} recovered"
          f" at {predict_recovered} days")


def main():
    slope_of_confirmed()
    slope_of_deaths()
    slope_of_recovered()

    covid_19_total_data()


if __name__ == '__main__':
    main()

"""                   date  confirmed  deaths  recovered
0   2020-01-22T00:00:00          0       0          0
1   2020-01-23T00:00:00          0       0          0
2   2020-01-24T00:00:00          0       0          0
3   2020-01-25T00:00:00          0       0          0
4   2020-01-26T00:00:00          2       0          0
..                  ...        ...     ...        ...
92  2020-04-23T00:00:00      39561    1533       3582
93  2020-04-24T00:00:00      40834    1597       3614
94  2020-04-25T00:00:00      42596    1695       3614
95  2020-04-26T00:00:00      43700    1723       3614
96  2020-04-27T00:00:00      45157    1782       3614

[97 rows x 4 columns]
There will be about 45473.27338364266 confirmed cases at 100 days
There will be about 1786.4330817866612 deaths at 100 days
There will be about 3828.1233530491536 recovered at 100 days
"""
"""
Well Originally I was trying to predict the next cases of Covid-19 and graph them
however the models seemed kinda hard and I just couldn't figure them out so I
decided to start over basically and go a different route. So I made subplots
for California of Confirmed, Deaths, and Recovered Cases. My question changed
from when will the virus roughly end, to are deaths growing faster or slower 
compared to recovered cases? Well when comparing the two graphs individually it
looks like they are growing about the same except that as of current time there 
are more recovered cases than deaths. But when you look at the trends the 
recovered cases are growing faster than the deaths as of current times, 
since this could be different as time goes on. Also recovered cases went stagnant 
for the past couple of days, as deaths continued to increase. I also tried to 
"predict" the total confirmed cases, deaths and recoveries at 100 days using the
slope formula.
"""