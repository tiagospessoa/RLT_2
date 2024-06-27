"""Sample Webots controller for the square path benchmark."""

from controller import Robot

# Get pointer to the robot.
robot = Robot()

# Get pointer to each wheel of our robot.
leftWheel = robot.getDevice('left wheel')
rightWheel = robot.getDevice('right wheel')
rightWheelSensor = robot.getDevice('right wheel sensor')
rightWheelSensor.enable(16) # Refreshes the sensor every 16ms.

diametro_roda = 0.195
lado_quadrado = 2
#Calculo do angulo a ser percorrido pela roda na linha recta
angulo_linha_recta = 2*lado_quadrado/diametro_roda
#Calculo do angulo a ser percorrido pela roda na viragem
percurso_roda_viragem = (1/2)*3.141592*(0.33/2)
angulo_viragem = (2*percurso_roda_viragem/diametro_roda)
robot.step(48)
leftWheel.setPosition(float('inf'))
rightWheel.setPosition(float('inf'))
# Repeat the following 4 times (once for each side).
for i in range(0, 4):
    valor_inicial_roda_direita = rightWheelSensor.getValue()
    #print("Angulo inicial direita: %f"%valor_inicial_roda_direita)
    # First set both wheels to go forward, so the robot goes straight.
    #leftWheel.setPosition(1000)
    leftWheel.setVelocity(5)
    rightWheel.setVelocity(5)
    #rightWheel.setPosition(1000)
    # Wait for the robot to reach a corner.
    # Malha aberta - temporizador
    #robot.step(3900)
    # Malha fechada - trajetoria em linha recta
    valor_actual_roda_direita = rightWheelSensor.getValue()
    while valor_actual_roda_direita - valor_inicial_roda_direita <= angulo_linha_recta:
        valor_actual_roda_direita = rightWheelSensor.getValue()
        robot.step(16)
    # Virar a direita.
    print('Vou parar')
    
    leftWheel.setVelocity(0)
    rightWheel.setVelocity(0)
    robot.step(96)
    leftWheel.setVelocity(0.5)
    rightWheel.setVelocity(-0.5)
    robot.step(96)
    #leftWheel.setPosition(1000)
    #robot.step(16)
    #rightWheel.setPosition(-1000)
    #robot.step(16)
    valor_actual_roda_direita = rightWheelSensor.getValue()
    valor_inicial = rightWheelSensor.getValue()
    print('Angulo viragem: ' + str(angulo_viragem))
    while valor_inicial-valor_actual_roda_direita < angulo_viragem-0.11:
        valor_actual_roda_direita = rightWheelSensor.getValue()
        #print('Valor atual roda direita: ' + str(valor_actual_roda_direita-valor_inicial))
        #print('Valor atual roda direita: ' + str(valor_actual_roda_direita))
        robot.step(16)
    #robot.step(16)
    # Malha aberta - temporizador para virar a direita
    #robot.step(488)

# Stop the robot when path is completed, as the robot performance
# is only computed when the robot has stopped.
leftWheel.setVelocity(0)
rightWheel.setVelocity(0)