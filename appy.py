import streamlit as st

st.set_page_config(page_title="Collab.ge — კრეატორებისა და ბრენდების პლატფორმა", layout="wide")

# სესხის მართვა ეტაპების გასავლელად
if "step" not in st.session_state:
    st.session_state.step = "welcome"  # ეტაპები: "welcome", "choose_role", "register", "main"
if "user_type" not in st.session_state:
    st.session_state.user_type = None
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "campaigns" not in st.session_state:
    st.session_state.campaigns = []
if "creators" not in st.session_state:
    st.session_state.creators = []

# პრემიუმ, სადა და დახვეწილი დიზაინი (ემოჯების გარეშე, მდიდრული ვიბით)
st.markdown("""
    <style>
    .stApp {
        background-color: #f7f5f0;
    }
    .main {
        background-color: #f7f5f0;
    }
    .stButton>button {
        background-color: #3b4231;
        color: #f7f5f0;
        border-radius: 6px;
        padding: 12px 28px;
        border: none;
        font-weight: 500;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        font-size: 12px;
        box-shadow: 0 4px 20px rgba(59, 66, 49, 0.08);
    }
    .stButton>button:hover {
        background-color: #2c3224;
        color: #ffffff;
    }
    .card {
        background-color: #ffffff;
        padding: 32px;
        border-radius: 12px;
        box-shadow: 0 4px 25px rgba(59, 66, 49, 0.04);
        margin-bottom: 24px;
        border: 1px solid #e8e4dc;
    }
    h1, h2, h3, p, label, span, a {
        color: #3b4231 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .hero-title {
        font-family: serif;
        letter-spacing: 6px;
        font-weight: 400;
        font-size: 48px;
        text-align: center;
        margin-top: 80px;
        margin-bottom: 16px;
    }
    .hero-subtitle {
        text-align: center;
        font-size: 16px;
        color: #6b7262 !important;
        margin-bottom: 40px;
        letter-spacing: 0.5px;
    }
    .subtext {
        color: #6b7262 !important;
        font-size: 15px;
        letter-spacing: 0.2px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------ტოტალური ეტაპები----------------

# ეტაპი 1: მისასალმებელი დიდი სათაური და დაწყების ღილაკი
if st.session_state.step == "welcome":
    st.markdown("<h1 class='hero-title'>C O L L A B . G E</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>პლატფორმა, რომელიც აკავშირებს წამყვან ბრენდებსა და კრეატორებს შიდა მარკეტინგული კამპანიებისთვის.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("დაწყება"):
            st.session_state.step = "choose_role"
            st.rerun()

# ეტაპი 2: როლის არჩევა (ბრენდი / კრეატორი)
elif st.session_state.step == "choose_role":
    st.markdown("<h1 class='hero-title' style='font-size: 36px; margin-top: 40px;'>აირჩიეთ თქვენი სტატუსი</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>ვისი სახით უერთდებით პლატფორმას?</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div class="card" style="text-align: center; padding: 40px;">
            <h3 style="font-family: serif; font-size: 22px; font-weight: 500; margin-bottom: 15px;">ბრენდი</h3>
            <p class="subtext">მსურს კამპანიების დამატება და კრეატორების მოძიება.</p>
        </div>
        """, unsafe_allow_html=True)
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            if st.button("ბრენდის რეგისტრაცია", key="ch_brand"):
                st.session_state.user_type = "brand"
                st.session_state.step = "register"
                st.rerun()

    with col2:
        st.markdown("""
        <div class="card" style="text-align: center; padding: 40px;">
            <h3 style="font-family: serif; font-size: 22px; font-weight: 500; margin-bottom: 15px;">კრეატორი</h3>
            <p class="subtext">მსურს კამპანიებში მონაწილეობა და ბრენდებთან თანამშრომლობა.</p>
        </div>
        """, unsafe_allow_html=True)
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            if st.button("კრეატორის რეგისტრაცია", key="ch_creator"):
                st.session_state.user_type = "creator"
                st.session_state.step = "register"
                st.rerun()

# ეტაპი 3: რეგისტრაციის ფორმა არჩეული როლის მიხედვით
elif st.session_state.step == "register":
    st.markdown(f"<h1 class='hero-title' style='font-size: 32px; margin-top: 30px;'>{'ბრენდის' if st.session_state.user_type == 'brand' else 'კრეატორის'} რეგისტრაცია</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>გთხოვთ შეავსოთ საჭირო ინფორმაცია პლატფორმაზე შესასვლელად.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.session_state.user_type == "brand":
            b_name = st.text_input("ბრენდის ოფიციალური დასახელება")
            b_contact = st.text_input("საკონტაქტო პირი / ელ-ფოსტა / ტელეფონი")
            
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            if st.button("რეგისტრაციის დასრულება"):
                if b_name and b_contact:
                    st.session_state.user_name = b_name
                    st.session_state.step = "main"
                    st.rerun()
                else:
                    st.warning("გთხოვთ შეავსოთ სავალდებულო ველები.")

        else:
            c_name = st.text_input("სახელი და გვარი")
            c_link = st.text_input("სოციალური ქსელის ბმული (Instagram / TikTok)")
            c_followers = st.number_input("გამომწერების რაოდენობა", min_value=500, step=500)
            
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            if st.button("რეგისტრაციის დასრულება"):
                if c_name and c_link:
                    st.session_state.user_name = c_name
                    # ავტომატურად ვამატებთ კრეატორთა ბაზაში
                    st.session_state.creators.append({
                        "name": c_name,
                        "link": c_link,
                        "followers": c_followers
                    })
                    st.session_state.step = "main"
                    st.rerun()
                else:
                    st.warning("გთხოვთ შეავსოთ სავალდებულო ველები.")

# ეტაპი 4: მთავარი პლატფორმა (მუშა სივრცე)
elif st.session_state.step == "main":
    top_col1, top_col2 = st.columns([4, 1])
    with top_col1:
        st.markdown(f"<h2 style='font-family: serif; font-size: 24px; margin:0;'>C O L L A B . G E</h2>", unsafe_allow_html=True)
        st.markdown(f"<p class='subtext' style='margin-top: 5px;'>მოგესალმებით, <b>{st.session_state.user_name}</b> ({'ბრენდი' if st.session_state.user_type == 'brand' else 'კრეატორი'})</p>", unsafe_allow_html=True)
    with top_col2:
        if st.button("გასვლა"):
            st.session_state.step = "welcome"
            st.session_state.user_type = None
            st.session_state.user_name = ""
            st.rerun()

    st.markdown("<hr style='border: 1px solid #e8e4dc; margin: 25px 0;'>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["აქტიური კამპანიები", "რეგისტრირებული კრეატორები"])

    with tab1:
        st.subheader("მიმდინარე კამპანიები")
        st.markdown("<p class='subtext' style='margin-bottom: 25px;'>ბრენდების მიერ დამატებული შეთავაზებები.</p>", unsafe_allow_html=True)

        if st.session_state.user_type == "brand":
            with st.expander("ახალი კამპანიის დამატება"):
                offer = st.text_area("შეთავაზების დეტალები (ბარტერი / ანაზღაურება)")
                req = st.text_input("მოთხოვნები კრეატორს")
                contact = st.text_input("საკონტაქტო ინფორმაცია")
                if st.button("კამპანიის გამოქვეყნება"):
                    if offer and contact:
                        new_camp = {
                            "brand": st.session_state.user_name,
                            "offer": offer,
                            "req": req if req else "ინდივიდუალური",
                            "contact": contact
                        }
                        st.session_state.campaigns.append(new_camp)
                        st.success("კამპანია წარმატებით გამოქვეყნდა.")
                        st.rerun()
                    else:
                        st.warning("გთხოვთ შეავსოთ სავალდებულო ველები.")

        if not st.session_state.campaigns:
            st.info("პლატფორმაზე ამჟამად აქტიური კამპანიები არ არის.")
        else:
            for idx, camp in enumerate(st.session_state.campaigns):
                st.markdown(f"""
                <div class="card">
                    <h3 style="margin-top:0; font-family: serif; font-size: 18px; font-weight: 500;">{camp['brand']}</h3>
                    <p style="margin: 8px 0;"><b>შეთავაზება:</b> {camp['offer']}</p>
                    <p style="margin: 8px 0;"><b>მოთხოვნა:</b> {camp['req']}</p>
                    <p style="margin: 8px 0;"><b>საკონტაქტო:</b> {camp['contact']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.session_state.user_type == "creator":
                    if st.button(f"განაცხადის გაგზავნა #{idx+1}", key=f"apply_{idx}"):
                        st.success("თქვენი განაცხადი წარმატებით გაიგზავნა.")

    with tab2:
        st.subheader("კრეატორთა ბაზა")
        st.markdown("<p class='subtext' style='margin-bottom: 25px;'>ბრენდებს შეუძლიათ დაათვალიერონ რეგისტრირებული კრეატორები და პირდაპირ დაუკავშირდნენ.</p>", unsafe_allow_html=True)

        if not st.session_state.creators:
            st.info("ბაზაში კრეატორები ჯერ არ არიან დარეგისტრირებული.")
        else:
            for cr in st.session_state.creators:
                st.markdown(f"""
                <div class="card">
                    <h3 style="margin-top:0; font-family: serif; font-size: 18px; font-weight: 500;">{cr['name']}</h3>
                    <p style="margin: 6px 0;"><b>სოციალური ქსელი:</b> <a href="{cr['link']}" target="_blank">{cr['link']}</a></p>
                    <p style="margin: 6px 0;"><b>გამომწერები:</b> {cr['followers']}+</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.session_state.user_type == "brand":
                    if st.button(f"თანამშრომლობის შეთავაზება — {cr['name']}", key=f"collab_{cr['name']}"):
                        st.success(f"შეტყობინება წარმატებით გაიგზავნა კრეატორთან ({cr['name']}).")
