from deepface import DeepFace

#####see if the face is the same#########
#verification = DeepFace.verify(img1_path = r"C:\Users\nickm\OneDrive\Pictures\Camera Roll\img3.jpg",  
#    img2_path = r"C:\Users\nickm\OneDrive\Pictures\Camera Roll\img5.PNG", enforce_detection=False)
#print(verification)

#######preform an analysis on the face###########
#analysis = DeepFace.analyze(img_path = r"C:\Users\nickm\OneDrive\Pictures\Camera Roll\img5.PNG", actions = ["age", "gender", "emotion", "race"])
#print(analysis)

######see if face is in a collection of faces#########
recognition = DeepFace.find(img_path = r"C:\Users\nickm\OneDrive\Pictures\Camera Roll\img5.PNG", db_path = “C:/Users/nickm/OneDrive/Pictures/Camera Roll/nick-face")
