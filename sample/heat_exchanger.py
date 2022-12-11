import typing


class heat_exchanger():


    m_d : float = 0
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


