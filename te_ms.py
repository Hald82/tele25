from pyrogram import Client, filters

# Replace these with your API details
api_id = "13824135"
api_hash = "72c39aa03a40bdd005c12a3926196282"
session_name = "text"

# Replace with your target group ID
target_group_id = -1002059552508  # Example: -100XXXXXXXXXX for groups

# Create a Pyrogram client
app = Client(session_name, api_id=api_id, api_hash=api_hash)

@app.on_message(filters.private & ~filters.service)
def forward_private_messages(client, message):
    """
    Forwards private messages to a Telegram group.
    """
    try:
        # Forward the message to the group
        message.forward(target_group_id)
        print(f"Forwarded message from {message.chat.id} to group {target_group_id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Bot is running. Listening for private messages...")

    # Run the Pyrogram client (this will keep listening for new messages)
    app.run()
