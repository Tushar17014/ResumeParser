import streamlit as st
from pdfminer.high_level import extract_text
from extract_info import extract_contact, extract_email, extract_name, extract_skills, extract_education
from categorize import predict_category
import os

st.title("Resume Parser")
st.write("Upload a resume to extract information.")



uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    file_path = f"./temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("Parsing the resume...")
    resume = extract_text(file_path)

    if os.path.exists(file_path):
        os.remove(file_path)

    contact = extract_contact(resume)
    email = extract_email(resume)
    name = extract_name(resume)
    skills = extract_skills(resume)
    education = extract_education(resume)

    extracted_info = {"Contact": contact, "Email": email, "Name": name, "Skills": skills, "Education": education}

    category = predict_category(resume)

    st.write("### Resume Category: ")
    st.write(category)
    st.write("### Extracted Information:")
    
    if extracted_info:
        st.write(f"**Name:** {extracted_info.get('Name', 'Not Found')}")
        st.write(f"**Contact:** {extracted_info.get('Contact', 'Not Found')}")
        st.write(f"**Email:** {extracted_info.get('Email', 'Not Found')}")
        st.write("**Skills:**")
        skills = extracted_info.get('Skills', [])
        if skills:
            st.write(", ".join(skills))
        else:
            st.write("Not Found")
        st.write("**Education:**")
        education = extracted_info.get('Education', [])
        if education:
            for edu in education:
                st.write(f"- {edu}")
        else:
            st.write("Not Found")
    else:
        st.write("No data extracted.")
