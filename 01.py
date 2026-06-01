from roboflow import Roboflow

API_KEY = "Due583nQjuqECgFBsQvn"

rf = Roboflow(api_key=API_KEY)

print("Loading workspace...")
print("Loading project...")

model = (
    rf.workspace()
      .project("prediksi_cuaca")
      .version(1)
      .model
)

# GANTI DENGAN FOTO YANG BENAR-BENAR ADA
IMAGE_PATH = r"C:\Users\USER\Documents\water-fashion\mona.jpeg"

try:

    print("\n===== START PREDICT =====")

    result = model.predict(
        IMAGE_PATH
    )

    print("\n===== RAW RESULT =====")
    print(result)

    result_json = result.json()

    print("\n===== JSON RESULT =====")
    print(result_json)

except Exception as e:

    import traceback

    print("\n===== ERROR =====")
    print("TYPE:", type(e).__name__)
    print("MESSAGE:", str(e))
    traceback.print_exc()