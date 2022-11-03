import math
#light speed
c=1

class Particle:
    """ class rapresenting a generic particle
    """
    def __init__(self, mass, charge, name, momentum=0.):
        """Arguments:
        mass: mass in MeV/c^2
        charge: charge in units of the electron
        name: particle name
        momentum: particle initial momentum
        """
        #salvo in attributi
        self.mass=mass
        self.charge=charge
        self.name=name
        self.momentum=momentum
        #momento definito privato


    def info(self):
        """print some info about particle
        """
        msg='Particle "{}" of mass {:.3f} MeV/c^2, charge:{} e momentum {:.3f} MeV/c^2'
        return msg.format(self.name,self.mass,self.charge,self.momentum)
    @property
    def energy(self):
        """Particle energy
        """
        return math.sqrt((self.mass*c)**2 + (self.momentum*c**2)**2)
    @energy.setter
    def energy(self,value):
        """set the particle energy
        """
        if value < self.mass:
            print('cannot set the energy to value lower than the mass')
        else:
            self.momentum = math.sqrt(value**2 - (self.mass*c**2)**2)*c**2
    @property
    def momentum(self):
        return self._momentum
    @momentum.setter
    def momentum(self, value):
        if value < 0:
            print('cannot set momentum to negative value')
            print('momentum will be set to 0')
            self._momentum = 0
        else:
            self._momentum = value
            #se non entra in questo else _m non è inizializzato quindi getter fallisce
    @property
    def beta(self):
        if not (self.energy > 0):
            return 0
        else:
            return c*self.momentum/self.energy
    @beta.setter
    def beta(self,value):
        if (value < 0.) or (value > 1.):
            print('beta must be in the [0.,1.] range')
            return
        if(not(value < 1.)) and (self.mass > 0.):
            print('only massless particles can travel beta=1!')
            return
        self.momentum = c * value * self.mass/math.sqrt(1-value**2)


#classi figlie
class proton(Particle):
    """ class describing particle"""
    NAME= 'proton'
    MASS=939.  #MeV/c^2
    CHARGE=+1  #e

    def __init__(self,momentum=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)


class Alpha(Particle):
    """ class describing alpha nucleum"""
    NAME= 'alpha'
    MASS=3727.3  #MeV/c^2
    CHARGE=+4  #e

    def __init__(self,momentum=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)


if name == '__main__':
    proton= Proton(200.)
    proton.info()
    proton.beta=0.8
    proton.info()
    alpha= Alpha(20.)
    alpha.energy= 10000.
    alpha.info()





particle=Particle(105.6,charge=-1,name='Muon')
print(particle.info())
print('particle energy:{:.2f} MeV'.format(particle.energy))
particle.energy=200
print('particle energy:{:.2f} MeV'.format(particle.energy))
particle.energy=10
print('particle energy:{:.2f} MeV'.format(particle.energy))

print(particle.momentum)
particle.momentum=20
print(particle.momentum)

proton= Particle(939., charge=+1, name='proton', momentum=-10.)
print(proton.energy)
print(proton.momentum)