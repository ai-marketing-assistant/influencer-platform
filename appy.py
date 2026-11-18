import streamlit as st

# გვერდის კონფიგურაცია
st.set_page_config(page_title="collab.ge", page_icon="✨", layout="wide")

# --- სესიის საწყისი მდგომარეობები ---
if "page" not in st.session_state:
  st.session_state.page = "home"
if "role" not in st.session_state:
  st.session_state.role = ""
if "username" not in st.session_state:
  st.session_state.username = ""

# ბაზები (მეხსიერებაში შესანახად აპლიკაციის ფარგლებში)
if "influencers" not in st.session_state:
  st.session_state.influencers = [
      {
          "name": "ნინი კანდელაკი",
          "followers": "45K",
          "content": "მოდა და ლაიფსტაილი",
          "ig": "instagram.com/nini",
          "tt": "tiktok.com/@nini",
      },
      {
          "name": "გიორგი ბერიძე",
          "followers": "120K",
          "content": "ტექნოლოგიები და გეიმინგი",
          "ig": "instagram.com/giorgi",
          "tt": "tiktok.com/@giorgi",
      },
  ]

if "offers" not in st.session_state:
  st.session_state.offers = [
      {
          "company": "Moya Matcha",
          "title": "ახალი პროდუქტის რეკლამირება",
          "desc": (
              "ვეძებთ ინფლუენსერებს სთორების და ვიდეოების ასატვირთად."
          ),
      },
      {
          "company": "Style Ge",
          "title": "ზამთრის კოლექციის პრომო",
          "desc": "გვჭირდება მოდის მიმართულების ინფლუენსერები.",
      },
  ]


# --- ერთიანი დახვეწილი მწვანე/ბეჟი დიზაინი (CSS) ---
st.markdown(
    """
    <style>
    /* მთლიანი აპის მუქი მწვანე ფონი */
    .stApp {
        background-color: #2b382f;
        color: #f5f2eb;
    }

    /* სათაურები ბეჟი/ღია ფერში */
    h1, h2, h3, h4 {
        color: #f5f2eb !important;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* ღილაკების დახვეწილი სტილი ჩარჩოებით */
    .stButton button {
        background-color: transparent !important;
        color: #f5f2eb !important;
        border: 1px solid rgba(245, 242, 235, 0.4) !important;
        border-radius: 6px;
        font-weight: 500;
        letter-spacing: 1px;
        padding: 10px 20px;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton button:hover {
        background-color: rgba(245, 242, 235, 0.15) !important;
        border-color: #f5f2eb !important;
    }

    /* ტექსტური ველების ჩარჩოები და დიზაინი */
    .stTextInput input, .stTextArea textarea {
        background-color: #1e2721 !important;
        color: #f5f2eb !important;
        border: 1px solid rgba(245, 242, 235, 0.3) !important;
        border-radius: 6px;
    }

    /* ბარათების (Cards) ჩარჩოები */
    .card-box {
        background-color: #1e2721;
        border: 1px solid rgba(245, 242, 235, 0.2);
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ==========================================
# 1. მთავარი გვერდი (ანიმაციური შესავალი)
# ==========================================
if st.session_state.page == "home":
  st.markdown(
      """
        <style>
        .welcome-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 55vh;
            text-align: center;
        }

        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .app-title {
            animation: fadeIn 1.8s ease forwards;
            font-size: 4rem;
            font-weight: 300;
            letter-spacing: 6px;
            color: #f5f2eb;
            margin-bottom: 10px;
        }

        .app-subtitle {
            animation: fadeIn 1.8s ease 0.4s forwards;
            opacity: 0;
            font-size: 0.9rem;
            letter-spacing: 3px;
            color: #d1c7bd;
            text-transform: uppercase;
            margin-bottom: 30px;
        }
        </style>

        <div class="welcome-container">
            <div class="app-title">COLLAB.GE</div>
            <div class="app-subtitle">ინფლუენსერებისა და კომპანიების პლატფორმა</div>
        </div>
        """,
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns([1.5, 2, 1.5])
  with col2:
    if st.button("დაწყება"):
      st.session_state.page = "role_select"
      st.rerun()


# ==========================================
# 2. როლის არჩევა (რეგისტრაცია / შესვლა)
# ==========================================
elif st.session_state.page == "role_select":
  st.title("აირჩიეთ თქვენი როლი")
  st.write("ვინ ხართ?")

  col1, col2 = st.columns(2)
  with col1:
    if st.button("🏢 კომპანია"):
      st.session_state.role = "company"
      st.session_state.page = "register"
      st.rerun()
  with col2:
    if st.button("✨ ინფლუენსერი"):
      st.session_state.role = "influencer"
      st.session_state.page = "register"
      st.rerun()

  st.write("")
  if st.button("← უკან დაბრუნება"):
    st.session_state.page = "home"
    st.rerun()


# ==========================================
# 3. რეგისტრაციის ფორმა (როლის მიხედვით)
# ==========================================
elif st.session_state.page == "register":
  if st.session_state.role == "company":
    st.title("კომპანიის რეგისტრაცია")
    comp_name = st.text_input("კომპანიის სახელი")
    offer_title = st.text_input("შეთავაზების სათაური (მაგ: ახალი კამპანია)")
    offer_desc = st.text_area("შეთავაზების აღწერა")

    if st.button("რეგისტრაცია და შესვლა"):
      if comp_name and offer_title:
        st.session_state.username = comp_name
        st.session_state.offers.append(
            {"company": comp_name, "title": offer_title, "desc": offer_desc}
        )
        st.session_state.page = "dashboard"
        st.rerun()
      else:
        st.warning("გთხოვთ შეავსოთ ძირითადი ველები!")

  else:
    st.title("ინფლუენსერის რეგისტრაცია")
    inf_name = st.text_input("სახელი / გვარი ან არხის სახელი")
    followers = st.text_input("ფოლოვერების რაოდენობა (მაგ: 50K)")
    content_type = st.text_input("ძირითადი კონტენტი (მაგ: ლაიფსტაილი, თეიქი)")
    ig_link = st.text_input("Instagram-ის ლინკი")
    tt_link = st.text_input("TikTok-ის ლინკი")

    if st.button("რეგისტრაცია და შესვლა"):
      if inf_name:
        st.session_state.username = inf_name
        st.session_state.influencers.append({
            "name": inf_name,
            "followers": followers,
            "content": content_type,
            "ig": ig_link,
            "tt": tt_link,
        })
        st.session_state.page = "dashboard"
        st.rerun()
      else:
        st.warning("გთხოვთ შეიყვანოთ სახელი!")

  if st.button("← უკან"):
    st.session_state.page = "role_select"
    st.rerun()


# ==========================================
# 4. მთავარი სამუშაო გვერდი (Dashboard)
# ==========================================
elif st.session_state.page == "dashboard":
  st.title(f"მოგესალმებით, {st.session_state.username}! 👋")

  # --- თუ მომხმარებელი არის ინფლუენსერი ---
  if st.session_state.role == "influencer":
    st.write(
        "### აქტიური შეთავაზებები კომპანიებისგან (შეგიძლიათ გააგზავნოთ"
        " განაცხადი):"
    )

    for idx, offer in enumerate(st.session_state.offers):
      st.markdown(
          f"""
            <div class="card-box">
                <h4>🏢 {offer['company']}</h4>
                <p><b>სათაური:</b> {offer['title']}</p>
                <p><b>აღწერა:</b> {offer['desc']}</p>
            </div>
            """,
          unsafe_allow_html=True,
      )
      if st.button(
          f"განაცხადის გაგზავნა ({offer['company']})", key=f"offer_{idx}"
      ):
        st.success(
            f"განაცხადი წარმატებით გაეგზავნა კომპანიას — {offer['company']}!"
        )

  # --- თუ მომხმარებელი არის კომპანია ---
  else:
    tab1, tab2 = st.tabs(
        ["📋 ყველა შეთავაზება", "✨ რეგისტრირებული ინფლუენსერები"]
    )

    with tab1:
      st.write("### პლატფორმაზე არსებული ყველა კომპანიის შეთავაზება:")
      for offer in st.session_state.offers:
        st.markdown(
            f"""
                <div class="card-box">
                    <h4>🏢 {offer['company']}</h4>
                    <p><b>სათაური:</b> {offer['title']}</p>
                    <p><b>აღწერა:</b> {offer['desc']}</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      st.write("---")
      st.write("### დაამატე ახალი შეთავაზება:")
      new_title = st.text_input("შეთავაზების სათაური")
      new_desc = st.text_area("შეთავაზების დეტალები")
      if st.button("დამატება"):
        if new_title:
          st.session_state.offers.append({
              "company": st.session_state.username,
              "title": new_title,
              "desc": new_desc,
          })
          st.success("შეთავაზება წარმატებით დაემატა!")
          st.rerun()

    with tab2:
      st.write(
          "### აპლიკაციაში რეგისტრირებული ინფლუენსერები და მათი მონაცემები:"
      )
      for inf in st.session_state.influencers:
        st.markdown(
            f"""
                <div class="card-box">
                    <h3>✨ {inf['name']}</h3>
                    <p><b>ფოლოვერები:</b> 👥 {inf['followers']}</p>
                    <p><b>კონტენტი:</b> 🎬 {inf['content']}</p>
                    <p><b>სოც-ლინკები:</b> 
                       <a href="https://{inf['ig']}" target="_blank" style="color: #d1c7bd; margin-right: 15px;">Instagram</a> 
                       <a href="https://{inf['tt']}" target="_blank" style="color: #d1c7bd;">TikTok</a>
                    </p>
                </div>
                """,
            unsafe_allow_html=True,
        )

  st.write("")
  if st.button("სისტემიდან გასვლა (Logout)"):
    st.session_state.page = "home"
    st.session_state.role = ""
    st.session_state.username = ""
    st.rerun()
