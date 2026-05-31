import streamlit as st
from api.clients import generate_reply

st.title("Customer Support Reply Generator")

customer_message = st.text_area(
    "Enter Customer Message",
    height=150
)

if st.button("Generate Reply"):

    if customer_message:

        try:

            result = generate_reply(customer_message)

            if result["status"] == "success":

                st.success("Reply Generated Successfully")

                st.subheader("Customer Message")
                st.write(result["customer_message"])

                st.subheader("AI Reply")
                st.write(result["generated_reply"])

                st.subheader("Sentiment")
                st.info(result["sentiment"])

                st.subheader("Technique Used")
                st.write(result["technique_used"])

            else:
                st.error(result["message"])

        except Exception as e:
            st.error(str(e))