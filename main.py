from configuration.config_handler import ConfigHandler
from drone_math.parametric_vector_handler import ParametricVectorHandler
config = ConfigHandler('config.ini', 'Config')
version = config.getData('version')

print('Drone ' + version)
print('-------------')

mathConfig = ConfigHandler('math_equations.ini', None)

while(True):
    mathSection = raw_input("Please enter the section the drone will be using: ")
    
    if not (mathConfig.hasSection(mathSection)):
        print('\nThe math configuration does not have that section!')
        raw_input('Please double check spelling and hit enter when ready\n\n')
        mathConfig.reload()
    else:
        print('drone_math Section that will be used is: ' + mathSection)
        mathConfig.setSection(mathSection)
        break

equationVectorHandler = ParametricVectorHandler(mathConfig)