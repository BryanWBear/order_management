import streamlit as st
import pandas as pd

with st.form('order_form'):
    st.text_input('Order Number')
    st.text_input('Order Date')

    st.write('Select Order Type')
    order_type_df = pd.DataFrame(
        [
            {'Paid': False, 'Needs Shipping': False, 'Canceled': False, 'New Order': False, 'Reorder': False, 'Rush Order': False},
        ]
    )

    edited_order_df = st.data_editor(order_type_df)

    st.text_input('Customer Name')
    st.text_input('Email')
    st.text_input('Mailing Address')
    st.text_input('Phone Number')
    st.text_input('Company Name')

    st.header('Order Details')

    df = pd.DataFrame(
        [
            {'Item Description (Location, Size, Font, Thread Colors)': '', 'Size': '', 'Quantity': '', 'Unit Cost': ''},
            {'Item Description (Location, Size, Font, Thread Colors)': '', 'Size': '', 'Quantity': '', 'Unit Cost': ''},
            {'Item Description (Location, Size, Font, Thread Colors)': '', 'Size': '', 'Quantity': '', 'Unit Cost': ''},
        ]
    )

    st.data_editor(df, num_rows='dynamic')

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write('Submitted!')