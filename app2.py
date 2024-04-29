import streamlit as st

# Rumus perhitungan BMI
def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return ("Underweight", ...)
    elif 18.5 <= bmi < 25:
        return ("Normal", ...)
    elif 25 <= bmi < 30:
        return ("Overweight", ...)
    else:
        return ("Obese", ...)

def display_bmi_info(bmi):
    category, advice, color, exercises, motivation = interpret_bmi(bmi)
    st.success(f'BMI Anda adalah {bmi:.2f}.')
    st.metric(label="Kategori", value=category, delta_color="off", help=advice)
    st.caption(advice)
    st.markdown("**Saran Olahraga:**")
    exercise_table = { "Aktivitas": [], "Manfaat": [] }
    for exercise, benefit in exercises:
        exercise_table["Aktivitas"].append(exercise)
        exercise_table["Manfaat"].append(benefit)
    st.table(exercise_table)
    st.markdown("**Motivasi:**")
    st.markdown(motivation)

def main():
    st.header('Interactive BMI Calculator')
    st.markdown("<hr style='border: 2px solid blue; border-radius: 5px;'/>", unsafe_allow_html=True)

    with st.sidebar:
        name = st.text_input("Masukkan nama Anda:")
        gender = st.selectbox("Pilih jenis kelamin Anda:", ["Pria", "Wanita"])
        weight = st.number_input("Masukkan berat Anda (dalam kg):", min_value=1.0, format="%.2f")
        height = st.number_input("Masukkan tinggi Anda (dalam cm):", min_value=1.0, format="%.2f")
    
    if st.sidebar.button('Hitung BMI'):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            display_bmi_info(bmi)
        else:
            st.error("Mohon masukkan data yang valid!")

if __name__ == '__main__':
    main()
