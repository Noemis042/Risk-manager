import streamlit as st

def calculate_risk(leverage, position_pct):
    score = leverage * 2 + position_pct
    score = min(score, 100)

    if score < 30:
        return score, "🟢 Safe trade"
    elif score < 60:
        return score, "🟠 Medium risk"
    else:
        return score, "🔴 High risk"

st.title("📊 Risk Manager")

pair = st.text_input("Pair (e.g. BTCUSDT)")
leverage = st.number_input("Leverage (x)", min_value=1, step=1)
position = st.number_input("Position size (%)", min_value=1, max_value=100, step=1)

if st.button("Check Risk"):
    score, msg = calculate_risk(leverage, position)
    st.write(f"**{pair} → Risk Score: {score}**")
    st.success(msg)
