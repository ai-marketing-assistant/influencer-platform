import streamlit as st

st.set_page_config(page_title="Collab.ge — კრეატორებისა და ბრენდების პლატფორმა", page_icon="⚡", layout="wide")

# თანამედროვე, სუფთა სტარტაპული დიზაინი (Clean SaaS Style)
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .main {
        background-color: #0f172a;
    }
    /* თანამედროვე ნეონურ-იისფერი და ლურჯი აქცენტები */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
        color: white;
    }
    /* მუქი ბარათები მინის ეფექტით */
    .card {
        background-color: #1e293b;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        border: 1px solid #334155;
    }
    h1, h2, h3 {
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    p, label, span {
        color: #94a3b8 !important;
    }
    </style>
""", unsafe_allow_html=True)

# სათაური და შენ მიერ არჩეული ზუსტი აღწერა
st.markdown("<h1 style='text-align: center; font-weight: 800; letter-spacing: -1px;'>⚡ C O L L A B . G E</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 17px; margin-bottom: 40px; color: #cbd5e1;'>პლატფორმა, რომელიც აკავშირებს წამყვან ბრენდებსა და კრეატორებს შიდა მარკეტინგული კამპანიებისთვის.</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚀 აქტიური კამპანიები", "🏢 ბრენდისთვის", "✨ ინფლუენსერის რეგისტრაცია"])

with tab1:
    st.subheader("მიმდინარე კამპანიები")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h3>☕ კაფე "ლოკალი"</h3>
            <p><b>მოთხოვნა:</b> 3 მიკრო-კრეატორი (5K+ გამომწერი)</p>
            <p><b>შეთავაზება:</b> ბარტერი + ფიქსირებული ანაზღაურება სთორებზე</p>
            <p><b>ლოკაცია:</b> თბილისი</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("განაცხადის გაგზავნა", key="btn1"):
            st.success("განაცხადი წარმატებით გაიგზავნა!")

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🎧 ტექ-ბრენდი "სტუდიო"</h3>
            <p><b>მოთხოვნა:</b> 2 კრეატორი Reels / TikTok ვიდეოსთვის</p>
            <p><b>შეთავაზება:</b> პროდუქტი საჩუქრად + 250₾</p>
            <p><b>ლოკაცია:</b> მთელი საქართველო</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("განაცხადის გაგზავნა", key="btn2"):
            st.success("განაცხადი წარმატებით გაიგზავნა!")

with tab2:
    st.subheader("კამპანიის განთავსება (ბრენდი)")
    brand_name = st.text_input("ბრენდის სახელი")
    offer = st.text_area("შეთავაზების დეტალები (ბარტერი / ბიუჯეტი)")
    req = st.text_input("მოთხოვნები კრეატორს")
    contact = st.text_input("საკონტაქტო (Instagram Direct ან ტელეფონი)")
    if st.button("კამპანიის გამოქვეყნება"):
        if brand_name and offer:
            st.success(f"კამპანია '{brand_name}' წარმატებით დაემატა ბაზაში!")
        else:
            st.warning("გთხოვთ შეავსოთ ძირითადი ველები.")

with tab3:
    st.subheader("კრეატორის პროფილი")
    inf_name = st.text_input("სახელი და გვარი")
    ig_link = st.text_input("Instagram / TikTok პროფილის ბმული")
    followers = st.number_input("გამომწერების რაოდენობა", min_value=500, step=500)
    niche = st.selectbox("კატეგორია / ნიშა", ["ტექნოლოგიები და გეიმინგი", "ლაიფსტაილი და მოდა", "კვება და ჰორეკა", "მოგზაურობა", "სხვა"])
    if st.button("პროფილის რეგისტრაცია"):
        if inf_name and ig_link:
            st.success("თქვენი პროფილი წარმატებით დარეგისტრირდა პლატფორმაზე!")
        else:
            st.warning("გთხოვთ მიუთითოთ სახელი და სოც. ქსელის ბმული.")
