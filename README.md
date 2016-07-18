# DroneProject
 - This is a project to control a drone with a mathematical equations and more :)
 - The drone is powered via a Raspberry Pi 2, v1.1
 - Intially the drone will follow a pre-determined math equation with **high** accuracy
 - The drone will be able to think on its' own and adjust to its' environment. Ex: Use the wind as an aid

### To Do
- Include an equation parser (Read equations from a text file)
- Include a 'menu' to select between options (Different equations or demos)
- Include a derivative calculator function
- Create a function to return the direction and speed of a equation at certain time values
- A lottttttt of physics math *To Do: Expand on the physics*

### Schedule
 - Finish Math Equations:
  - ~~Request an equation(3) and assure that equation is workable **End of 7/17/2016**~~ **COMPLETED**
  - ~~Methods to return a position vector and a velocity vector **End of 7/17/2016**~~ **COMPLETED**
  - Boolean to store postion and velocity in an array to a given amount **End of 7/18/2016**
  - Format Code **End of 7/18/2016*8
  - Model all parts of the drone and have available in a folder on the repository (Open Source :D ) **End of 7/19/2016/**
  - Remodel the hull of the Drone (also available) **End of 7/20/16**
  - Assure calculations of the hull and order a 3d-print **End of 7/21/16**
  - Resolder all components into new breadboard **End of 7/21/16**
  - Connect Voltage Regulator and test powering the Raspberry Pi via big battery **7/22/16**
  - Work with accelerometer and gyroscope, create methods to get data from these components **TBD**
  - Add some sort of handler for the math to check with to store world velocity vectors. AKA, a system in order to store gravity, wind resistance, drag, and other forces. **TBD**
  - Put together drone? **TBD**
  - Create simple program for drone to slowy go upwards until speed == 0 **TBD**
