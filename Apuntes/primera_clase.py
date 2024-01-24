import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as anim 
from tqdm import tqdm

class Particle:
    def __init__(self, r0, v0, a0, t, m=1, radius=2, id=0) -> None:
        self.dt = t[1] - t[0]

        # Atributos Instantaneos
        self.r = r0
        self.v = v0
        self.a = a0

        self.m = m
        self.radius = radius
        self.id = id

        self.p = self.m*self.v

        # Historial

        self.R = np.zeros((len(t),len(r0)))
        self.V = np.zeros_like(self.R)
        self.A = np.zeros_like(self.R)

        self.F = np.zeros_like(self.R)

        self.K = 10

    def setPosition(self, i):
        self.R[i] = self.r

    def Evolution(self, i):

        self.setPosition(i)
        self.r += self.dt*self.v
        self.v += self.dt*self.a

    
    def getPosition(self, scale=1):
        return self.R[::scale]

dt = 0.01
tmax = 10
t = np.arange(0,tmax,dt)

print(t)

def GetParticle(N):

    ret = []

    for _ in range(N):
        r0 = np.random.rand(2) * 40
        v0 = np.random.rand(2) * 10
        a0 = np.random.rand(2) * 10
    
        p = Particle(r0, v0, a0, t)
        ret.append(p)

    return ret

def runSimulation(t, particle):
    for it in range(len(t)):
        for i in range(len(particle)):
            particle[i].Evolution(it)

p = GetParticle(50)
runSimulation(t, p)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(121)
# ax1 = fig.add_subplot(122)

def init():

    ax.clear()
    ax.set_xlim(0,80)
    ax.set_ylim(0,80)

def Update(i):

    init()

    for part in p:
        x = part.getPosition()[i,0]
        y = part.getPosition()[i,1]

        circle = plt.Circle( (x,y), part.radius, color='r', fill=True )
        ax.add_patch(circle)

animation = anim.FuncAnimation(fig, Update ,frames=len(t), init_func=init)
plt.show()
