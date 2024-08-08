import streamlit as st

def main():
    st.set_page_config(
    page_title="BitLocks",
    page_icon="❤️",
    layout="centered",
)

#     st.title("🔥 Welcome to BitLocks! 🔥")
#     logo_image = 'BitLocks_logo.jpg'  # Replace 'bitlocks_logo.png' with the actual file name of your logo
#     st.image(logo_image, width=150)
#     st.markdown("### Quick Links:")
#     encrypt_button = '[🔒 Encrypt Files with BitLocks](https://bitlocks-encryption.streamlit.app/)'
#     decrypt_button = '[🔓 Decrypt Files with BitLocks](https://bitlocks-decryption.streamlit.app/)'
#     st.markdown(encrypt_button, unsafe_allow_html=True)
#     st.markdown(decrypt_button, unsafe_allow_html=True)

#     st.write("BitLocks simplifies data security by encrypting and storing sensitive files with ease. Our user-friendly interface empowers users of all levels of expertise to safeguard their data.")

#     st.write("We leverage the InterPlanetary File System (IPFS) for secure storage, distributing files across a decentralized network to minimize the risk of breaches and ensure data integrity.")

#     st.write("Our seamless integration with the Verbwire API for IPFS storage ensures smooth execution and reliable file storage without the hassle.")

#     st.write("Secure personal documents, financial records, or confidential business files with confidence. BitLocks offers robust encryption and decentralized storage.")

#     st.write("In summary, BitLocks simplifies encryption and storage while enhancing security through advanced techniques and decentralized storage.")
import io
#import streamlit as st
#import snowflake_dcr as dcr
import os
#from zipfile import ZipFile

# Page settings
st.set_page_config(
    page_title="BitLocks Setup Assistant",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This app generates setup scripts for BitLocks!"
    }
)

# Set up main page
col1, col2 = st.columns((6, 1))
col1.title("🔒 BitLocks   🔒")
col2.image("BitLocks_logo.jpg", width=120)
st.sidebar.image("BitLocks_logo.jpg")
# action = st.sidebar.radio("What action would you like to take?", ("Initial Deployment 🔐",
#                                                                   "Add Additional User 🗝️",
#                                                                   "Upgrade Security 🔒",
#                                                                   "Uninstall 🗑️"))

# Introduction
st.markdown("### Quick Links:")
encrypt_button = '[🔒 Encrypt Files with BitLocks](https://bitlocks-encryption.streamlit.app/)'
decrypt_button = '[🔓 Decrypt Files with BitLocks](https://bitlocks-decryption.streamlit.app/)'
st.markdown(encrypt_button, unsafe_allow_html=True)
st.markdown(decrypt_button, unsafe_allow_html=True)

st.write("BitLocks simplifies data security by encrypting and storing sensitive files with ease. Our user-friendly interface empowers users of all levels of expertise to safeguard their data.")

st.write("We leverage the InterPlanetary File System (IPFS) for secure storage, distributing files across a decentralized network to minimize the risk of breaches and ensure data integrity.")

st.write("Our seamless integration with the Verbwire API for IPFS storage ensures smooth execution and reliable file storage without the hassle.")

st.write("Secure personal documents, financial records, or confidential business files with confidence. BitLocks offers robust encryption and decentralized storage.")

st.write("In summary, BitLocks simplifies encryption and storage while enhancing security through advanced techniques and decentralized storage.")

# Build form based on selected action
# if action == "Initial Deployment 🔐":
#     st.subheader("🔒 Initial Deployment! 🔒")

#     with st.form("initial_deployment_form"):
#         version = "BitLocks 1.0"
#         admin_email = st.text_input("Admin Email Address")
#         admin_password = st.text_input("Admin Password", type="password")
#         company_name = st.text_input("Company Name")
#         company_size = st.selectbox("Company Size", ["Small", "Medium", "Large"])
#         submitted = st.form_submit_button("Deploy")

#         if submitted:
#             with st.spinner("Generating Setup Scripts..."):
#                 bitlocks_setup.prepare_initial_deployment(version, admin_email, admin_password, company_name, company_size)
#                 bitlocks_setup.execute()

#             st.success("Setup Scripts Ready for Download!")
#             #load_zip_buffer(bitlocks_setup, zip_buffer)

# # Add other action forms similarly...

# if st.button("Download Setup Scripts"):
#     st.download_button(label="Download Setup Scripts", data=zip_buffer, file_name="bitlocks_setup.zip")

    

# if __name__ == "__main__":
#     main()
