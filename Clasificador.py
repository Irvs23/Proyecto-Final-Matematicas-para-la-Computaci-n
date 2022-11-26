import cv2
#Leemos la Imagen
image = cv2.imread('casa.png')
#Pasamos la imagen la escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Detección de Bordes
canny = cv2.Canny(gray, 10, 150)
#Dilatamos y Erosionamos la Imagen
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
#Encontramos los contornos correspondientes
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#Analizamos cada contorno
for c in cnts:
  #Parámetro que especifica la precisión de aproximación.
  epsilon = 0.01*cv2.arcLength(c,True)
  #Especificamos el contorno, epsilon y true en el parámetro closed ya que todos los vértices iniciales y finales de las figuras están conectados.
  approx = cv2.approxPolyDP(c,epsilon,True)
  print(approx)
  #Obtenemos los puntos x, y el ancho y alto del contorno actual, estos datos nos serán de ayuda cuando estemos tratando de diferenciar entre cuadrado y rectángulo.
  x,y,w,h = cv2.boundingRect(approx)
  if len(approx)==3:
    cv2.putText(image,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
  if len(approx)==4:
    aspect_ratio = float(w)/h
    print('aspect_ratio= ', aspect_ratio)
    if aspect_ratio == 1:
      cv2.putText(image,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
    else:
      cv2.putText(image,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
  if len(approx)==5:
    cv2.putText(image,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
  if len(approx)==6:
    cv2.putText(image,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
  if len(approx)==8:
     cv2.putText(image,'Octagono', (x,y-5),1,1.5,(0,255,0),2)
  if len(approx)>10:
    cv2.putText(image,'Circulo', (x,y-5),1,1.5,(0,255,0),2)
  cv2.drawContours(image, [approx], 0, (0,255,0),2)
  cv2.imshow('image',image)
  cv2.waitKey(0)