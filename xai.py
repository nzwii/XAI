import streamlit as st

tweet = [
    "旅行に行ったら、土産にインフルもらってきた。",
    "インフル感染の危機。"
]
n = len(tweet)
tweet_and_drop = {
    "旅行に行ったら、土産にインフルもらってきた。":["土産に", "インフル"],
    "インフル感染の危機。":["インフル", "危機。"]
}

with st.form("input_form", clear_on_submit=False):
    series = st.selectbox(label='ツイートを選択してください', options=[tweet[i] for i in range(n)])
    submitted = st.form_submit_button("学習結果を表示") 
     
if submitted:
    st.write(tweet_and_drop[series])