import numpy as np
from PySide6 import QtWidgets
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
from tespy.networks import Network



import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from qt_material import apply_stylesheet



# def absorption_heat_pump_simulation(ambient_temperature, generator_temperature, condenser_temperature,
#                                     evaporator_temperature, pump_efficiency):
#     # Konstanten und Parameter
#     cp_water = 4.186  # spezifische Wärmekapazität von Wasser in kJ/kg°C
#     cp_refrigerant = 2.09  # spezifische Wärmekapazität des Kältemittels in kJ/kg°C
#     latent_heat = 2337  # Verdampfungsenthalpie des Kältemittels in kJ/kg
#     generator_pressure = 5  # Druck im Generator in bar
#     absorber_pressure = 2  # Druck im Absorber in bar
#
#     # Berechnung der Massenströme
#     mass_flow_evap = 0.5  # Massenstrom im Verdampfer in kg/s
#     mass_flow_pump = mass_flow_evap / pump_efficiency  # Massenstrom der Pumpe in kg/s
#     mass_flow_refrigerant = mass_flow_evap / (latent_heat * (evaporator_temperature - ambient_temperature))
#
#     # Berechnung der Wärmeübertragung im Verdampfer
#     heat_transfer_evap = mass_flow_evap * cp_water * (evaporator_temperature - ambient_temperature)
#
#     # Berechnung der Wärmeübertragung im Kondensator
#     heat_transfer_cond = mass_flow_evap * cp_water * (condenser_temperature - generator_temperature)
#
#     # Berechnung des Druckverhältnisses im Verdichter
#     compression_ratio = generator_pressure / absorber_pressure
#
#     # Berechnung der Leistung des Verdichters
#     compressor_power = mass_flow_refrigerant * cp_refrigerant * (generator_temperature - condenser_temperature) / (
#             compression_ratio - 1)
#
#     # Berechnung der Energieströme im Absorber und Desorber
#     heat_absorber = mass_flow_pump * cp_water * (generator_temperature - condenser_temperature)
#     heat_desorber = mass_flow_pump * cp_water * (generator_temperature - evaporator_temperature)
#
#     # Berechnung der Leistungszahl der Wärmepumpe
#     cop = heat_transfer_evap / compressor_power
#
#     # Ausgabe der Ergebnisse
#     print("Massenstrom im Verdampfer:", mass_flow_evap, "kg/s")
#     print("Massenstrom der Pumpe:", mass_flow_pump, "kg/s")
#     print("Massenstrom des Kältemittels:", mass_flow_refrigerant, "kg/s")
#     print("Wärmeübertragung im Verdampfer:", heat_transfer_evap, "kW")
#     print("Wärmeübertragung im Kondensator:", heat_transfer_cond, "kW")
#     print("Leistung des Verdichters:", compressor_power, "kW")
#     print("Leistungszahl der Wärmepumpe:", cop)
#     print("Energiestrom im Absorber:", heat_absorber, "kW")
#     print("Energiestrom im Desorber:", heat_desorber, "kW")




from CoolProp.CoolProp import PropsSI


# def simulate_absorption_heat_pump(temp_evaporator, temp_absorber, temp_generator, temp_condenser, volume_flow_rate):
#     """
#     Simuliert eine Absorptionswärmepumpe unter der Annahme idealer Bedingungen.
#
#     Die Funktion nimmt die Temperaturen in den vier Hauptkomponenten der Wärmepumpe und den Volumenstrom als Eingabe und gibt die berechneten Drücke, Massenströme und Wärmeströme zurück.
#
#     Parameters:
#         temp_evaporator (float): Temperatur des Verdampfers in Grad Celsius.
#         temp_absorber (float): Temperatur des Absorbers in Grad Celsius.
#         temp_generator (float): Temperatur des Generators in Grad Celsius.
#         temp_condenser (float): Temperatur des Kondensators in Grad Celsius.
#         volume_flow_rate (float): Volumenstrom in m^3/s.
#
#     Returns:
#         dict: Ein Wörterbuch, das die berechneten Drücke (in Pa), Massenströme (in kg/s) und Wärmeströme (in kW) enthält.
#     """
#
#     # Umrechnung der Temperaturen in Kelvin
#     temp_evaporator += 273.15  # Temperatur in K
#     temp_absorber += 273.15  # Temperatur in K
#     temp_generator += 273.15  # Temperatur in K
#     temp_condenser += 273.15  # Temperatur in K
#
#     # Drücke berechnen
#     pressure_evaporator = PropsSI('P', 'T', temp_evaporator, 'Q', 0, 'NH3')  # Druck in Pa
#     pressure_generator = PropsSI('P', 'T', temp_generator, 'Q', 1, 'NH3')  # Druck in Pa
#
#     # Spezifisches Volumen und Dichte berechnen
#     specific_volume_evaporator = PropsSI('V', 'T', temp_evaporator, 'Q', 0, 'NH3')   # spezifisches Volumen in m^3/kg
#     specific_volume_generator = PropsSI('V', 'T', temp_generator, 'Q', 1, 'NH3')  # spezifisches Volumen in m^3/kg
#
#     # Massenströme berechnen
#     density_evaporator = 1 / specific_volume_evaporator  # Dichte in kg/m^3
#     density_generator = 1 / specific_volume_generator  # Dichte in kg/m^3
#     mass_flow_rate_evaporator = volume_flow_rate * density_evaporator  # Massenstrom in kg/s
#     mass_flow_rate_generator = volume_flow_rate * density_generator  # Massenstrom in kg/s
#
#     # Wärmeströme berechnen
#     heat_flow_input = mass_flow_rate_generator * (
#                 PropsSI('H', 'P', pressure_generator, 'Q', 1, 'NH3') - PropsSI('H', 'P', pressure_evaporator, 'Q', 0,
#                                                                                'NH3')) / 1e3  # Wärmestrom in kW
#     heat_flow_output = mass_flow_rate_evaporator * (
#                 PropsSI('H', 'P', pressure_generator, 'Q', 1, 'NH3') - PropsSI('H', 'P', pressure_evaporator, 'Q', 0,
#                                                                                'NH3')) / 1e3  # Wärmestrom in kW
#
#     # Leistungszahl und Wirkungsgrad berechnen
#     coefficient_of_performance = heat_flow_output / heat_flow_input  # Leistungszahl (unitless)
#     efficiency = heat_flow_output / (heat_flow_input + heat_flow_output)  # Wirkungsgrad (unitless)
#
#     # Ausgabe
#     return {
#         'pressure_evaporator': pressure_evaporator,
#         'pressure_generator': pressure_generator,
#         'mass_flow_rate_evaporator': mass_flow_rate_evaporator,
#         'mass_flow_rate_generator': mass_flow_rate_generator,
#         'heat_flow_input': heat_flow_input,
#         'heat_flow_output': heat_flow_output,
#         'coefficient_of_performance': coefficient_of_performance,
#         'efficiency': efficiency
#     }
from HeatExchangerSimulation.HeatExchange_UI import Ui_Form


def simulate_absorption_heat_pump(evaporator_temperature: float, desorber_temperature: float,
                                  condenser_temperature: float, absorber_temperature: float,
                                  volumetric_flow_rate: float, coolant='NH3'):
    """
    Diese Funktion simuliert eine Absorptionswärmepumpe.

    Parameters:
    evaporator_temperature (float): Die Temperatur des Verdampfers in Grad Celsius.
    generator_temperature (float): Die Temperatur des Generators in Grad Celsius.
    condenser_temperature (float): Die Temperatur des Kondensators in Grad Celsius.
    absorber_temperature (float): Die Temperatur des Absorbers in Grad Celsius.
    volumetric_flow_rate (float): Der Volumenstrom in m³/s.

    Returns:
    dict: Ein Wörterbuch, das die berechneten Größen enthält.
    """


    # Konvertiere die Eingabetemperaturen in Kelvin
    evaporator_temperature += 273.15
    desorber_temperature += 273.15
    condenser_temperature += 273.15
    absorber_temperature += 273.15


    # Überprüfe den gültigen Temperaturbereich für NH3
    min_temp = PropsSI('Tmin', coolant) - 273.15
    max_temp = PropsSI('Tmax', coolant) - 273.15
    if any(temp < min_temp or temp > max_temp for temp in [evaporator_temperature, desorber_temperature,
                                                           condenser_temperature, absorber_temperature]):
        raise ValueError("Eine oder mehrere Temperaturen liegen außerhalb des gültigen Bereichs für NH3.")
    liquid = 0
    vapor = 1


    # Berechne die Drücke
    evaporator_pressure = PropsSI('P', 'T', evaporator_temperature, 'Q', liquid, coolant)  # Pa
    generator_pressure = PropsSI('P', 'T', desorber_temperature, 'Q', vapor, coolant)  # Pa

    # Berechne die spezifischen Volumina
    specific_volume_evaporator = 1 / PropsSI('D', 'T', evaporator_temperature, 'Q', liquid, coolant)  # m³/kg
    specific_volume_generator = 1 / PropsSI('D', 'T', desorber_temperature, 'Q', vapor, coolant)  # m³/kg

    # Berechne die Massenströme
    mass_flow_rate_evaporator = volumetric_flow_rate / specific_volume_evaporator  # kg/s
    mass_flow_rate_generator = volumetric_flow_rate / specific_volume_generator  # kg/s

    # Berechne die Wärmeströme
    enthalpie_desorb = PropsSI('H', 'P', generator_pressure, 'Q', vapor, coolant)
    enthalpie_evapo = PropsSI('H', 'P', evaporator_pressure, 'Q', liquid, coolant)
    enthalpie_absorb = PropsSI('H', 'T', absorber_temperature, 'Q', liquid, coolant)
    enthalpie_conden = PropsSI('H', 'T', condenser_temperature, 'Q', liquid, coolant)

    Q_evaporator = mass_flow_rate_evaporator * (enthalpie_absorb - enthalpie_conden)  # W
    Q_condenser = mass_flow_rate_generator * (enthalpie_desorb - enthalpie_evapo)  # W

    Q_absorber = 1
    Q_generator = 1


    # Berechne die Leistungszahl (COP)
    cop = (Q_condenser + Q_absorber) / Q_generator


    return {"Heat Input": Q_evaporator / 1e3,  # kW
            "Heat Output": Q_condenser / 1e3,  # kW
            "COP": cop / 1e3}

def main():
    # absorption_heat_pump_simulation(20, 80, 50, -10, 0.8)

    simulation_results = simulate_absorption_heat_pump(-40, 40, 10, 20, 0.05, 'NH3')
    for key, value in simulation_results.items():
        print(f"{key}: {value}")





# Beispielaufruf der Funktion


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()

        self.ui.setupUi(self)

        with plt.style.context("rose-pine-moon"):
            sc = MplCanvas(self, width=5, height=4, dpi=100)

            # Example data
            x = [*range(0, 20)]
            y = [*range(0, 20)]

            for i in y:
                y[i] = i*i

            # Generate additional points for smooth curve
            x_smooth = np.linspace(min(x), max(x), 200)
            y_smooth = np.interp(x_smooth, x, y)

            sc.axes.plot(x_smooth, y_smooth, '-')

            self.ui.layoutPlot_01.addWidget(sc)

        self.ui.simulateButton.clicked.connect(self.simulate_clicked)

    def simulate_clicked(self):

        evaporator_T = float(self.ui.evaporator_temperature.text())
        desorber_T = float(self.ui.desorber_temperature.text())
        condenser_T = float(self.ui.condenser_temperature.text())
        absorber_T = float(self.ui.absorber_temperature.text())
        volume_flow_rate = float(self.ui.volumetric_flow_rate.text())
        coolant = self.ui.coolant_var.text()
        simulation_results = simulate_absorption_heat_pump(evaporator_T,
                                                           desorber_T,
                                                           condenser_T,
                                                           absorber_T,
                                                           volume_flow_rate,
                                                           coolant)
        for key, value in simulation_results.items():
            print(f"{key}: {value}")


        print('hallo')
        # self.ui.tabWidget.indexOf(0).



class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)



if __name__ == "__main__":
    main()

    app = QApplication(sys.argv)

    apply_stylesheet(app, theme='dark_lightgreen.xml')

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

