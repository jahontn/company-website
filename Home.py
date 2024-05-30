import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Bizning Korhona")
comment = """
Finding a best company to work for seems an elusive task for disillusioned young and older employees alike.
Any employer worth its salt has recognized and responded to the shifting demands of the workforce in order to 
hold on to top talent. Like any youthful type, Gen Z is reckoning with working for “the man,” but our 27th 
edition of the Best Companies to Work For list, published with our partners at Great Place to Work, shows an emerging 
corporate equivalent of “the man in therapy.” Helping employees find meaning in their jobs, many of these best companies 
offer wellness benefits and a commitment to their workforce looking as diverse as the nation’s population. 
In practice, creating a more empathetic workplace looks like staying loyal to workers, emphasizing the needs of individuals
 with diversity and inclusion initiatives, and, naturally, paying employees well.
 """
st.write(comment)

st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])


