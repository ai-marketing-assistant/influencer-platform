import streamlit as st

# გვერდის საწყისი მდგომარეობა
if "page" not in st.session_state:
  st.session_state.page = "home"

# --- მთავარი გვერდი (ანიმაციური შესავალი) ---
if st.session_state.page == "home":
  st.markdown(
      """
        <style>
        /* Streamlit-ის ძირითადი ფონის მუქ ფერზე შეცვლა */
        .stApp {
            background-color: #0f172a;
        }

        /* ეკრანის ცენტრში მოქცევა */
        .welcome-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 55vh;
            text-align: center;
        }

        /* სახელი collab.ge - მწვანე ფერში, თავიდან უფერული და მერე ნელა შემოდის */
        @keyframes fadeInTitle {
            0% {
                opacity: 0;
                transform: translateY(30px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .app-title {
            animation: fadeInTitle 1.8s ease forwards;
            font-size: 5rem;
            font-weight: 900;
            color: #10b981 !important; /* ლამაზი ზურმუხტისფერი მწვანე */
            letter-spacing: 3px;
            text-shadow: 0 0 20px rgba(16, 185, 129, 0.3); /* მწვანე ბზინვარება */
        }

        /* ღილაკის დიზაინი */
        .stButton button {
            background-color: #10b981 !important;
            color: white !important;
            border-radius: 8px;
            font-weight: 600;
            border: none;
            padding: 12px 24px;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: #059669 !important;
            transform: scale(1.05);
        }
        </style>

        <div class="welcome-container">
            <div class="app-title">collab.ge</div>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # ღილაკი ცენტრში
  col1, col2, col3 = st.columns([1, 1, 1])
  with col2:
    if st.button("დაწყება", use_container_width=True):
      st.session_state.page = "register"
      st.rerun()

# --- რეგისტრაციის გვერდი ---
elif st.session_state.page == "register":
  st.title("რეგისტრაცია")
  st.write("მოგესალმებით collab.ge-ს რეგისტრაციის გვერდზე!")

  username = st.text_input("სახელი / მომხმარებელი")
  email = st.text_input("ელ-ფოსტა")
  password = st.text_input("პაროლი", type="password")

  if st.button("რეგისტრაციის დასრულება"):
    st.success("წარმატებით დარეგისტრირდით!")

  st.write("")
  if st.button("← უკან დაბრუნება"):
    st.session_state.page = "home"
    st.rerun()
