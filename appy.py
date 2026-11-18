import streamlit as st

st.set_page_config(page_title="Collab.ge — კრეატორებისა და ბრენდების პლატფორმა", layout="wide")

# სია იწყება სრულად ცარიელი ფურცლიდან — რეალური ბაზა
if "campaigns" not in st.session_state:
    st.session_state.campaigns = []

if "creators" not in st.session_state:
    st.session_state.creators = []

# მდიდრული, სადა და დახვეწილი პრემიუმ დიზაინი (ემოჯებისა და ყალბი მონაცემების გარეშე)
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
        padding: 10px 24px;
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
    h1, h2, h3, p, label, span {
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

st.markdown("<h1 class='title-text' style='text-align: center; font-size: 36px; margin-bottom: 12px;'>C O L L A B . G E</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 15px; color: #6b7262; margin-bottom: 45px; letter-spacing: 0.5px;'>პლატფორმა, რომელიც აკავშირებს წამყვან ბრენდებსა და კრეატორებს შიდა მარკეტინგული კამპანიებისთვის.</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["აქტიური კამპანიები", "ბრენდისთვის", "კრეატორის რეგისტრაცია"])

with tab1:
    st.subheader("მიმდინარე კამპანიები")
    st.markdown("<p class='subtext' style='margin-bottom: 25px;'>აირჩიეთ სასურველი შეთავაზება და გააგზავნეთ განაცხადი.</p>", unsafe_allow_html=True)
    
    if not st.session_state.campaigns:
        st.info("პლატფორმაზე ამჟამად აქტიური კამპანიები არ არის. გთხოვთ, დაამატოთ ახალი განცხადება 'ბრენდისთვის' განყოფილებიდან.")
    else:
        for idx, camp in enumerate(st.session_state.campaigns):
            st.markdown(f"""
            <div class="card">
                <h3 style="margin-top:0; font-family: serif; font-size: 20px; font-weight: 500;">{camp['brand']}</h3>
                <p style="margin: 10px 0;"><b>შეთავაზება:</b> {camp['offer']}</p>
                <p style="margin: 10px 0;"><b>მოთხოვნა:</b> {camp['req']}</p>
                <p style="margin: 10px 0;"><b>საკონტაქტო:</b> {camp['contact']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"განაცხადის გაგზავნა #{idx+1}", key=f"apply_{idx}"):
                st.success("თქვენი განაცხადი წარმატებით გაიგზავნა.")

with tab2:
    st.subheader("ახალი კამპანიის განთავსება")
    st.markdown("<p class='subtext' style='margin-bottom: 25px;'>შეავსეთ ფორმა კამპანიის პლატფორმაზე გამოსაქვეყნებლად.</p>", unsafe_allow_html=True)
    
    brand_name = st.text_input("ბრენდის დასახელება")
    offer = st.text_area("შეთავაზების დეტალები (ბარტერი / ანაზღაურება)")
    req = st.text_input("მოთხოვნები კრეატორს")
    contact = st.text_input("საკონტაქტო ინფორმაცია (Instagram / ტელეფონი / ელ-ფოსტა)")
    
    if st.button("გამოქვეყნება"):
        if brand_name and offer and contact:
            new_camp = {
                "brand": brand_name,
                "offer": offer,
                "req": req if req else "ინდივიდუალური",
                "contact": contact
            }
            st.session_state.campaigns.append(new_camp)
            st.success(f"კამპანია '{brand_name}' წარმატებით დაემატა.")
        else:
            st.warning("გთხოვთ შეავსოთ სავალდებულო ველები.")

with tab3:
    st.subheader("კრეატორის რეგისტრაცია")
    st.markdown("<p class='subtext' style='margin-bottom: 25px;'>დარეგისტრირდით კრეატორთა ბაზაში.</p>", unsafe_allow_html=True)
    
    inf_name = st.text_input("სახელი და გვარი")
    ig_link = st.text_input("Instagram / TikTok პროფილის ბმული")
    followers = st.number_input("გამომწერების რაოდენობა", min_value=500, step=500)
    niche = st.selectbox("კატეგორია / ნიშა", ["ესთეტიკა და ლაიფსტაილი", "კვება და კაფეები", "მოგზაურობა", "მოდა", "თავის მოვლა"])
    
    if st.button("რეგისტრაცია"):
        if inf_name and ig_link:
            st.success(f"მადლობა, {inf_name}. თქვენი პროფილი წარმატებით დარეგისტრირდა.")
        else:
            st.warning("გთხოვთ მიუთითოთ სახელი და სოც. ქსელის ბმული.")
