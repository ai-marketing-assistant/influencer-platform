import streamlit as st

st.set_page_config(page_title="Collab.ge — კრეატორებისა და ბრენდების პლატფორმა", page_icon="🌿", layout="wide")

# დინამიური მეხსიერება (რომ კამპანიები და განაცხადები რეალურად ინახებოდეს)
if "campaigns" not in st.session_state:
    st.session_state.campaigns = [
        {
            "brand": "🌿 Matcha & Tea Studio",
            "offer": "პრემიუმ სასაჩუქრე ნაკრები + დეგუსტაცია",
            "req": "3 მიკრო-კრეატორი (3K+ გამომწერი)",
            "contact": "Instagram: @matcha.ge"
        },
        {
            "brand": "☕ Minimalist Cafe",
            "offer": "ღია მენიუ ორ პერსონაზე + კონტენტ ბარტერი",
            "req": "2 სთორი და 1 ესთეტიკური Reels-ი",
            "contact": "Tel: 555 98 76 54"
        }
    ]

if "applications" not in st.session_state:
    st.session_state.applications = []

# პრემიუმ "MOYA" სტილის დიზაინი (ზეთისხილისფერი და კრემისფერი, jobs.ge სტილის სისუფთავე)
st.markdown("""
    <style>
    .stApp {
        background-color: #f7f5f0;
        color: #3b4231;
    }
    .main {
        background-color: #f7f5f0;
    }
    /* ზეთისხილისფერი ღილაკები */
    .stButton>button {
        background-color: #3b4231;
        color: #f7f5f0;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
        font-weight: 500;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(59, 66, 49, 0.1);
    }
    .stButton>button:hover {
        background-color: #2c3224;
        color: white;
    }
    /* ელეგანტური კრემისფერი/თეთრი ბარათები */
    .card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(59, 66, 49, 0.05);
        margin-bottom: 20px;
        border: 1px solid #e8e4dc;
    }
    h1, h2, h3 {
        color: #3b4231;
        font-family: serif;
    }
    p, label, span {
        color: #555c4d !important;
    }
    </style>
""", unsafe_allow_html=True)

# სათაური და შენ მიერ არჩეული ზუსტი აღწერა
st.markdown("<h1 style='text-align: center; letter-spacing: 2px;'>C O L L A B . G E</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #737b67; margin-bottom: 35px;'>პლატფორმა, რომელიც აკავშირებს წამყვან ბრენდებსა და კრეატორებს შიდა მარკეტინგული კამპანიებისთვის.</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["✨ აქტიური კამპანიები", "🏢 ბრენდისთვის (დამატება)", "🌿 კრეატორის რეგისტრაცია"])

with tab1:
    st.subheader("მიმდინარე კამპანიები და ვაკანსიები")
    st.markdown("<p style='color: #737b67; margin-bottom: 20px;'>აირჩიე შენთვის სასურველი შეთავაზება და გააგზავნე განაცხადი პირდაპირ ბრენდთან.</p>", unsafe_allow_html=True)
    
    for idx, camp in enumerate(st.session_state.campaigns):
        st.markdown(f"""
        <div class="card">
            <h3>{camp['brand']}</h3>
            <p><b>შეთავაზება:</b> {camp['offer']}</p>
            <p><b>მოთხოვნა:</b> {camp['req']}</p>
            <p><b>საკონტაქტო:</b> {camp['contact']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b = st.columns([1, 4])
        with col_a:
            if st.button(f"განაცხადის გაგზავნა #{idx+1}", key=f"apply_{idx}"):
                st.success("თქვენი განაცხადი წარმატებით გაიგზავნა! ბრენდი მალე დაგიკავშირდებათ.")

with tab2:
    st.subheader("ახალი კამპანიის განთავსება (ბრენდის პანელი)")
    st.markdown("<p style='color: #737b67;'>შეავსეთ ფორმა და თქვენი შეთავაზება წამებში გამოჩნდება მთავარ გვერდზე.</p>", unsafe_allow_html=True)
    
    brand_name = st.text_input("ბრენდის სახელი")
    offer = st.text_area("შეთავაზების დეტალები (ბარტერი / ანაზღაურება)")
    req = st.text_input("მოთხოვნები კრეატორს (მაგ: 3K+ გამომწერი)")
    contact = st.text_input("საკონტაქტო ინფორმაცია (Instagram / ტელეფონი / ელ-ფოსტა)")
    
    if st.button("კამპანიის გამოქვეყნება"):
        if brand_name and offer and contact:
            new_camp = {
                "brand": brand_name,
                "offer": offer,
                "req": req if req else "ინდივიდუალური",
                "contact": contact
            }
            st.session_state.campaigns.append(new_camp)
            st.success(f"კამპანია '{brand_name}' წარმატებით დაემატა პლატფორმაზე!")
        else:
            st.warning("გთხოვთ შეავსოთ ძირითადი ველები (ბრენდი, შეთავაზება, კონტაქტი).")

with tab3:
    st.subheader("კრეატორის პროფილი და რეგისტრაცია")
    st.markdown("<p style='color: #737b67;'>დარეგისტრირდით ბაზაში, რომ ბრენდებმა მარტივად გიპოვონ.</p>", unsafe_allow_html=True)
    
    inf_name = st.text_input("სახელი და გვარი")
    ig_link = st.text_input("Instagram / TikTok პროფილის ბმული")
    followers = st.number_input("გამომწერების რაოდენობა", min_value=500, step=500)
    niche = st.selectbox("კატეგორია / ნიშა", ["ესთეტიკა და ლაიფსტაილი", "კვება და კაფეები", "მოგზაურობა", "მოდა", "თავის მოვლა"])
    
    if st.button("პროფილის შენახვა"):
        if inf_name and ig_link:
            st.success(f"მადლობა, {inf_name}! თქვენი პროფილი წარმატებით დაემატა კრეატორთა კატალოგში.")
        else:
            st.warning("გთხოვთ მიუთითოთ სახელი და სოც. ქსელის ბმული.")
