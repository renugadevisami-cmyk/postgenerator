import streamlit as st
from groq import Groq  #AI brain

st.set_page_config(page_title="Viral Post Generator", page_icon="🔥",layout='centered')

#API setup

api_key="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"


# exception handling
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"API key error. Please check your API key. Error: {e}")
    

st.title("AI Viral Post Generator 🔥")
st.markdown("-------------")

st.write("Enter a topic and let the AI generate a viral social media post for you!")
topic = st.text_area("What is your post about?", placeholder="Ex: The future of AI in healthcare")

language = st.selectbox ("Select Language", ["English", "Spanish", "French", "German", "Chinese"])

col1,col2,col3 = st.columns([1,2,1])
with col2:
    generate_btn = st.button("Generate Post 🔥", type="primary",use_container_width=True)


if generate_btn:
    if not topic.strip():
        st.warning("Please enter a topic to generate a post.")
    else:
        with st.spinner("AI is thinking..."):
            prompt = f"""Act as an professional social media marketer.
            write an engaging and viral linkedin/instagram post about'{topic}'.
            Strict requirements: Write a post in **{language}**

            Rules:
            1. Start with a catchy hook/headline
            2. Use bullet points
            3. Include relevant emojis
            4. End with a question to audinece
            5. Add 5 trendig hashtags
            """
            
            
            try:
                client_completion_=client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")

                with st.spinner("Generating your viral post..."):
                    st.balloons()

                    ai_response = client_completion_.choices[0].message.content
                    st.success("Post Generated Successfully! 🎉")                          
                    st.markdown(ai_response)
                    st.info("Tip: copy and paste the post to your social media platform to share it with your audience.")
            except Exception as e:
                st.error(f"Error generating post: {e}")