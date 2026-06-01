from roboflow import Roboflow

API_KEY = "Due583nQjuqECgFBsQvn"

rf = Roboflow(api_key=API_KEY)

print("Testing validator...")
validator = rf.workspace().project(
    "validasi-kategori-bukan-kategori"
).version(1).model
print("Validator OK")

print("Testing weather...")
weather = rf.workspace().project(
    "prediksi_cuaca"
).version(1).model
print("Weather OK")