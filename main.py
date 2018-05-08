import face_recognition

# ladujemy zdjecia
images  = []
known_faces = []
for i in range(30):
    images.append(face_recognition.load_image_file("base/"+str(i)+".jpg"))

test_image = face_recognition.load_image_file("unknown/3.jpg")

# odkodowanie jesli wiecej twarzy na zdjeciu zwraca tablice ale przyjmujemy ze tylko jedna twarz i index 0 bierzemy 1
try:
    for i in range(30):
        known_faces.append(face_recognition.face_encodings(images[i])[0])

        test_face = face_recognition.face_encodings(test_image)[0]

except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

# tablica wynikowa true jesli znana false jesli nie
results = face_recognition.compare_faces(known_faces, test_face)

print("Czy osoba znana? {}".format(True in results))

