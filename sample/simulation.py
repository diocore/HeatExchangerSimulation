import heat_exchanger
import sys

def main() -> int:
    absorption_heat_pump = heat_exchanger.absorption_heat_pump()

    absorption_heat_pump.calculate()

    W = 1000

    hex_1  = heat_exchanger.heat_exchanger(W/4)
    hex_2 = heat_exchanger.heat_exchanger(W/4)
    hex_3 = heat_exchanger.heat_exchanger(W/4)
    hex_4 = heat_exchanger.heat_exchanger(W/4)



    Q_1 = hex_1.simulate(10,50)

    Q_2 = hex_2.simulate(50, 20)

    Q_3 = hex_3.simulate(20, 70)

    Q_4 = hex_4.simulate(70, 10)

    epsilon = (Q_1 + Q_2 + Q_3 + Q_4)/ W




    return 0

if __name__ == '__main__':
    sys.exit(main())