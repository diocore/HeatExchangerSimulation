from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import sys
from PySide6.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet

from CoolProp.CoolProp import PropsSI
from HeatExchangerSimulation.HeatExchange_UI import Ui_Form

def simulate_absorption_heat_pump_Mixture(evaporator_temperature: float, desorber_temperature: float,
                                          condenser_temperature: float, absorber_temperature: float,
                                          m_dot_coolant: float, m_dot_solvent: float, coolant='NH3'):
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
    solvent = 'water'

    # Konvertierung der Eingabetemperaturen in Kelvin
    evaporator_temperature += 273.15
    desorber_temperature += 273.15
    condenser_temperature += 273.15
    absorber_temperature += 273.15

    liquid = 0
    gas = 1

    absorber_temperature_in = absorber_temperature
    absorber_temperature_out = absorber_temperature_in - 20

    # Berechnung der Einlauf-Enthalpie für die Absorberlösung
    h_in_absorber_solution = PropsSI('H', 'T', absorber_temperature_in, 'Q', gas, coolant) / 1e3
    # Berechnung der Ablauf-Enthalpie für die Absorberlösung
    h_out_absorber_solution = PropsSI('H', 'T', absorber_temperature_out, 'Q', liquid, solvent) / 1e3 # kJ/kg

    desorber_temperature_in = absorber_temperature_out
    desorber_temperature_out = desorber_temperature

    # Berechnung der Einlauf-Enthalpie für die Desorberlösung
    h_in_desorber_solution = PropsSI('H', 'T', desorber_temperature_in, 'Q', liquid, solvent) / 1e3  # kJ/kg
    # Berechnung der Ablauf-Enthalpie für die Desorberlösung
    h_out_desorber_solution = PropsSI('H', 'T', desorber_temperature_out, 'Q', gas, coolant) / 1e3  # kJ/kg

    condenser_temperature_in = desorber_temperature_out
    condenser_temperature_out = condenser_temperature

    # Berechnung der Einlauf-Enthalpie für das Kondensator-Kühlmittel
    h_in_condensator_coolant = PropsSI('H', 'T', condenser_temperature_in, 'Q', gas, coolant) / 1e3  # kJ/kg
    # Berechnung der Ablauf-Enthalpie für das Kondensator-Kühlmittel
    h_out_condensator_coolant = PropsSI('H', 'T', condenser_temperature_out, 'Q', liquid, coolant) / 1e3  # kJ/kg

    evaporator_temperature_in = condenser_temperature_out
    evaporator_temperature_out = evaporator_temperature

    # Berechnung der Einlauf-Enthalpie für das Verdampfer-Kühlmittel
    h_in_evaporator_coolant = PropsSI('H', 'T', evaporator_temperature_in, 'Q', liquid, coolant) / 1e3  # kJ/kg
    # Berechnung der Ablauf-Enthalpie für das Verdampfer-Kühlmittel
    h_out_evaporator_coolant = PropsSI('H', 'T', evaporator_temperature_out, 'Q', gas, coolant) / 1e3  # kJ/kg


    Q_evaporator = m_dot_coolant * (h_out_evaporator_coolant - h_in_evaporator_coolant)
    Q_desorber = m_dot_solvent * (h_out_desorber_solution - h_in_desorber_solution)
    Q_condenser = m_dot_coolant * (h_out_condensator_coolant - h_in_condensator_coolant)
    Q_absorber = m_dot_solvent * (h_out_absorber_solution - h_in_absorber_solution)


    # Berechnung der Leistungszahl (COP)
    COP = (abs(Q_condenser) + abs(Q_absorber)) / (abs(Q_desorber) + abs(Q_evaporator))


    return {"Q_evaporator": Q_evaporator,  # kW
            "Q_condenser": Q_condenser,  # kW
            "Q_absorber": Q_absorber,  # kW
            "Q_desorber": Q_desorber,  # kW
            "COP": COP }



class MainWindow(QWidget):
    def __init__(self):
        """
           Initialisiert das MainWindow-Objekt.
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.simulateButton.clicked.connect(self.simulate_clicked)

    def simulate_clicked(self):
        """
            Wird aufgerufen, wenn der 'Simulate' Button geklickt wird.
            Führt die entsprechenden Aktionen aus.
        """
        try:
            # Abrufen von Eingangswerten aus der Benutzeroberfläche
            evaporator_T = float(self.ui.evaporator_temperature.text())
            desorber_T = float(self.ui.desorber_temperature.text())
            condenser_T = float(self.ui.condenser_temperature.text())
            absorber_T = float(self.ui.absorber_temperature.text())
            mass_flow_rate_coolant = float(self.ui.mass_flow_rate_coolant.text())
            mass_flow_rate_solvent = float(self.ui.mass_flow_rate_solvent.text())
            coolant = self.ui.coolant_var.text()

            # Simulation einer Absorptionswärmepumpe durchführen
            simulation_results = simulate_absorption_heat_pump_Mixture(evaporator_T,
                                                               desorber_T,
                                                               condenser_T,
                                                               absorber_T,
                                                               mass_flow_rate_coolant,
                                                               mass_flow_rate_solvent,
                                                               coolant)

            # Ausgabe-String vorbereiten
            output = ''
            for key, value in simulation_results.items():
                if key != 'COP':
                    output += f"{key}: {value:.2f} kW\n"
                else:
                    output += f"{key}: {value:.3f} \n"

            # Aktualisiert die Benutzeroberfläche mit den Simulationsergebnissen.
            self.ui.textEditValues.setText(output)
            # COP-Temperatur-Diagramme aufzeichnen und ausgeben
            with plt.style.context("rose-pine-moon"):
                # Evaporator Plot
                sc = MplCanvas(self, width=5, height=4, dpi=100)
                x = [*range(int(evaporator_T) - 20, int(evaporator_T) + 20)]
                y = []
                for T in x:
                    result = simulate_absorption_heat_pump_Mixture(T,
                                                               desorber_T,
                                                               condenser_T,
                                                               absorber_T,
                                                               mass_flow_rate_coolant,
                                                               mass_flow_rate_solvent,
                                                               coolant)
                    y.append(result['COP'])


                sc.axes.plot(x, y, '-')
                sc.axes.set_xlabel("Evaporator T in °C")
                sc.axes.set_ylabel("COP")


                layout = self.ui.LayoutEvaporatorPlot
                for i in reversed(range(layout.count())):
                    layout.itemAt(i).widget().setParent(None)
                layout.addWidget(sc)
            # COP-Temperatur-Diagramme aufzeichnen und ausgeben
            with plt.style.context("rose-pine-moon"):
                # Condenser Plot
                sc = MplCanvas(self, width=5, height=4, dpi=100)
                x = [*range(int(condenser_T) - 20, int(condenser_T) + 20)]
                y = []
                for T in x:
                    result = simulate_absorption_heat_pump_Mixture(evaporator_T,
                                                               desorber_T,
                                                               T,
                                                               absorber_T,
                                                               mass_flow_rate_coolant,
                                                               mass_flow_rate_solvent,
                                                               coolant)
                    y.append(result['COP'])


                sc.axes.plot(x, y, '-')
                sc.axes.set_xlabel("Condenser T in °C")
                sc.axes.set_ylabel("COP")


                layout = self.ui.LayoutCondenserPlot
                for i in reversed(range(layout.count())):
                    layout.itemAt(i).widget().setParent(None)
                layout.addWidget(sc)
            # COP-Temperatur-Diagramme aufzeichnen und ausgeben
            with plt.style.context("rose-pine-moon"):
                # Desorber Plot

                sc = MplCanvas(self, width=5, height=4, dpi=100)
                x = [*range(int(desorber_T) - 20, int(desorber_T) + 20)]
                y = []
                for T in x:
                    result = simulate_absorption_heat_pump_Mixture(evaporator_T,
                                                               T,
                                                               condenser_T,
                                                               absorber_T,
                                                               mass_flow_rate_coolant,
                                                               mass_flow_rate_solvent,
                                                               coolant)
                    y.append(result['COP'])

                sc.axes.plot(x, y, '-')
                sc.axes.set_xlabel("Desorber T in °C")
                sc.axes.set_ylabel("COP")


                layout =  self.ui.LayoutDesorberPlot
                for i in reversed(range(layout.count())):
                    layout.itemAt(i).widget().setParent(None)
                layout.addWidget(sc)
            # COP-Temperatur-Diagramme aufzeichnen und ausgeben
            with plt.style.context("rose-pine-moon"):
                # Absorber Plot
                sc = MplCanvas(self, width=5, height=4, dpi=100)
                x = [*range(int(absorber_T) - 5, int(absorber_T) + 5)]
                y = []
                for T in x:
                    result = simulate_absorption_heat_pump_Mixture(evaporator_T,
                                                                   desorber_T,
                                                                   condenser_T,
                                                                   T,
                                                                   mass_flow_rate_coolant,
                                                                   mass_flow_rate_solvent,
                                                                   coolant)
                    y.append(result['COP'])


                sc.axes.plot(x, y, '-')
                sc.axes.set_xlabel("Absorber T in °C")
                sc.axes.set_ylabel("COP")

                layout = self.ui.LayoutAbsorberPlot
                for i in reversed(range(layout.count())):
                    layout.itemAt(i).widget().setParent(None)
                layout.addWidget(sc)
        except Exception as E:
            # Giebt die Exception in der Ausgabe aus.
            self.ui.textEditValues.setText(E.__str__())


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
                Initialisiert eine Matplotlib-Leinwand in einem Qt-Anwendungsfenster.

                :param parent: Das übergeordnete Widget, zu dem die Leinwand gehören soll.
                :param width: Die Breite der Leinwand
                :param height: Die Höhe der Leinwand
                :param dpi: Die Auflösung der Leinwand (dots per inch).
        """
        # Erzeugt eine Instanz der Figure-Klasse mit der angegebenen Breite, Höhe und Auflösung
        fig = Figure(figsize=(width, height), dpi=dpi)
        # Erstellt ein Achsenobjekt innerhalb der Abbildung
        self.axes = fig.add_subplot(111)
        # Ruft den Initialisierungsmethode der Elternklasse FigureCanvasQTAgg auf
        super(MplCanvas, self).__init__(fig)


if __name__ == "__main__":

    app = QApplication(sys.argv) # Erstellen einer QApplication-Instanz

    apply_stylesheet(app, theme='dark_lightgreen.xml') # Anwendung eines Stylesheets

    window = MainWindow() # Erstellen einer MainWindow-Instanz
    window.show()  # Anzeigen des Hauptfensters

    sys.exit(app.exec())  # Start der Anwendungsereignisschleife und Beendigung des Programms nach dem Schließen des Fensters

