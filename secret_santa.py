import streamlit as st
import random
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SessionState(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

def create_message(to_name, from_name, budget, date, location):
    message = f"""
    Subject: 🎅 Your Secret Santa Assignment 🎁

    Dear {to_name},

    Ho ho ho! 🎅 The holiday season is upon us and it's time for our Secret Santa gift exchange!

    You have been chosen to be the Secret Santa for: {from_name}. Remember, the identity of your giftee is a secret, so let's keep the mystery alive!

    Here are some details to keep in mind:
    - Budget: {budget} 
    - Gift Exchange Date: {date} (may change it to a different date if everyone agrees)
    - Location: {location} (may change it to a different location if everyone agrees)

    Remember, it's not about the price tag but the thought that counts. Let's spread joy, laughter, and the holiday spirit!

    Happy gifting and may your holidays be filled with joy and surprises!

    Best wishes,
    Dummy Secret Santa 🎅🎁
    """
    return message

def get_state(**kwargs):
    if 'session_state' not in st.session_state:
        st.session_state['session_state'] = SessionState(**kwargs)
    return st.session_state['session_state']

def send_email(to_name, to_email, from_name, budget, date, location):
    print(f"Sending email to {to_name}...")
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your@gmail.com', 'your_password')  # replace with your Gmail and password

    # Create the email
    msg = MIMEMultipart()
    message = create_message(to_name, from_name, budget, date, location)
    msg['From'] = 'your@gmail.com'  # replace with your Gmail
    msg['To'] = to_email
    msg['Subject'] = "Secret Santa"
    msg.attach(MIMEText(message, 'plain'))

    # Send the email
    server.send_message(msg)
    server.quit()

state = get_state(participants=[], pairs=[])

st.title('Secret Santa Generator')

# Input for common location, fixed budget, and date
common_location = st.text_input('Common Location', value='Location')
fixed_budget = st.text_input('Fixed Budget', value='Rs250')
exchange_date = st.text_input('Gift Exchange Date', value='December 25, 2023')

# CSV file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    for participant in data[['Name', 'Email ID']].values.tolist():
        if participant not in state.participants:
            state.participants.append(participant)
    st.write(data)

# Input for participant name and email
name = st.text_input('Name')
email = st.text_input('Email')

if st.button('Add Participant'):
    # Check if participant already exists
    if [name, email] not in state.participants:
        state.participants.append([name, email])
        st.success(f'Added {name}')
    else:
        st.error(f'{name} is already added')

# Display the list of participants in separate boxes and add a button to remove a participant
for i, participant in enumerate(state.participants):
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.write(participant[0])
    with col2:
        st.write(participant[1])
    with col3:
        if st.button(f'Remove {participant[0]}', key=f'Remove-{i}'):
            state.participants.remove(participant)
            st.success(f'Removed {participant[0]}')

if len(state.participants) >= 2:
    if st.button('Generate'):
        # Shuffle the list
        random.shuffle(state.participants)

        # Generate pairs
        state.pairs = [(state.participants[i], state.participants[(i+1)%len(state.participants)]) for i in range(len(state.participants))]

        # Display pairs in a visually appealing way
        st.markdown("## 🎅 Secret Santa Pairs 🎁")
        for pair in state.pairs:
            st.markdown(f"🎁 <span style='color:LightSalmon;'>{pair[0][0]}</span> is the Secret Santa for <span style='color:LightSalmon;'>{pair[1][0]}</span> 🎄", unsafe_allow_html=True)
        print("Thank you for using Secret Santa Generator! 🎅")
        st.markdown("Thank you for using Secret Santa Generator! 🎅")

    if state.pairs and st.button('Send Emails'):
        # Send emails
        for pair in state.pairs:
            to_name, to_email = pair[0]
            from_name, from_email = pair[1]
            send_email(to_name, to_email, from_name, fixed_budget, exchange_date, common_location)
            st.success(f'Email sent to {to_name}')
        st.success("Merry Christmas! 🎄🎅🎁")
else:
    st.error('Please add more participants.')

# Create a sample DataFrame
data = {
    'Name': ['John Doe', 'Jane Smith', 'Mike Johnson'],
    'Email ID': ['john@example.com', 'jane@example.com', 'mike@example.com']
}
df = pd.DataFrame(data)

# Convert DataFrame to CSV
csv = df.to_csv(index=False)

# Create a download button
st.download_button(
    label="Download example CSV",
    data=csv,
    file_name="example.csv",
    mime="text/csv"
)
