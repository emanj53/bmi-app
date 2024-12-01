# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:35:03 2024

@author: eman
"""

import streamlit as st

def main():
    st.title("🚴‍♂️ تطبيق حساب مؤشر كتلة الجسم (BMI) 🚴‍♂️")
    الطول = st.number_input("أدخل طولك بالمتر (مثال: 1.75)", min_value=0.5, max_value=2.5, step=0.01)
    الوزن = st.number_input("أدخل وزنك بالكيلوجرام (مثال: 70)", min_value=10.0, max_value=300.0, step=0.1)
    
    if st.button("احسب BMI"):
        if الطول > 0:
            bmi = الوزن / (الطول ** 2)
            st.write(f"🔢 مؤشر كتلة جسمك هو: {bmi:.2f}")
            
            if bmi < 18.5:
                st.warning("📉 وزنك أقل من الطبيعي. حاول زيادة وزنك بشكل صحي!")
            elif 18.5 <= bmi < 24.9:
                st.success("✅ وزنك طبيعي. استمر في نمط حياتك الصحي!")
            elif 25 <= bmi < 29.9:
                st.warning("⚠️ وزنك زائد قليلاً. حاول تحسين نظامك الغذائي.")
            else:
                st.error("🚨 لديك سمنة. يُفضل مراجعة أخصائي تغذية.")
        else:
            st.error("يرجى إدخال الطول والوزن بشكل صحيح.")
            
if __name__ == "__main__":
    main()
