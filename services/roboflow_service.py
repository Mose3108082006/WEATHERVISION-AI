from roboflow import Roboflow
import tempfile

API_KEY = "Ld8FDyojU2B4NsmFZyjr"

rf = Roboflow(api_key=API_KEY)

validator_model = rf.workspace().project("there").version(1).model
weather_model = rf.workspace().project("prediksi_cuaca").version(1).model


def save_temp(image):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    temp.write(image.read())
    temp.close()
    return temp.name


def safe_get_label(pred):
    """
    AMAN: ambil label walau struktur Roboflow beda-beda
    """
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
        # VALIDATOR
        # =========================
        validator_result = validator_model.predict(image_path).json()
        validator_preds = validator_result.get("predictions", [])

        if not validator_preds:
            return {"valid": False, "reason": "no_detection", "weather": None, "confidence": 0}

        best = validator_preds[0]

        label = safe_get_label(best).lower().strip()
        confidence = round(best.get("confidence", 0) * 100, 2)

        print("VALIDATOR:", label, confidence)

        # =========================
        # FILTER
        # =========================
        if "bukan" in label:
            return {
                "valid": False,
                "reason": "not_category",
                "weather": None,
                "confidence": confidence
            }

        # =========================
        # WEATHER MODEL
        # =========================
        weather_result = weather_model.predict(image_path).json()
        weather_preds = weather_result.get("predictions", [])

        if not weather_preds:
            return {"valid": False, "reason": "no_weather", "weather": None, "confidence": 0}

        best_weather = weather_preds[0]

        weather_label = safe_get_label(best_weather)

        return {
            "valid": True,
            "reason": "success",
            "weather": weather_label,
            "confidence": round(best_weather.get("confidence", 0) * 100, 2)
        }

    except Exception as e:
        print("❌ FULL ERROR:", str(e))

        return {
            "valid": False,
            "reason": str(e),
            "weather": None,
            "confidence": 0
        }