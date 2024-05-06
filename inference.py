import pyttsx3
from keras.models import load_model 


def inFrame(lst):
	if lst[28].visibility > 0.6 and lst[27].visibility > 0.6 and lst[15].visibility>0.6 and lst[16].visibility>0.6:
		return True 
	return False

model  = load_model("C:\\Users\\user\\OneDrive\\Desktop\\Setup\\yoga-main\\yoga-main\\model.h5")

import cv2
import numpy as np
import mediapipe as mp
label = np.load("C:\\Users\\user\\OneDrive\\Desktop\\Setup\\yoga-main\\yoga-main\\labels.npy")

startingpose="standing side bend"


holistic = mp.solutions.pose
holis = holistic.Pose()
drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


while True:
	lst = []

	_, frm = cap.read()

	window = np.zeros((940,940,3), dtype="uint8")

	frm = cv2.flip(frm, 1)

	res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

	frm = cv2.blur(frm, (4,4))
	if res.pose_landmarks and inFrame(res.pose_landmarks.landmark):
		for i in res.pose_landmarks.landmark:
			lst.append(i.x - res.pose_landmarks.landmark[0].x)
			lst.append(i.y - res.pose_landmarks.landmark[0].y)

		lst = np.array(lst).reshape(1,-1)

		p = model.predict(lst)
		pred = label[np.argmax(p)]



		if p[0][np.argmax(p)] > 0.75:
			print(p[0][np.argmax(p)],"score")
			print(pred,"result",startingpose)
			cv2.putText(window, pred , (120,120),cv2.FONT_ITALIC, 0.2, (0,250,0),2)


			# engine = pyttsx3.init()
			# engine.setProperty('rate', 145)
			# engine.say("Detected pose is" + pred)
			# engine.runAndWait()

			if startingpose != str(pred):
				engine = pyttsx3.init()
				engine.setProperty('rate', 145)
				engine.say("Your pose  is wrong")
				engine.runAndWait()

				if startingpose == "standing side bend":



					im = cv2.imread("C:\\Users\\user\\OneDrive\\Desktop\\Setup\\yoga-main\\yoga-main\\images\\standingsidebend.jpg")
					cv2.imshow("window", im)
					cv2.waitKey(3000)

					engine = pyttsx3.init()
					engine.setProperty('rate', 145)
					engine.say(""""Start by standing with your feet a comfortable distance apart and your hands at your sides, palms facing your thighs. 

Slowly bend to one side, sliding your arm down your leg toward your knee, so your shoulder leans down and to the side. 

Your other hand will naturally slide up your leg toward your hip as you bend.

Hold the stretch and focus on taking deep breaths in and out. 

Return to the starting position.  

Repeat the stretch, bending to the opposite side. 

As you do each rep, you might feel a stretch in your low back, hips, and the sides of your body.""")
					engine.runAndWait()


				elif startingpose == "tadasana":

					im = cv2.imread("C:\\Users\\user\\OneDrive\\Desktop\\Setup\\yoga-main\\yoga-main\\images\\tadasana.jpg")
					cv2.imshow("window", im)
					cv2.waitKey(3000)

					engine = pyttsx3.init()
					engine.setProperty('rate', 145)
					engine.say(""""Stand upright, keeping a distance of 2 inches between your feet
Inhale and lift your arms in front, levelling up to your shoulders
Lock the fingers of both hands together and then slowly rotate your wrist outwards
Now inhale and lift your hands above the head
While lifting your arms, also lift your heels off the ground, balancing your entire body weight on your toes
Be in this position for 20 - 30 seconds or as long as you are comfortable
Now slowly bring your heels down
Exhale and release your fingers
Now draw your arms down and return to the initial position.""")
					engine.runAndWait()




				elif startingpose == "Warrior_2":

					im = cv2.imread("C:\\Users\\user\\OneDrive\\Desktop\\Setup\\yoga-main\\yoga-main\\images\\warrior2.jpg")
					cv2.imshow("window", im)
					cv2.waitKey(3000)
					engine = pyttsx3.init()
					engine.setProperty('rate', 145)
					engine.say(""""Face the long side of your mat with your arms stretched straight out from your shoulders and your feet parallel to each other in a wide stance. You want your ankles approximately beneath your wrists.
Turn your right foot and knee to face the front of the mat.
Angle your left toes slightly in toward the upper left corner of the mat.
Bend your right knee and stack it over your right ankle.
Distribute your weight evenly between both legs. Press down through the outer edge of your back foot.
Keep the crown of your head stacked over your pelvis and your shoulders over your hips.
Reach strongly through both arms toward the front and back of the mat and turn your head to look past your right fingertips.
Stay here for 5–10 breaths.
To come out of the pose, exhale as you press down through your feet, then inhale and straighten your legs. Return your feet to parallel facing the left long side of the mat.
Repeat on the other side.""")
					engine.runAndWait()



			else:

				engine = pyttsx3.init()
				engine.setProperty('rate', 145)
				engine.say("Your pose  is ok")
				engine.runAndWait()

				if startingpose== "standing side bend":

					startingpose="tadasana"

					im = cv2.imread("C:\\Users\\user\\OneDrive\\Desktop\\Setup\\yoga-main\\yoga-main\\images\\tadasana.jpg")
					cv2.imshow("window", im)
					cv2.waitKey(3000)

				elif startingpose=="tadasana":

					startingpose="Warrior_2"
					im = cv2.imread("C:\\Users\\user\\OneDrive\\Desktop\\Setup\\yoga-main\\yoga-main\\images\\warrior2.jpg")
					cv2.imshow("window", im)
					cv2.waitKey(3000)


				elif startingpose=="Warrior_2":

					im = cv2.imread("C:\\Users\\user\\OneDrive\\Desktop\\Setup\\yoga-main\\yoga-main\\images\\warrior2.jpg")
					cv2.imshow("window", im)
					cv2.waitKey(3000)


					startingpose="standing side bend"
				print('ttt')


				engine = pyttsx3.init()
				engine.setProperty('rate', 145)
				engine.say("try this pose "+ startingpose)
				engine.runAndWait()



		else:
			print(pred, "result")
			cv2.putText(window, pred, (180, 180), cv2.FONT_ITALIC, 1.3, (0, 255, 0), 2)




			cv2.putText(window, "Asana is either wrong not trained" , (100,180),cv2.FONT_ITALIC, 1.8, (0,0,255),3)

	else: 
		cv2.putText(frm, "pose: "+startingpose+"  \n Make Sure Full body visible", (100,450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)

		
	drawing.draw_landmarks(frm, res.pose_landmarks, holistic.POSE_CONNECTIONS,
							connection_drawing_spec=drawing.DrawingSpec(color=(255,255,255), thickness=6 ),
							 landmark_drawing_spec=drawing.DrawingSpec(color=(0,0,255), circle_radius=3, thickness=3))


	# window[120:700, 170:810, :] = cv2.resize(frm, (640, 480))

	cv2.imshow("window", frm)

	if cv2.waitKey(1) == 27:
		cv2.destroyAllWindows()
		cap.release()
		break

