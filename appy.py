import streamlit as st

# გვერდის საწყისი მდგომარეობა
if "page" not in st.session_state:
  st.session_state.page = "home"

# --- მთავარი გვერდი (მსგავსი დიზაინი სურათიდან) ---
if st.session_state.page == "home":
  st.markdown(
      """
        <style>
        /* სურათის სტილის მუქი მწვანე ფონი */
        .stApp {
            background-color: #2b382f;
        }

        /* ეკრანის ცენტრში მოქცევა */
        .moya-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 60vh;
            text-align: center;
        }

        /* ანიმაცია: სახელის და ქვედა წარწერის ნელა შემოსვლა (Fade In) */
        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .app-title {
            animation: fadeIn 1.8s ease forwards;
            font-size: 3.8rem;
            font-weight: 300;
            letter-spacing: 6px;
            color: #e2e8f0;
            margin-bottom: 10px;
        }

        .app-subtitle {
            animation: fadeIn 1.8s ease 0.4s forwards;
            opacity: 0;
            font-size: 0.9rem;
            letter-spacing: 3px;
            color: #94a3b8;
            text-transform: uppercase;
            margin-bottom: 40px;
        }

        /* ღილაკის დიზაინი (სურათის სტილში) */
        .stButton button {
            background-color: transparent !important;
            color: #e2e8f0 !important;
            border: 1px solid rgba(226, 232, 240, 0.4) !important;
            border-radius: 4px;
            font-weight: 400;
            letter-spacing: 2px;
            padding: 10px 0px;
            width: 100%;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: rgba(226, 232, 240, 0.1) !important;
            border-color: #e2e8f0 !important;
        }
        </style>

        <div class="moya-container">
            <div class="app-title">COLLAB.GE</div>
            <div class="app-subtitle">MINDFUL MOMENTS & IDEAS</div>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # ღილაკი ცენტრში (ზუსტად როგორც სურათზეა ბოლოში)
  col1, col2, col3 = st.columns([1.5, 2, 1.5])
  with col2:
    if st.button("დაწყება"):
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
