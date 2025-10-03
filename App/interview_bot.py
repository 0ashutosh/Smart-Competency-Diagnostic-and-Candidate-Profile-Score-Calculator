def run_interview():
    st.title("AI Interview Bot 🤖")

    # Select a domain
    domains = qa_df['domain'].unique()
    selected_domain = st.selectbox("Choose your domain:", domains)

    # Filter questions from that domain
    domain_questions = qa_df[qa_df['domain'] == selected_domain].reset_index(drop=True)

    # Session state to keep track of current question
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
        st.session_state.score = 0

    if st.session_state.q_index < len(domain_questions):
        q_row = domain_questions.iloc[st.session_state.q_index]
        st.subheader(f"Question {st.session_state.q_index+1}: {q_row['question']}")

        user_answer = st.text_area("Your Answer:", key=f"answer_{st.session_state.q_index}")

        if st.button("Submit Answer"):
            correct_answer = q_row['answer']

            st.write("Expected Answer:", correct_answer)

            # Simple keyword-based scoring
            score = 0
            for word in correct_answer.lower().split():
                if word in user_answer.lower():
                    score += 1
            st.success(f"Your Score for this question: {score}")

            # Update total score
            st.session_state.score += score
            st.session_state.q_index += 1
            st.experimental_set_query_params()  # refresh UI
    else:
        st.success("Interview Finished ✅")
        st.write(f"Your Total Score: {st.session_state.score}")
