import typing
import math


class heat_exchanger():
    m_dot = 0.1  # kg/s
    T_in = 80  # °C
    T_out = 50  # °C
    c_p = 1000  # J/kg-K
    #c_p2 = 1000  # J/kg-K
    A = 1  # m^2
    U = 1000  # W/m^2-K

    W = 1000

    # Heat transfer rate
    Q_dot = m_dot * c_p * (T_in - T_out)



    # Heat capacity rate
    C_dot = m_dot * c_p1

    def __init__(self,W):
        self.W = W
        pass

    #def effectiveness(self) -> float:
        #return (1 - math.exp(-U * A / C_min1)) / (1 - C_r1 * math.exp(-U * A / C_min1))

    def COP(self) -> float:
        Q  = m_dot * c_p1 * (T_in - T_out)
        return Q / W

    def simulate(self, T_in, T_out) -> float:
        Q_dot = m_dot * c_p * (T_out - T_in)
        return Q_dot




class absorption_heat_pump():

    m_d : float = 1
    """Massenstrom zufließende reiche Lösung"""

    m_a : float = 0
    """Massenstrom austretende arme Lösung"""

    m_r: float = m_a + m_d
    """Massenstrom zufließende reiche Lösung"""

    cp : float = 0
    """spezifische Wärmekapazität"""

    V : float = 0
    """Volumenstrom"""
    zeta_a : float = 0
    """Konzentration austretende Lösung"""
    zeta_d : float = 0
    """Konzentration Dampf"""
    zeta_r : float = 0
    """Konzentration zufließende reiche Lösung"""
    f : float = m_r / m_d
    """Lösungsmittelumlauf"""

    def incoming_energy(self, a):
        self.m_a
        """
        @param a: this is a parameter
        @return:
        """
        self.m
        return self.desorber_Q() + self.evaporator_Q() + self.pump_L()

    def calculate(self):
        #T_hot = 100  # Temperature of hot fluid (in Celsius)
        #T_cold = 20  # Temperature of cold fluid (in Celsius)
        #m_hot = 1  # Mass flow rate of hot fluid (in kg/s)
        #m_cold = 2  # Mass flow rate of cold fluid (in kg/s)
        #Cp_hot = 4.18  # Specific heat capacity of hot fluid (in kJ/kg/K)
        #Cp_cold = 3.5  # Specific heat capacity of cold fluid (in kJ/kg/K)
        #A = 1  # Surface area of heat exchanger (in m^2)
        #U = 1000  # Heat transfer coefficient (in W/m^2/K)

        #Q = U * A * (T_hot - T_cold)  # Heat transfer rate (in W)
        #delta_T_hot = Q / (m_hot * Cp_hot)  # Change in temperature of hot fluid (in K)
        #delta_T_cold = -Q / (m_cold * Cp_cold)  # Change in temperature of cold fluid (in K)
        #T_hot_out = T_hot - delta_T_hot  # Outlet temperature of hot fluid (in Celsius)
        #T_cold_out = T_cold - delta_T_cold  # Outlet temperature of cold fluid (in Celsius)

        #print("Heat transfer rate: ", Q, "W")
        #print("Outlet temperature of hot fluid: ", T_hot_out, "Celsius")
        #print("Outlet temperature of cold fluid: ", T_cold_out, "Celsius")

        m_dot1 = 0.1  # kg/s
        m_dot2 = 0.2  # kg/s
        T_in1 = 80  # °C
        T_in2 = 20  # °C
        T_out1 = 50  # °C
        T_out2 = 50  # °C

        #### lenis vars
        c_p1 = 1
        c_p2 = 1
        d_i = 0.0254  # 1 inch in meters
        k = 0.6 # thermal conductivity of water
        h_1 = 1000
        h_2 = h_1
        d_1 = 0.25 #diameter in meter

        U = 1/ ( 1/h_1 + k/d_1 + 1/h_2)
        A = 1

        #### lenis vars



        # Heat transfer rate
        Q_dot = m_dot1 * c_p1 * (T_in1 - T_out1)

        Q_dot_idk =  m_dot2 * c_p2 * (T_out2 - T_in2)

        # Heat capacity rate
        C_dot1 = m_dot1 * c_p1
        C_dot2 = m_dot2 * c_p2

        C_min = min(C_dot1, C_dot2)
        C_max = max(C_dot1, C_dot2)
        C_r = C_min / C_max

        # Effectiveness
        epsilon = (T_in1 - T_out2) / (T_in1 - T_in2)

        epsilon_idk = (1 - math.exp(-U * A / C_min)) / (1 - C_r * math.exp(-U * A / C_min))

        print("Heat transfer rate: ", Q_dot, "W")
        print("Effectiveness: ", epsilon, "")


        #print("Outlet temperature of hot fluid: ", T_hot_out, "Celsius")
        #print("Outlet temperature of cold fluid: ", T_cold_out, "Celsius")



    def outgoing_energy(self):
        self.incoming_energy()
        return self.condensator_Q() + self.absorber_Q()

    def config(self):
        return 0

    def absorber_Q(self):
        return 0

    def evaporator_Q(self):
        return 0

    def desorber_Q(self):
        return 0

    def condensator_Q(self):
        return 0

    def pump_L(self):
        return 0

    def calculate_Q(self):
        return (self.absorber_Q() + self.desorber_Q()) / self.condensator_Q()


