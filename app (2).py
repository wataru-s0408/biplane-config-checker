
import streamlit as st

def check_feasibility(frontal_angle, frontal_cran_caud, lateral_angle, lateral_cran_caud):
    # Define the feasible ranges for angles
    frontal_rao_range = range(0, 186)
    frontal_lao_range = range(0, 121)
    lateral_rao_range = range(27, 116)
    
    # Check if the angles are within the feasible ranges
    if frontal_angle.startswith("RAO"):
        frontal_angle_value = int(frontal_angle.split()[1])
        if frontal_angle_value not in frontal_rao_range:
            return "×", "フロンタルアームのRAO角度が範囲外です。"
    elif frontal_angle.startswith("LAO"):
        frontal_angle_value = int(frontal_angle.split()[1])
        if frontal_angle_value not in frontal_lao_range:
            return "×", "フロンタルアームのLAO角度が範囲外です。"
    else:
        return "×", "フロンタルアームの角度指定が不正です。"

    if lateral_angle.startswith("RAO"):
        lateral_angle_value = int(lateral_angle.split()[1])
        if lateral_angle_value not in lateral_rao_range:
            return "×", "ラテラルアームのRAO角度が範囲外です。"
    else:
        return "×", "ラテラルアームはRAO角度のみ指定可能です。"

    # Check for interference based on angle difference
    angle_difference = abs(frontal_angle_value - lateral_angle_value)
    if angle_difference < 75:
        return "×", "この構成は干渉の可能性があります。RAO80に変更を検討してください。"
    
    return "〇", "この構成は可能です。"

# Streamlit app layout
st.title("バイプレーン構成判定ツール")

st.sidebar.header("フロンタルアームの設定")
frontal_angle = st.sidebar.selectbox("RAO/LAO角度", ["RAO 0", "RAO 30", "RAO 60", "RAO 90", "RAO 120", "RAO 150", "RAO 180", "LAO 0", "LAO 30", "LAO 60", "LAO 90", "LAO 120"])
frontal_cran_caud = st.sidebar.selectbox("CRAN/CAUD角度", ["CRAN 0", "CRAN 15", "CRAN 30", "CAUD 0", "CAUD 15", "CAUD 30"])

st.sidebar.header("ラテラルアームの設定")
lateral_angle = st.sidebar.selectbox("RAO角度", ["RAO 27", "RAO 45", "RAO 60", "RAO 75", "RAO 90", "RAO 115"])
lateral_cran_caud = st.sidebar.selectbox("CRAN/CAUD角度", ["CRAN 0", "CRAN 15", "CRAN 30", "CAUD 0", "CAUD 15", "CAUD 30"])

if st.sidebar.button("判定"):
    result, advice = check_feasibility(frontal_angle, frontal_cran_caud, lateral_angle, lateral_cran_caud)
    st.write(f"判定結果: {result}")
    st.write(f"アドバイス: {advice}")
