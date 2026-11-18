import streamlit as st

# გვერდის საწყისი მდგომარეობის შექმნა
if "page" not in st.session_state:
  st.session_state.page = "home"

# --- მთავარი გვერდი (ანიმაციური შესავალი) ---
if st.session_state.page == "home":
  st.markdown(
      """
        <style>
        /* სმაილების და ზედმეტი ელემენტების დამალვა, სუფთა დიზაინი */
        .stButton button {
            background-color: #3b82f6;
            color: white;
            border-radius: 8px;
            font-weight: 600;
            border: none;
            padding: 10px 24px;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: #2563eb;
            transform: scale(1.05);
        }

        /* ანიმაცია: ჯერ სახელი შემოდის */
        @keyframes fadeInTitle {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* ანიმაცია: მერე ღილაკი (გვიან იწყება) */
        @keyframes fadeInButton {
            0% { opacity: 0; transform: translateY(20px); }
            50% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .main-title {
            animation: fadeInTitle 1.5s ease forwards;
            font-size: 4rem;
            font-weight: 800;
            text-align: center;
            color: #ffffff;
            margin-top: 100px;
            letter-spacing: 2px;
        }

        .delayed-button-container {
            animation: fadeInButton 2.2s ease forwards;
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
        </style>

        <!-- მთავარი სახელი რომელიც პირველი ხვდებათ -->
        <div class="main-title">collab.ge</div>
        """,
      unsafe_allow_html=True,
  )

  # ღილაკი, რომელიც სახელის მერე გამოჩნდება
  col1, col2, col3 = st.columns([1, 1, 1])
  with col2:
    st.markdown('<div class="delayed-button-container">', unsafe_allow_html=True)
    if st.button("დაწყება", use_container_width=True):
      st.session_state.page = "register"
      st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- რეგისტრაციის გვერდი ---
elif st.session_state.page == "register":
  st.title("რეგისტრაცია")
  st.write("მოგესალმებით collab.ge-ს რეგისტრაციის გვერდზე!")

  # რეგისტრაციის ველები (მაგალითისთვის)
  username = st.text_input("სახელი / მომხმარებელი")
  email = st.text_input("ელ-ფოსტა")
  password = st.text_input("პაროლი", type="password")

  if st.button("რეგისტრაციის დასრულება"):
    st.success("წარმატებით დარეგისტრირდით!")

  st.write("")
  if st.button("← უკან დაბრუნება"):
    st.session_state.page = "home"
    st.rerun()
