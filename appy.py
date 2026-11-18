import streamlit as st

# CSS სტილები და HTML ელემენტები ანიმაციით
st.markdown(
    """
    <style>
    /* ანიმაციის წესები */
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
        animation: fadeIn 1.5s ease forwards;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        margin-top: 50px;
    }

    .fade-subtitle {
        animation: fadeIn 1.5s ease 0.5s forwards;
        opacity: 0;
        text-align: center;
        color: #94a3b8;
        margin-bottom: 30px;
    }
    </style>

    <!-- ვიზუალური ნაწილი ანიმაციით -->
    <div class="fade-title">ჩემი საიტი</div>
    <div class="fade-subtitle">მოგესალმებით, გთხოვთ აირჩიოთ მოქმედება</div>
    """,
    unsafe_allow_html=True,
)

# Streamlit-ის მშობლიური ღილაკები (უფრო მარტივია როცა ფუნქციონალიც უნდა ჰქონდეს)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  if st.button("🚀 დაწყება", use_container_width=True):
    st.success("დაწყების ღილაკი დააჭირე!")
  if st.button("ℹ️ გაიგე მეტი", use_container_width=True):
    st.info("აქ იქნება დამატებითი ინფორმაცია.")
