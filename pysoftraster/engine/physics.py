import math
import threading

class PhysicsObject:
    def __init__(self, id, position, velocity, mass=1.0, radius=1.0):
        self.id = id
        self.position = list(position)
        self.velocity = list(velocity)
        self.mass = mass
        self.radius = radius
        self.forces = [0.0, -9.81*mass, 0.0]  # Gravity by default

    def apply_force(self, fx, fy, fz):
        self.forces[0] += fx
        self.forces[1] += fy
        self.forces[2] += fz

    def integrate(self, dt):
        ax, ay, az = [f/self.mass for f in self.forces]
        self.velocity[0] += ax*dt
        self.velocity[1] += ay*dt
        self.velocity[2] += az*dt
        self.position[0] += self.velocity[0]*dt
        self.position[1] += self.velocity[1]*dt
        self.position[2] += self.velocity[2]*dt
        self.forces = [0.0, -9.81*self.mass, 0.0]

class PhysicsEngine:
    def __init__(self):
        self.objects = {}
        self.running = False
        self.thread = None

    def add(self, obj):
        self.objects[obj.id] = obj

    def step(self, dt):
        # Naive collision: bounce on y=0
        for obj in self.objects.values():
            obj.integrate(dt)
            if obj.position[1] < obj.radius:
                obj.position[1] = obj.radius
                obj.velocity[1] = -obj.velocity[1]*0.8

    def start(self, dt=1/60):
        self.running = True
        if not self.thread or not self.thread.is_alive():
            self.thread = threading.Thread(target=self._loop, args=(dt,))
            self.thread.start()

    def stop(self):
        self.running = False

    def _loop(self, dt):
        while self.running:
            self.step(dt)
            time.sleep(dt)