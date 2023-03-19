# GRAVITAS
#### A simple physics module for python

*The current goal of the project is to have basic physics simulations available at your fingertips. Physics caluclations with the help of one function.*

#### Usage
* Run Simulation for Particle System:
   * within **[engine2.py](https://github.com/bwaklog/Gravitas/blob/683c4f23c8aa3e7fb4fbd026dc35291cb0c57035/engine2.py)**:
       * as of the time being, variables cant be changed at runtime.
       * Number of Particles in System : `NUM_PARTICLES = <integral value>`
       * Num of Rigid Bodies in System : `NUM_RIGID_BODIES = <integral value>`
       * to change the default and random initialized values for the respective systems
         ```python

         NUM_PARTICLES = 1 # any integral_value

         particles = [] # stores list of particle objects

         # line 38 - Particle Simulation
         def InitializeParticles():
            for _ in range(NUM_PARTICLES):
               particle = Particle(
                  position=vector2(x=rd.randint(0, 50), y=rd,randint(0, 50)).vec(), # range for random positioning (<start>, <stop>)
                  velocity=vector2(x=0, y=0).vec(), # provide initialized velocities
                  mass=1 # mass of particle
               )
         particles.append(particle)
         ```
         ```python
         NUM_RIGID_BODIES = 1 # any integral_value

         rigidBodies = [] # stores list of particle objects
         # line 124 - Rigid Body Simulation
         def InitializeRigidBodies():
            for _ in range(NUM_RIGID_BODIES):
               rigidBody = RigidBody(
                  position=vector2(x=rd.randint(0, 50), y=rd.randint(0, 50)), # range for random positioning (<start>, <stop>)
                  linearVelocity=vector2(x=0, y=0), # provide initialized linear velocities
                  angle=(rd.randint(0, 360))/360 * np.pi, # initialized angle in radians
                  angularVelocity=0, # initial angular velocity
                  force=vector2(x=0, y=0), 
                  torque=0,
                  shape=[1 + rd.randint(0, 2), 1 + rd.randint(0, 2), 1]
                  # shape is defined in following manner:
                  # [<width of the BoxShape>, <length of BoxShape>, <mass of BoxShape>]
               )
               # force and torque are set to 0 here (which means its intial value is null / undefined)
               # it is later on computed on calling ComputeForceAndTorque(<rigidbody>) function
        
         rigidBodies.append(rigidBody)
         ```
      

	* Within **[main.py](https://github.com/bwaklog/Gravitas/blob/dd86f2fb2e104ffd7a138e4cb8ab3af78df7a6f8/main.py)**
      
      * Simulation for rigid
         ```python
         # main.py
	      import engine2 as e2d

   # Run simulation for Particle System
   e2d.RunSimulation()
   ```
   ![Particle simulation output!](https://i.imgur.com/r8IFpgy "Particle Simulation output")

   ``` python
   import engine2 as e2d

         # Run simulation for Rigid Body System
         e2d.RunRigidBodySimulation()
	      ```
         <!-- ![Rigid Body simulation output!](https://i.imgur.com/sxSFyJa.png "Rigid Body Simulation output") -->
         <img src="https://i.imgur.com/sxSFyJa.png" width=70% height=50% alt="Rigid Body Simulation Output">

#### Features
v 0.0.2 :

   1. *Rigid Body simulations (2D) [basic simulation under gravity infulence]*

v 0.0.1 :

   1. *Partilce Simulation (2D) [basic simulation under gravity under gravity influence]*
   
#### Roadmap
v 0.0.3 + :
   1. Collision detection for Solid Objects
   2. Constrained Rigid Body Simulation

## Instructions

1. Install 

	*! pip package unavailable for the time being.*

## Credit
Introduction to Physics Simulations : https://www.toptal.com/game/video-game-physics-part-i-an-introduction-to-rigid-body-dynamics
<!-- * Solar system data : https://www.kaggle.com/datasets/jaredsavage/solar-system-major-bodies-data?resource=download -->
