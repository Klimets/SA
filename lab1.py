import pandas as pd
from pylab import np
import matplotlib.pyplot as plt
from sklearn import linear_model


def main():
    data = pd.read_csv('forestfires.csv', index_col=False, header=0)
    x = data.wind.values
    y = data.ISI.values
    print(np.corrcoef(x, y))
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    regr = linear_model.LinearRegression()
    regr.fit(x, y)

    plt.scatter(x, y, color='black')
    plt.plot(x, regr.predict(x), color='blue', linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()


if __name__ == "__main__":
    main()
