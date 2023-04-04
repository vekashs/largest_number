import streamlit as st

def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title("Find the Largest Number")
st.write("Enter three numbers below:")

a = st.number_input("First number")
b = st.number_input("Second number")
c = st.number_input("Third number")

if st.button("Find largest number"):
    result = largest_number(a, b, c)
    st.success(f"The largest number is {result}")
