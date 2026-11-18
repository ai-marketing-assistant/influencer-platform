import streamlit as st

# გვერდის საწყისი მდგომარეობა
if "page" not in st.session_state:
  st.session_state.page = "home"

# --- მთავარი გვერდი (ანიმაციური შესავალი) ---
if st.session_state.page == "home":
  st.markdown(
      """
        <style>
        /* ეკრანის ცენტრში მოქცევა */
        .welcome-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 65vh;
            text-align: center;
        }

        /* სახელი collab.ge - თავიდან უფერული (opacity: 0) და ოდნავ ქვემოთ, მერე ნელა შემოდის */
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

        /* ღილაკის ანიმაცია - ჩნდება სახელის შემოსვლის შემდეგ */
        @keyframes fadeInButton {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            70% {
                opacity: 0;
                transform: translateY(20px);
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
            color: #ffffff;
            letter-spacing: 3px;
            margin-bottom: 20px;
        }

        .btn-box {
            animation: fadeInButton 2.4s ease forwards;
            opacity: 0;
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        </style>

        <div class="welcome-container">
            <!-- აპლიკაციის დიდი სახელი, რომელიც ნელ-ნელა ხილული ხდება -->
            <div class="app-title">collab.ge</div>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # ღილაკი, რომელიც სახელის გამოჩენის მერე მოდის
  col1, col2, col3 = st.columns([1, 1, 1])
  with col2:
    st.markdown('<div class="btn-box">', unsafe_allow_html=True)
    if st.button("დაწყება", use_container_width=True):
      st.session_state.page = "register"
      st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

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
