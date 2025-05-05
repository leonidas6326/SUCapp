# Function to calculate total points
def calculate_points(age, sex, tumor_size, seer_stage, cystectomy, chemotherapy):
    points = 0
    
    # Age points
    if age < 60:
        points += 0
    elif 60 <= age <= 69:
        points += 7
    elif 70 <= age <= 79:
        points += 28
    else:  # age >= 80
        points += 58

    # Sex points
    if sex == "Male":
        points += 0
    else:  # Female
        points += 22
    
    # Tumor size points
    if tumor_size == "Unknown":
        points += 15  # Points for "Unknown"
    elif tumor_size == "<5cm":
        points += 0
    elif tumor_size == "5-9.9cm":
        points += 40
    elif tumor_size == "≥10cm":
        points += 85

    # SEER stage points
    if seer_stage == "Localized":
        points += 0
    elif seer_stage == "Regional":
        points += 86
    elif seer_stage == "Distant":
        points += 100

    # Radical cystectomy points
    if cystectomy == "Done":
        points += 0
    else:  # Not done
        points += 76

    # Chemotherapy points
    if chemotherapy == "Done":
        points += 0
    else:  # Not done
        points += 27
    
    return points

# Function to calculate survival probability (adjust according to your nomogram's conversion)
def calculate_survival_probability(points):
    # Assuming a linear conversion, adjust according to your real mapping (or curve)
    if points < 100:
        survival_probability = 0.50  # Example value for low risk
    elif points < 150:
        survival_probability = 0.37  # Intermediate
    elif points < 200:
        survival_probability = 0.15  # High risk
    else:
        survival_probability = 0.03  # Very high risk
    return survival_probability

# Streamlit user interface
st.title("5-Year Overall Survival Risk Calculator For Patients with Sarcomatoid Urothelial Carcinoma")

# User inputs
age = st.selectbox("Age", [i for i in range(18, 101)])
sex = st.radio("Sex", ["Male", "Female"])

# Update the Tumor size selectbox to include "Unknown"
tumor_size = st.selectbox("Tumor size", ["Unknown", "<5cm", "5-9.9cm", "≥10cm"])

seer_stage = st.selectbox("SEER Stage", ["Localized", "Regional", "Distant"])
cystectomy = st.selectbox("Radical Cystectomy", ["Done", "Not done"])
chemotherapy = st.selectbox("Chemotherapy", ["Done", "Not done"])

# Calculate points and survival probability
points = calculate_points(age, sex, tumor_size, seer_stage, cystectomy, chemotherapy)
survival_probability = calculate_survival_probability(points)

# Display results
st.write(f"Total Risk Points: {points}")
st.write(f"Estimated 5-Year Survival Probability: {survival_probability * 100:.2f}%")

