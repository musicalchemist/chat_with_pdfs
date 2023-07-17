import streamlit as st
from chatbot import PDFChatBot

def run():
    chatbot = PDFChatBot()

    st.set_page_config(page_title="Chat with your PDFs", page_icon=":books:")

    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "processing_done" not in st.session_state:
        st.session_state.processing_done = False

    st.header("PDF Chat: Upload PDFs and Chat! :books:")

    st.subheader("Upload documents")
    pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
    if st.button("Process"):
        with st.spinner("Processing"):
            raw_text = chatbot.read_pdf(pdf_docs)
            text_partitions = chatbot.partition_text(raw_text, chunk_size=1500, chunk_overlap=250)
            embeddings = chatbot.create_embeddings(type='openai')
            vectorstore = chatbot.create_embedding_vectorstore(text_partitions, embeddings, type='faiss')
            st.session_state.qa_chain = chatbot.generate_qa_chain(vectorstore)
            st.session_state.processing_done = True

    if st.session_state.processing_done:
        user_query = st.text_input("Chat and ask questions about your pdfs:")
        if user_query:
            with st.spinner("Generating response"):
                response = st.session_state.qa_chain({'question': user_query, "chat_history": st.session_state.chat_history})
                st.session_state.chat_history = response['chat_history']
            st.write(f"Bot: {response['answer']}")
    else:
        st.write("Please upload and process documents before chatting.")

if __name__ == '__main__':
    run()
