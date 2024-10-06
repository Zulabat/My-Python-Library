import numpy as np
import matplotlib.pyplot as plt


class Charting:

    @staticmethod
    def scatterplot(x: [], y: [], x_label='x', y_label='y'):
        """
        Creates a scatter plot of x and y data
        :param x:
        :param y:
        :param x_label: Optional parameter to specify the x-axis label
        :param y_label: Optional parameter to specify the y-axis label
        :return: Plot object
        """
        x_data = np.array(x)
        y_data = np.array(y)
        plt.scatter(x_data, y_data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        return plt
