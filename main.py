import face_recognition

# ladujemy zdjecia
biden_image = face_recognition.load_image_file("base/1.jpg")
obama_image = face_recognition.load_image_file("base/2.jpg")
unknown_image = face_recognition.load_image_file("1.jpg")

# odkodowanie jesli wiecej twarzy na zdjeciu zwraca tablice ale przyjmujemy ze tylko jedna twarz i index 0 bierzemy 1
try:
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    biden_face_encoding,
    obama_face_encoding
]

# tablica wynikowa true jesli znana false jesli nie
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Czy osoba znana? {}".format(not not True in results))