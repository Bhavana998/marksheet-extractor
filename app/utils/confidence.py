def calculate_confidence(llm_score: float, ocr_score: float):
    return round(0.6 * llm_score + 0.4 * ocr_score, 2)
