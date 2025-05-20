import streamlit as st 
from web_functions import predict

def app(df, x, y):
    st.title("Halaman Prediksi")

    col1, col2, col3 = st.columns(3)

    with col1:
        bp = st.text_input('Input Nilai tekanan darah')
        sg = st.text_input('Input Nilai gravitasi spesifik')
        al = st.text_input('Input Nilai protein dalam urine')
        su = st.text_input('Input Nilai gula')
        rbc = st.text_input('Input Nilai seldarah merah')
        pc = st.text_input('Input Nilai sel nanah')
        pcc = st.text_input('Input Nilai gumpalan sel darah')
        ba = st.text_input('Input Nilai bakteri')

    with col2:
        bgr = st.text_input('Input Nilai glukosa darah acak')
        bu = st.text_input('Input Nilai urea darah')
        sc = st.text_input('Input Nilai serum kreatinin')
        sod = st.text_input('Input Nilai natrium')
        pot = st.text_input('Input Nilai kalium')
        hemo = st.text_input('Input Nilai hemoglobin')
        pcv = st.text_input('Input Nilai vol sel darah terkemas')
        wc = st.text_input('Input Nilai jumlah sel darah putih')

    with col3:
        rc = st.text_input('Input Nilai jumlah sel darah merah')
        htn = st.text_input('Input Nilai hipertensi')
        dm = st.text_input('Input Nilai diabetes militus')
        cad = st.text_input('Input Nilai penyakit arteri koroner')
        appet = st.text_input('Input nilai Nafsu makan')
        pe = st.text_input('Input Nilai edema pada kaki (bengkak kaki)')
        ane = st.text_input('Input Nilai anemia')

    features = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]

    if st.button("Prediksi"):
        prediction, score = predict(x, y, features)
        st.info("Prediksi berhasil dilakukan.")

        if prediction == 1:
            st.warning("Orang tersebut TERKENA penyakit ginjal.")
        else:
            st.success("Orang tersebut TIDAK terkena penyakit ginjal.")

        st.info(f"Model yang digunakan memiliki akurasi: {score * 100:.2f}%")
