import streamlit as st

st.set_page_config(page_title="Collab.ge — კრეატორებისა და ბრენდების პლატფორმა", layout="wide")

# სესხის მართვა რეგისტრაციისთვის და მონაცემებისთვის
if "registered" not in st.session_state:
    st.session_state.registered = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None  # "brand" ან "creator"
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "campaigns" not in st.session_state:
    st.session_state.campaigns = []
if "creators" not in st.session_state:
    st.session_state.creators = []

# პრემიუმ, სადა და დახვეწილი დიზაინი (ემოჯების გარეშე)
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
        padding: 12px 24px;
        border: none;
        font-weight: 500;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 12px;
        box-shadow: 0 4px 15px rgba(59, 66, 49, 0.08);
    }
    .stButton>button:hover {
        background-color: #2c3224;
        color: #ffffff;
    }
    .card {
        background-color: #ffffff;
        padding: 28px;
        border-radius: 12px;
        box-shadow: 0 4px 25px rgba(59, 66, 49, 0.04);
        margin-bottom: 24px;
        border: 1px solid #e8e4dc;
    }
    h1, h2, h3, p, label, span, a {
        color: #3b4231 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .title-text {
        font-family: serif;
        letter-spacing: 4px;
        font-weight: 400;
    }
    .subtext {
        color: #6b7262 !important;
        font-size: 15px;
        letter-spacing: 0.2px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. მთავარი შესასვლელი (თუ მომხმარებელი არ არის დარეგისტრირებული)
if not st.session_state.registered:
    st.markdown("<h1 class='title-text' style='text-align: center; font-size: 40px; margin-top: 30px; margin-bottom: 12px;'>C O L L A B . G E</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 15px; color: #6b7262; margin-bottom: 50px; letter-spacing: 0.5px;'>პლატფორმა, რომელიც აკავშირებს წამყვან ბრენდებსა და კრეატორებს შიდა მარკეტინგული კამპანიებისთვის.</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="font-family: serif; font-size: 20px; font-weight: 500; margin-top:0;">ბრენდებისთვის</h3>
            <p class="subtext" style="margin-top: 15px;">განათავსეთ კამპანიები, მართეთ შეთავაზებები და პირდაპირ დაუკავშირდით კრეატორებს.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("რეგისტრაცია ბრენდისთვის", key="reg_brand_btn"):
            st.session_state.reg_mode = "brand"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="font-family: serif; font-size: 20px; font-weight: 500; margin-top:0;">კრეატორებისთვის</h3>
            <p class="subtext" style="margin-top: 15px;">შექმენით პროფილი, დაათვალიერეთ აქტიური კამპანიები და მიიღეთ შეთავაზებები.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("რეგისტრაცია კრეატორისთვის", key="reg_creator_btn"):
            st.session_state.reg_mode = "creator"
            st.rerun()

    # რეგისტრაციის ფორმის გამოჩენა არჩევნის მიხედვით
    if "reg_mode" in st.session_state:
        st.markdown("<hr style='border: 1px solid #e8e4dc; margin: 40px 0;'>", unsafe_allow_html=True)
        
        if st.session_state.reg_mode == "brand":
            st.subheader("ბრენდის რეგისტრაცია")
            b_name = st.text_input("ბრენდის ოფიციალური დასახელება")
            b_contact = st.text_input("საკონტაქტო პირი / ელ-ფოსტა / ტელეფონი")
            
            if st.button("რეგისტრაციის დასრულება"):
                if b_name and b_contact:
                    st.session_state.registered = True
                    st.session_state.user_type = "brand"
                    st.session_state.user_name = b_name
                    st.rerun()
                else:
                    st.warning("გთხოვთ შეავსოთ სავალდებულო ველები.")

        elif st.session_state.reg_mode == "creator":
            st.subheader("კრეატორის რეგისტრაცია")
            c_name = st.text_input("სახელი და გვარი")
            c_link = st.text_input("სოციალური ქსელის ბმული (Instagram / TikTok)")
            c_followers = st.number_input("გამომწერების რაოდენობა", min_value=500, step=500)
            
            if st.button("რეგისტრაციის დასრულება"):
                if c_name and c_link:
                    st.session_state.registered = True
                    st.session_state.user_type = "creator"
                    st.session_state.user_name = c_name
                    # ავტომატურად ვამატებთ კრეატორთა ბაზაში
                    st.session_state.creators.append({
                        "name": c_name,
                        "link": c_link,
                        "followers": c_followers
                    })
                    st.rerun()
                else:
                    st.warning("გთხოვთ შეავსოთ სავალდებულო ველები.")

# 2. მთავარი აპლიკაცია (თუ მომხმარებელი წარმატებით დარეგისტრირდა)
else:
    top_col1, top_col2 = st.columns([4, 1])
    with top_col1:
        st.markdown(f"<h2 style='font-family: serif; font-size: 24px; margin:0;'>C O L L A B . G E</h2>", unsafe_allow_html=True)
        st.markdown(f"<p class='subtext' style='margin-top: 5px;'>მოგესალმებით, <b>{st.session_state.user_name}</b> ({'ბრენდი' if st.session_state.user_type == 'brand' else 'კრეატორი'})</p>", unsafe_allow_html=True)
    with top_col2:
        if st.button("გასვლა"):
            st.session_state.registered = False
            st.session_state.user_type = None
            st.session_state.user_name = ""
            if "reg_mode" in st.session_state:
                del st.session_state.reg_mode
            st.rerun()

    st.markdown("<hr style='border: 1px solid #e8e4dc; margin: 25px 0;'>", unsafe_allow_html=True)

    # ორმხრივი სამუშაო სივრცე
    tab1, tab2 = st.tabs(["აქტიური კამპანიები", "რეგისტრირებული კრეატორები"])

    with tab1:
        st.subheader("მიმდინარე კამპანიები")
        st.markdown("<p class='subtext' style='margin-bottom: 25px;'>ბრენდების მიერ დამატებული შეთავაზებები.</p>", unsafe_allow_html=True)

        # თუ ბრენდია, მისთვის ვხსნით კამპანიის დამატების ფორმას
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
                    # დასრულებულია შეტყობინების იმიტაცია
                        st.success(f"შეტყობინება წარმატებით გაიგზავნა კრეატორთან ({cr['name']}).")
