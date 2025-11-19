import streamlit as st
from main import research_query   # import your existing RAG logic

st.set_page_config(page_title="Local RAG Research Analyst", layout="wide")

st.title("🧠 Local RAG Research Analyst")
st.write("Ask a complex research question and get a fully local answer.")

query = st.text_input("Enter your research question:")

if st.button("Run Research"):
    if not query.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Researching..."):
            answer = research_query(query)
        st.success("Done!")
        st.subheader("📌 Final Answer")
        st.write(answer)
