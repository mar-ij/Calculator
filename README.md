import streamlit as st
# Streamlit App Title
st.title("🧮 Simple Streamlit Calculator")

# Taking input from the user
a = st.number_input("Enter your first number:", value=0)
b = st.number_input("Enter your second number:", value=0)

# Selecting operation
operation = st.selectbox("Choose your operation:", ["/", "*", "+", "-", "**", "//", "%"])

# Calculate Button
if st.button("Calculate"):
    if operation == "/" and b == 0:
        st.error("❌ Error: Division by zero is not allowed.")
    elif operation == "//" and b == 0:
        st.error("❌ Error: Integer division by zero is not allowed.")
    elif operation == "%" and b == 0:
        st.error("❌ Error: Modulo by zero is not allowed.")
    else:
        result = None
        if operation == "/":
            result = a / b
        elif operation == "*":
            result = a * b
        elif operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "**":
            result = a ** b
        elif operation == "//":
            result = a // b
        elif operation == "%":
            result = a % b

        st.success(f"✅ Result: {result}")
