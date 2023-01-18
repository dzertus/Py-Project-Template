# Open file
"""
Handlers
"""
import logging
from logging import Logger

from ui import view, buttons

logger: Logger = logging.getLogger('handler_cls')


class DefaultHandler:
    """
    Handler
    """
    """
    Class
    """
    def __init__(self):
        """
        """
        self.value = Wallet.initial_capital
        self.curve_data_X = []
        self.curve_data_Y = []

    @staticmethod
    def draw_result(X, Y):
        """

        :param X:
        :param Y:
        :return:
        """
        plt.plot(X, Y)
        plt.show()

    def calculate_dividende(self):
        """

        :param value:
        :param dividende:
        :param monthly_invest:
        :return:
        """
        self.value = (self.value * Wallet.dividende) / 100
        return int(round(self.value, 0))

    def add_month_wage(self, monthly_invest):
        """

        :param monthly_invest:
        :return:
        """
        self.value += monthly_invest
        return int(round(self.value, 0))

    def substract_taxes(self):
        #todo
        pass

    def print_capital(self):
        #todo
        pass

    def run(self, curve = False, time_warp='year'):
        """
        :param age:
        :param value:
        :param monthly_invest:
        :param time_warp:
        :return:
        """
        self.curve_data_X, self.curve_data_Y = [], []
        for year in range(Wallet.remaining_years):
            Wallet.age += 1
            # X
            self.curve_data_X.append(Wallet.age)
            # Y
            if Wallet.age > Wallet.retirement:
                monthly_invest = 0

            self.value = self.add_month_wage( Wallet.monthly_invest * 12)
            self.value += Wallet.conges_spectacle
            self.value += self.calculate_dividende()
            if Wallet.age > Wallet.retirement:
                print(Fore.BLUE + f'{Wallet.age} : {self.value}')
            else:
                print(f'{Wallet.age} : {self.value}')
            self.curve_data_Y.append(self.value)

        if curve:
            self.draw_result(self.curve_data_X, self.curve_data_Y)
