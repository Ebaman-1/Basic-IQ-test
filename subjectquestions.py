import streamlit as st

# ------------------------------
# QUIZ DATA
# ------------------------------
quiz_data = {
    "Mathematics": [
        {"question": "What is 12 × 8?", "options": ["96", "108", "86", "100"], "answer": "96"},
        {"question": "What is the square root of 81?", "options": ["7", "8", "9", "10"], "answer": "9"},
        {"question": "Solve: 15 + 27", "options": ["42", "40", "45", "41"], "answer": "42"},
        {"question": "What is 100 ÷ 5?", "options": ["10", "15", "20", "25"], "answer": "20"},
        {"question": "What is 7²?", "options": ["42", "47", "49", "56"], "answer": "49"},
        {"question": "What is 45 – 18?", "options": ["37", "28", "27", "33"], "answer": "27"},
        {"question": "Simplify: 5 × (6 + 4)", "options": ["50", "60", "70", "40"], "answer": "50"},
        {"question": "What is 3³?", "options": ["6", "9", "27", "81"], "answer": "27"},
        {"question": "Find: 2/5 of 100", "options": ["20", "25", "30", "40"], "answer": "40"},
        {"question": "What is 11 × 11?", "options": ["111", "120", "121", "123"], "answer": "121"},
    ],
    "English": [
        {"question": "What is the plural of 'child'?", "options": ["childs", "children", "childrens", "childer"], "answer": "children"},
        {"question": "Which is a noun?", "options": ["Run", "Happy", "Table", "Quickly"], "answer": "Table"},
        {"question": "Which of these is an adjective?", "options": ["Slowly", "Blue", "Dance", "Sing"], "answer": "Blue"},
        {"question": "Choose the correct spelling:", "options": ["Enviroment", "Environment", "Environmment", "Envirnment"], "answer": "Environment"},
        {"question": "What is the opposite of 'hot'?", "options": ["Cold", "Cool", "Warm", "Freeze"], "answer": "Cold"},
        {"question": "Which is a verb?", "options": ["Jump", "Table", "Blue", "Fast"], "answer": "Jump"},
        {"question": "Choose the synonym of 'happy':", "options": ["Sad", "Angry", "Joyful", "Cry"], "answer": "Joyful"},
        {"question": "What is the past tense of 'go'?", "options": ["Goes", "Gone", "Went", "Going"], "answer": "Went"},
        {"question": "Which is a pronoun?", "options": ["Car", "He", "Beautiful", "Play"], "answer": "He"},
        {"question": "Complete: The boy ___ playing.", "options": ["is", "are", "am", "be"], "answer": "is"},
    ],
    "Civic Education": [
        {"question": "What is democracy?", "options": ["Rule by kings", "Rule by military", "Government by the people", "Rule by the rich"], "answer": "Government by the people"},
        {"question": "Which of these is a civic right?", "options": ["Voting", "Stealing", "Cheating", "Disobedience"], "answer": "Voting"},
        {"question": "Which body makes laws?", "options": ["Executive", "Judiciary", "Legislature", "Police"], "answer": "Legislature"},
        {"question": "Who is a citizen?", "options": ["A person living in a country", "A visitor", "An illegal migrant", "A refugee"], "answer": "A person living in a country"},
        {"question": "What is the duty of the police?", "options": ["Make laws", "Punish criminals", "Maintain law and order", "Rule the country"], "answer": "Maintain law and order"},
        {"question": "Which symbol represents justice?", "options": ["Lion", "Scales", "Eagle", "Sword"], "answer": "Scales"},
        {"question": "What is the highest law in Nigeria?", "options": ["Court ruling", "Presidential order", "Constitution", "Act of parliament"], "answer": "Constitution"},
        {"question": "Who heads the judiciary?", "options": ["President", "Governor", "Chief Justice", "Senate President"], "answer": "Chief Justice"},
        {"question": "What does INEC stand for?", "options": ["Independent National Electoral Commission", "Internal National Education Council", "International Election Committee", "Independent National Examination Council"], "answer": "Independent National Electoral Commission"},
        {"question": "What is the age of voting in Nigeria?", "options": ["16", "17", "18", "21"], "answer": "18"},
    ],
    "Religious Studies": [
        {"question": "Who led the Israelites out of Egypt?", "options": ["Moses", "Abraham", "David", "Joseph"], "answer": "Moses"},
        {"question": "Who was the mother of Jesus?", "options": ["Sarah", "Elizabeth", "Mary", "Hannah"], "answer": "Mary"},
        {"question": "In Islam, who is the last prophet?", "options": ["Moses", "Jesus", "Muhammad", "Ibrahim"], "answer": "Muhammad"},
        {"question": "How many disciples did Jesus have?", "options": ["10", "12", "11", "13"], "answer": "12"},
        {"question": "What is the holy book of Christians?", "options": ["Torah", "Bible", "Quran", "Hadith"], "answer": "Bible"},
        {"question": "What is the holy book of Muslims?", "options": ["Torah", "Bible", "Quran", "Psalms"], "answer": "Quran"},
        {"question": "Who killed Goliath?", "options": ["Moses", "Samson", "David", "Solomon"], "answer": "David"},
        {"question": "Where was Prophet Muhammad born?", "options": ["Jerusalem", "Mecca", "Medina", "Baghdad"], "answer": "Mecca"},
        {"question": "Who built the ark?", "options": ["Abraham", "Noah", "Jacob", "Joseph"], "answer": "Noah"},
        {"question": "What day do Muslims gather for Jummah prayers?", "options": ["Friday", "Saturday", "Sunday", "Monday"], "answer": "Friday"},
    ],
}

# ------------------------------
# STREAMLIT APP
# ------------------------------
st.title("📚 Interactive Quiz App")

# Subject selection
subject = st.selectbox("Choose a subject:", list(quiz_data.keys()))

if subject:
    st.subheader(f"📝 {subject} Quiz")
    score = 0
    skipped = 0
    wrong = 0

    # Display questions
    for i, q in enumerate(quiz_data[subject]):
        options = ["Select an answer"] + q["options"]
        user_answer = st.radio(
            f"Q{i+1}: {q['question']}",
            options,
            index=0,  # default is "Select an answer"
            key=f"{subject}_{i}"
        )

        if user_answer == "Select an answer":
            skipped += 1
        elif user_answer == q["answer"]:
            score += 1
        else:
            wrong += 1

    # Submit button
    if st.button(f"Submit {subject} Quiz"):
        st.success(f"✅ You scored {score} out of 10 in {subject}!")
        st.info(f"❌ Wrong answers: {wrong}")
        st.warning(f"➖ Skipped questions: {skipped}")
