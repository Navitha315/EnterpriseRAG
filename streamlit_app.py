import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="Enterprise AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ------------------------
# Custom CSS
# ------------------------

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.stChatMessage{
    border-radius:15px;
}

.block-container{
    padding-top:2rem;
}

.source-box{
    background:white;
    border-radius:10px;
    padding:10px;
    margin-top:10px;
    border-left:5px solid #2E86DE;
}

.title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#2E86DE;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------

st.markdown("<div class='title'>🤖 Enterprise Knowledge Assistant</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Ask questions about enterprise documents</div>", unsafe_allow_html=True)

# ------------------------

if "messages" not in st.session_state:
    st.session_state.messages=[]

# Display history

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

        if msg["role"]=="assistant" and "sources" in msg:

            st.markdown("### 📄 Source Documents")

            for source in msg["sources"]:

                st.success(source.split("/")[-1])

# ------------------------

question=st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append({
        "role":"user",
        "content":question
    })

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching enterprise knowledge..."):

            try:

                response=requests.post(

                    API_URL,

                    json={
                        "question":question
                    }

                )

                result=response.json()

                answer=result["answer"]

                documents=result["documents"]

                st.write(answer)

                st.markdown("### 📄 Source Documents")

                unique=[]

                for doc in documents:

                    name=doc["source"].split("/")[-1]

                    if name not in unique:

                        unique.append(name)

                for file in unique:

                    st.success(file)

                st.session_state.messages.append({

                    "role":"assistant",

                    "content":answer,

                    "sources":unique

                })

            except Exception as e:

                st.error(str(e))


# ------------------------
# Sidebar
# ------------------------

with st.sidebar:

    st.title("⚙ Enterprise RAG")

    st.markdown("---")

    st.write("### Backend")

    st.success("FastAPI")

    st.write("### Vector DB")

    st.success("ChromaDB")

    st.write("### LLM")

    st.success("Groq")

    st.write("### Automation")

    st.success("n8n")

    st.write("### Source")

    st.success("Google Drive")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages=[]

        st.rerun()
