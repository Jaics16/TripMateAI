
import gradio as gr
from llm import chat_with_gemini

# ----------------------------------
# TripMateAI - Dark Chat Interface
# ----------------------------------

CUSTOM_CSS = """
body, .gradio-container {
    background: #10131c !important;
    color: #f1f5f9 !important;
}

.gradio-container {
    max-width: 1100px !important;
    margin: auto !important;
}

#main-header {
    text-align: center;
    padding: 28px 10px 18px;
}

#main-header h1 {
    color: #5eead4;
    font-size: 38px;
    margin-bottom: 5px;
}

#main-header p {
    color: #aab5c5;
    font-size: 15px;
}

#chatbot {
    border: 1px solid #30394b !important;
    border-radius: 16px !important;
}

button {
    border-radius: 10px !important;
}

#footer {
    text-align: center;
    color: #8491a5;
    font-size: 12px;
    padding: 20px;
}
"""

WELCOME_MESSAGE = """
Namaskaram! Welcome to **TripMateAI** 🌴

I'm your Kerala travel assistant. I can help you with:

- 🏞️ Kerala travel packages
- 🏡 Package details and destinations
- 💰 Travel price calculations
- 📋 Demonstration booking lookups
- ℹ️ Company information and policies

Where would you like to explore today?
"""


def respond(message, history):
    """Send the user's message to the existing Gemini chatbot."""

    if not message or not message.strip():
        return "", history

    try:
        reply = chat_with_gemini(
            message=message.strip(),
            history=history
        )

        if not reply:
            reply = "Sorry, I couldn't generate a response. Please try again."

        return "", history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": reply}
        ]

    except Exception as error:
        print(f"Gradio error: {error}")

        error_message = (
            "Sorry, something went wrong while processing your request. "
            "Please try again."
        )

        return "", history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": error_message}
        ]


def clear_chat():
    """Reset the conversation."""
    return [], WELCOME_MESSAGE


# ----------------------------------
# Build Gradio application
# ----------------------------------

with gr.Blocks(
    title="TripMateAI | Kerala Travel Assistant"
) as demo:

    gr.HTML("""
    <div id="main-header">
        <h1>🌴 TripMateAI</h1>
        <p>Your Intelligent Kerala Travel Companion</p>
        <p>Explore God's Own Country with confidence.</p>
    </div>
    """)

    chatbot = gr.Chatbot(
    value=[{"role": "assistant", "content": WELCOME_MESSAGE}],
    height=480,
    elem_id="chatbot",
    label="TripMateAI Assistant"
)

    with gr.Row():
        message = gr.Textbox(
            placeholder="Ask me about Kerala travel packages...",
            show_label=False,
            scale=8,
            lines=1,
            max_lines=4,
            container=False
        )

        send_button = gr.Button(
            "Send ➤",
            variant="primary",
            scale=1
        )

    gr.Markdown("### ✨ Suggested questions")

    with gr.Row():
        package_button = gr.Button("🏞️ View packages")
        price_button = gr.Button("💰 Calculate a price")
        booking_button = gr.Button("📋 Check a booking")

    with gr.Row():
        company_button = gr.Button("ℹ️ About TripMateAI")
        policy_button = gr.Button("📜 Cancellation policy")
        clear_button = gr.Button("🗑️ Clear chat")

    gr.HTML("""
    <div id="footer">
        TripMateAI Demo · Kerala, India · Powered by Gemini AI
        <br>
        Demonstration data only. No real bookings or payments are processed.
    </div>
    """)

    # Send message
    send_button.click(
        respond,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )

    message.submit(
        respond,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )

    # Suggested questions
    package_button.click(
        lambda: "What travel packages do you offer?",
        outputs=message
    )

    price_button.click(
        lambda: "Calculate the price for 2 adults and 1 child for KV001.",
        outputs=message
    )

    booking_button.click(
        lambda: "Check the booking details for KVB1001.",
        outputs=message
    )

    company_button.click(
        lambda: "What is TripMateAI, and what services does it provide?",
        outputs=message
    )

    policy_button.click(
        lambda: "What is your cancellation and refund policy?",
        outputs=message
    )

    # Clear conversation
    clear_button.click(
        clear_chat,
        outputs=[chatbot, message]
    )


if __name__ == "__main__":
    print("Starting TripMateAI web application...")

    demo.launch(
        theme=gr.themes.Base(
            primary_hue="teal",
            secondary_hue="slate",
            neutral_hue="slate"
        ),
        css=CUSTOM_CSS,
        inbrowser=True
    )