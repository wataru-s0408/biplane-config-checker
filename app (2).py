
import streamlit as st

# タイトルと説明
st.title("バイプレーン構成判定ツール")
st.write("フロンタルアームとラテラルアームの角度を選択して、干渉の有無を判定します。")

# スライダーで角度を選択
frontal_angle = st.slider("フロンタルアームの角度 (RAO/LAO)", 0, 360, 0)
frontal_cran_caud = st.slider("フロンタルアームのCRAN/CAUD角度", -90, 90, 0)
lateral_angle = st.slider("ラテラルアームの角度 (RAO)", 0, 360, 0)
lateral_cran_caud = st.slider("ラテラルアームのCRAN/CAUD角度", -90, 90, 0)

# SIDの固定値
frontal_sid = 110
lateral_sid = 115

# 判定ロジック
def check_feasibility(frontal_angle, frontal_cran_caud, lateral_angle, lateral_cran_caud):
    if frontal_angle == 0 and lateral_angle <= 75:
        return "〇", "この構成は可能です。"
    elif frontal_angle == 30 and frontal_cran_caud == 30 and lateral_angle <= 80 and lateral_cran_caud == 30:
        return "〇", "この構成は可能です。"
    elif frontal_angle == 30 and frontal_cran_caud == 30 and lateral_angle <= 60:
        return "〇", "この構成は可能です。"
    elif frontal_angle == 30 and frontal_cran_caud == 30 and lateral_angle <= 45 and lateral_cran_caud == -30:
        return "〇", "この構成は可能です。"
    else:
        return "×", "この構成は干渉の可能性があります。RAO80に変更を検討してください。"

# 判定結果
result, advice = check_feasibility(frontal_angle, frontal_cran_caud, lateral_angle, lateral_cran_caud)

# 結果表示
st.write(f"判定結果: {result}")
st.write(advice)

# 構成図の表示（簡易図）
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([0, frontal_sid], [0, frontal_angle], label="フロンタルアーム", color="blue")
ax.plot([0, lateral_sid], [0, lateral_angle], label="ラテラルアーム", color="red")
ax.legend()
ax.set_xlim(0, 150)
ax.set_ylim(0, 360)
ax.set_xlabel("SID (cm)")
ax.set_ylabel("角度 (°)")
st.pyplot(fig)
