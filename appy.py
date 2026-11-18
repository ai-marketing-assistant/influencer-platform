import streamlit as st

# გვერდის საწყისი მდგომარეობის შექმნა
if "page" not in st.session_state:
  st.session_state.page = "home"

# --- მთავარი გვერდი ანიმაციით ---
if st.session_state.page == "home":
  st.markdown(
      """
        <style>
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .fade-title {
            animation: fadeIn 1.2s ease forwards;
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            color: #ffffff;
            margin-top: 80px;
        }

        .fade-subtitle {
            animation: fadeIn 1.2s ease 0.4s forwards;
            opacity: 0;
            text-align: center;
            color: #94a3b8;
            font-size: 1.2rem;
            margin-bottom: 40px;
        }
        </style>

        <div class="fade-title">ჩემი პლატფორმა</div>
        <div class="fade-subtitle">მოგესალმებით, გთხოვთ აირჩიოთ მოქმედება</div>
        """,
      unsafe_allow_html=True,
  )

  # ღილაკები ცენტრში
  col1, col2, col3 = st.columns([1, 1.5, 1])
  with col2:
    # რეგისტრაციის ღილაკი
    if st.button("რეგისტრაცია", use_container_width=True):
      st.session_state.page = "register"
      st.rerun()

    # შესვლის ღილაკი (თუ დაგჭირდეს)
    if st.button("შესვლა", use_container_width=True):
      st.session_state.page = "login"
      st.rerun()

# --- რეგისტრაციის გვერდი ---
elif st.session_state.page == "register":
  st.title("რეგისტრაციის გვერდი")
  st.write("აქ იქნება რეგისტრაციის ფორმა (მონაცემების შეყვანა).")

  if st.button("← უკან დაბრუნება"):
    st.session_state.page = "home"
    st.rerun()

# --- შესვლის გვერდი ---
elif st.session_state.page == "login":
  st.title("შესვლის გვერდი")
  st.write("აქ იქნება ავტორიზაციის ფორმა.")

  if st.button("← უკან დაბრუნება"):
    st.session_state.page = "home"
    st.rerun()
