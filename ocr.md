# Pick 10 - OCR & Name Validation Module
**This is AI generated** #Still gonna do research 
# This will be included on the Regional Expo or Internatonal Science Fair

This module of **Pick 10** is responsible for **digitizing school registers** and **validating learner names** during subject registration. It ensures that learners’ entries match the official school list and links registration with **parental consent** verification.

---

## **Features**

- **OCR Digitization**  
  Upload scanned school registers (PDF/Image) and automatically extract learner names using **Tesseract** or **EasyOCR**.  

- **Error Correction / Fuzzy Matching**  
  Learner-entered names are automatically compared to OCR-extracted names using string similarity algorithms (e.g., **RapidFuzz**).  
  - Handles typos or minor spelling differences.
  - Ensures accurate registration tracking.  

- **Database Integration**  
  - Stores normalized names in a table with fields:  
    - `student_id`, `first_name`, `last_name`, `registered`, `parent_signed`
  - Updates registration status automatically when a match is found.

- **Admin Dashboard**  
  - Displays registration and consent status for all learners.  
  - Allows manual corrections for OCR or input errors.  
  - Exportable reports (CSV/PDF) for record-keeping.

---

## **Workflow**

1. **Upload Register**  
   Admin uploads a scanned class register (PDF/Image).

2. **OCR Processing**  
   - Extract text from the image.  
   - Preprocess: grayscale, thresholding, remove noise.  
   - Extract learner names and normalize formatting.

3. **Error Correction / Matching**  
   - Learners enter their names in the web form.  
   - Fuzzy matching compares input against OCR names.  
   - High-confidence matches update the database.  

4. **Registration & Consent Tracking**  
   - Marks `registered = True` if matched.  
   - Updates `parent_signed = True` if consent form uploaded.  
   - Dashboard reflects real-time status.

---

## **Technology Stack**
- **Python**: Backend processing  
- **OCR Libraries**: Tesseract OCR or EasyOCR  
- **Error Correction**: RapidFuzz (fuzzy string matching)  
- **Database**: MySQL / JSON  

---

## **Example: Python Code Snippet**

```python
from rapidfuzz import process, fuzz
import pytesseract
import cv2

# Load register image
image = cv2.imread("class_register.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

# OCR extract names
ocr_text = pytesseract.image_to_string(thresh)
ocr_names = [line.strip().title() for line in ocr_text.split("\n") if line.strip()]

# Learner input
learner_input = "andil thango"

# Fuzzy match
match, score, _ = process.extractOne(learner_input, ocr_names, scorer=fuzz.ratio)
if score > 85:
    print(f"Matched name: {match}")
else:
    print("Name not found. Please check spelling.")
