from roboflow import Roboflow
import tempfile

API_KEY = "Due583nQjuqECgFBsQvn"

rf = Roboflow(api_key=API_KEY)

# Model validator
validator_model = rf.workspace().project("validasi-kategori-bukan-kategori").version(1).model

# Model prediksi cuaca
weather_model = rf.workspace().project("prediksi_cuaca").version(1).model


def save_temp(image):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    temp.write(image.read())
    temp.close()
    return temp.name


def safe_get_label(pred):
    return (
        pred.get("class")
        or pred.get("prediction")
        or pred.get("top")
        or "unknown"
    )


def predict_weather(image):
    try:

        image_path = save_temp(image)

        # =========================
        # VALIDATOR MODEL
        # =========================
        validator_result = validator_model.predict(image_path).json()

        print("\n===== VALIDATOR RESULT =====")
        print(validator_result)

        validator_preds = validator_result.get("predictions", [])

        if not validator_preds:
            return {
                "valid": False,
                "reason": "no_detection",
                "weather": None,
                "confidence": 0
            }

        # Ambil prediksi dengan confidence tertinggi
        best_validator = max(
            validator_preds,
            key=lambda x: x.get("confidence", 0)
        )

        label = safe_get_label(best_validator).lower().strip()
        confidence = round(
            best_validator.get("confidence", 0) * 100,
            2
        )

        print(f"VALIDATOR LABEL: {label}")
        print(f"VALIDATOR CONFIDENCE: {confidence}%")

        # =========================
        # CEK KATEGORI
        # =========================

        # Jika bukan kategori -> tolak
        if label == "bukan kategori":
            return {
                "valid": False,
                "reason": "not_category",
                "weather": None,
                "confidence": confidence
            }

        # Jika label tidak dikenal -> tolak
        if label != "kategori":
            return {
                "valid": False,
                "reason": "unknown_class",
                "weather": None,
                "confidence": confidence
            }

        # =========================
        # PREDIKSI CUACA
        # =========================
        weather_result = weather_model.predict(image_path).json()

        print("\n===== WEATHER RESULT =====")
        print(weather_result)

        weather_preds = weather_result.get("predictions", [])

        if not weather_preds:
            return {
                "valid": False,
                "reason": "no_weather_prediction",
                "weather": None,
                "confidence": 0
            }

        best_weather = max(
            weather_preds,
            key=lambda x: x.get("confidence", 0)
        )

        weather_label = safe_get_label(best_weather)
        weather_confidence = round(
            best_weather.get("confidence", 0) * 100,
            2
        )

        return {
            "valid": True,
            "reason": "success",
            "weather": weather_label,
            "confidence": weather_confidence
        }

    except Exception as e:

        print("❌ ERROR:", str(e))

        return {
            "valid": False,
            "reason": str(e),
            "weather": None,
            "confidence": 0
        }