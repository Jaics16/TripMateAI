
import gradio as gr
from llm import chat_with_gemini


# ============================================================
# TRIPMATEAI — PROFESSIONAL KERALA TRAVEL ASSISTANT
# Gradio 6.x
# Existing Gemini backend is preserved.
# ============================================================


CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --forest: #073f32;
    --forest-light: #0b5a45;
    --mint: #e5f4e9;
    --gold: #d4aa55;
    --ink: #152820;
    --muted: #718078;
    --paper: #f7f8f3;
}

.gradio-container {
    max-width: 1440px !important;
    margin: auto !important;
    background: var(--paper) !important;
    font-family: 'DM Sans', sans-serif !important;
}

footer {
    display: none !important;
}

#topbar {
    background: white;
    border: 1px solid #e6ece5;
    border-radius: 18px;
    padding: 14px 22px;
    margin: 14px 0 18px;
    box-shadow: 0 8px 28px rgba(12,54,40,.05);
}

.brand-mark {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: var(--forest);
    color: white;
    font-size: 23px;
    margin-right: 10px;
}

.brand-name {
    color: var(--forest);
    font-size: 21px;
    font-weight: 800;
}

.brand-sub {
    color: #829087;
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.nav-pill {
    display: inline-block;
    padding: 9px 13px;
    border-radius: 999px;
    color: #52645b;
    font-size: 13px;
    font-weight: 700;
}

.nav-pill.active {
    background: #e6f5ec;
    color: var(--forest);
}

.hero {
    min-height: 340px;
    border-radius: 24px;
    overflow: hidden;
    padding: 42px 46px;
    color: white;
    background:
        linear-gradient(
            90deg,
            rgba(3,43,33,.91) 0%,
            rgba(4,58,42,.73) 46%,
            rgba(4,58,42,.10) 100%
        ),
        url('https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1800&q=85')
        center/cover;
    box-shadow: 0 18px 42px rgba(7,63,50,.16);
}

.hero-kicker {
    color: #bfe8d2;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2.5px;
    margin-bottom: 12px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(36px, 5vw, 58px);
    line-height: 1.04;
    margin: 0 0 13px;
    color: white;
}

.hero p {
    max-width: 560px;
    color: #e7f2ec;
    font-size: 16px;
    line-height: 1.7;
}

.hero-note {
    margin-top: 25px;
    color: #d9f0e2;
    font-size: 12px;
    font-weight: 700;
}

.section-heading {
    color: var(--ink);
    font-size: 23px;
    font-weight: 800;
}

.section-sub {
    color: var(--muted);
    font-size: 13px;
    margin-top: -7px;
}

.package-card {
    background: white;
    border: 1px solid #e8eee8;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(19,55,40,.055);
    height: 100%;
}

.package-image {
    height: 155px;
    background-size: cover;
    background-position: center;
}

.package-body {
    padding: 17px 18px 19px;
}

.package-tag {
    display: inline-block;
    background: #e7f5ec;
    color: #176047;
    border-radius: 999px;
    padding: 5px 9px;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
}

.package-card h3 {
    color: var(--ink);
    font-size: 17px;
    margin: 11px 0 5px;
}

.package-card p {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.55;
    min-height: 38px;
}

.package-meta {
    color: #75837b;
    font-size: 11px;
    margin-top: 8px;
}

.package-price {
    color: var(--forest);
    font-size: 20px;
    font-weight: 800;
    margin-top: 10px;
}

.package-price small {
    color: #89958e;
    font-size: 10px;
    font-weight: 500;
}

#chat-panel {
    background: white;
    border: 1px solid #e6ece5;
    border-radius: 20px;
    padding: 17px;
    box-shadow: 0 10px 30px rgba(12,54,40,.055);
}

#chat-title {
    color: var(--forest);
    font-size: 18px;
    font-weight: 800;
}

#chat-status {
    color: #78877e;
    font-size: 11px;
}

#chatbot {
    border: 0 !important;
    background: #fbfcfa !important;
    border-radius: 14px !important;
}

/* Chat input text visibility fix */
#msg-box textarea {
    border-radius: 14px !important;
    border: 1px solid #dce7de !important;
    background: #ffffff !important;
    color: #152820 !important;
    -webkit-text-fill-color: #152820 !important;
    font-size: 14px !important;
    caret-color: #073f32 !important;
}

/* Placeholder text */
#msg-box textarea::placeholder {
    color: #89968e !important;
    opacity: 1 !important;
}

/* Input focus */
#msg-box textarea:focus {
    border-color: #0b5a45 !important;
    box-shadow: 0 0 0 2px rgba(11,90,69,0.12) !important;
}

.primary-btn button {
    background: var(--forest) !important;
    color: white !important;
    border: 0 !important;
    border-radius: 13px !important;
    font-weight: 700 !important;
}

.secondary-btn button {
    background: #eaf5ee !important;
    color: var(--forest) !important;
    border: 1px solid #d8eadf !important;
    border-radius: 13px !important;
    font-weight: 700 !important;
}

.panel {
    background: white;
    border: 1px solid #e6ece5;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(19,55,40,.045);
}

.panel-title {
    color: var(--ink);
    font-size: 17px;
    font-weight: 800;
}

.panel-copy {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.6;
}

#footer-note {
    text-align: center;
    color: #89968e;
    font-size: 11px;
    padding: 18px 0 8px;
}

@media (max-width: 800px) {
    .hero {
        padding: 30px 24px;
        min-height: 300px;
    }

    #topbar {
        padding: 12px 14px;
    }

    .package-image {
        height: 135px;
    }
}
"""


# ============================================================
# WELCOME MESSAGE
# ============================================================

WELCOME_MESSAGE = """
Namaskaram! 🌴 Welcome to TripMateAI.

I'm your Kerala travel assistant.

I can help you with:

✅ Kerala travel packages
✅ Package details and destinations
✅ Travel price calculations
✅ Demonstration booking lookups
✅ Company information and policies

Where would you like to explore today?
"""


# ============================================================
# CHATBOT FUNCTION
# Existing Gemini integration is retained.
# ============================================================

def respond(message, history):

    if not message or not message.strip():
        return history, ""

    try:

        answer = chat_with_gemini(
            message=message.strip(),
            history=history
        )

        updated_history = list(history or [])

        updated_history.append({
            "role": "user",
            "content": message.strip()
        })

        updated_history.append({
            "role": "assistant",
            "content": str(answer)
        })

        return updated_history, ""

    except Exception as error:

        updated_history = list(history or [])

        updated_history.append({
            "role": "user",
            "content": message.strip()
        })

        updated_history.append({
            "role": "assistant",
            "content": (
                "Sorry! I couldn't process your request right now. "
                "Please try again.\n\n"
                f"Technical detail: {type(error).__name__}"
            )
        })

        return updated_history, ""


# ============================================================
# CLEAR CHAT
# ============================================================

def clear_chat():
    return [], WELCOME_MESSAGE


# ============================================================
# QUICK ACTION PROMPTS
# ============================================================

def explore_packages():
    return "Please show me all available Kerala travel packages."


def calculate_price():
    return "Help me calculate the total price for a travel package."


def booking_lookup():
    return "I want to look up a demonstration booking. What details do you need?"


def travel_policies():
    return "Please explain the company travel and cancellation policies."


# ============================================================
# GRADIO APPLICATION
# ============================================================

with gr.Blocks(
    title="TripMateAI | Explore Kerala"
) as demo:

    # --------------------------------------------------------
    # NAVIGATION BAR
    # --------------------------------------------------------

    with gr.Row(elem_id="topbar", equal_height=True):

        with gr.Column(scale=3):

            gr.HTML("""
            <div style="display:flex;align-items:center">

                <div class="brand-mark">🌴</div>

                <div>
                    <div class="brand-name">TripMateAI</div>

                    <div class="brand-sub">
                        Your Kerala Travel Companion
                    </div>
                </div>

            </div>
            """)

        with gr.Column(scale=2):

            gr.HTML("""
            <div style="display:flex;align-items:center;justify-content:flex-end;gap:8px">

                <span class="nav-pill active">Home</span>

                <span class="nav-pill">Travel Packages</span>

                <span class="nav-pill">About</span>

                <span class="nav-pill">Help</span>

            </div>
            """)

    # --------------------------------------------------------
    # HERO SECTION
    # --------------------------------------------------------

    gr.HTML("""
    <section class="hero">

        <div class="hero-kicker">
            Discover God's Own Country
        </div>

        <h1>
            Your next journey<br>
            starts in Kerala.
        </h1>

        <p>
            Find your perfect escape through misty mountains,
            peaceful backwaters and lush green landscapes —
            with a little help from your AI travel companion.
        </p>

        <div class="hero-note">
            ✦ Thoughtful trips · Local experiences · Friendly travel assistance
        </div>

    </section>
    """)

    # --------------------------------------------------------
    # MAIN CONTENT
    # --------------------------------------------------------

    with gr.Row(equal_height=False):

        # ----------------------------------------------------
        # LEFT SIDE: TRAVEL PACKAGES
        # ----------------------------------------------------

        with gr.Column(scale=7):

            gr.HTML("""
            <div style="margin:25px 0 15px">

                <div class="section-heading">
                    Explore Popular Getaways
                </div>

                <div class="section-sub">
                    Beautiful destinations to start planning your Kerala trip.
                </div>

            </div>
            """)

            with gr.Row():

                # MUNNAR

                gr.HTML("""
                <article class="package-card">

                    <div class="package-image"
                    style="
                    background-image:url(
                    'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=900&q=85'
                    )">
                    </div>

                    <div class="package-body">

                        <span class="package-tag">
                            Hill Station
                        </span>

                        <h3>
                            Munnar Hills Escape
                        </h3>

                        <p>
                            Tea gardens, misty mountains and scenic viewpoints.
                        </p>

                        <div class="package-meta">
                            ◷ 5 Days · 4 Nights
                        </div>

                        <div class="package-price">
                            ₹18,500
                            <small>/ adult · from</small>
                        </div>

                    </div>

                </article>
                """)

                # ALLEPPEY

                gr.HTML("""
                <article class="package-card">

                    <div class="package-image"
                    style="
                    background-image:url(
                    'https://images.unsplash.com/photo-1593693411515-c20261bcad6e?auto=format&fit=crop&w=900&q=85'
                    )">
                    </div>

                    <div class="package-body">

                        <span class="package-tag">
                            Backwaters
                        </span>

                        <h3>
                            Alleppey Backwater Break
                        </h3>

                        <p>
                            Relax aboard a houseboat along peaceful waterways.
                        </p>

                        <div class="package-meta">
                            ◷ 3 Days · 2 Nights
                        </div>

                        <div class="package-price">
                            ₹12,500
                            <small>/ adult · from</small>
                        </div>

                    </div>

                </article>
                """)

                # WAYANAD

                gr.HTML("""
                <article class="package-card">

                    <div class="package-image"
                    style="
                    background-image:url(
                    'https://images.unsplash.com/photo-1511497584788-876760111969?auto=format&fit=crop&w=900&q=85'
                    )">
                    </div>

                    <div class="package-body">

                        <span class="package-tag">
                            Nature & Adventure
                        </span>

                        <h3>
                            Wayanad Nature Trail
                        </h3>

                        <p>
                            Discover forest trails, waterfalls and green hills.
                        </p>

                        <div class="package-meta">
                            ◷ 4 Days · 3 Nights
                        </div>

                        <div class="package-price">
                            ₹15,000
                            <small>/ adult · from</small>
                        </div>

                    </div>

                </article>
                """)

            # INFORMATION PANEL

            gr.HTML("""
            <div class="panel" style="margin-top:18px">

                <div class="panel-title">
                    A Better Way to Plan Your Trip
                </div>

                <div class="panel-copy">
                    Ask TripMateAI about package inclusions,
                    child pricing, estimated totals, demonstration
                    booking records, and company travel policies.

                    Your AI assistant uses the project's connected
                    information and tools.
                </div>

            </div>
            """)

        # ----------------------------------------------------
        # RIGHT SIDE: AI CHATBOT
        # ----------------------------------------------------

        with gr.Column(
            scale=5,
            elem_id="chat-panel"
        ):

            gr.HTML("""
            <div style="display:flex;align-items:center;gap:11px;margin-bottom:12px">

                <div style="
                    width:42px;
                    height:42px;
                    border-radius:50%;
                    background:#e5f4e9;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:22px;
                ">
                    🌿
                </div>

                <div>

                    <div id="chat-title">
                        TripMateAI Assistant
                    </div>

                    <div id="chat-status">
                        ● Ready to help with your Kerala trip
                    </div>

                </div>

            </div>
            """)

            
            chatbot = gr.Chatbot(
                value=[
                    {
                        "role": "assistant",
                        "content": WELCOME_MESSAGE
                    }
                ],
                height=390,
               show_label=False,
                elem_id="chatbot"
            )

            # MESSAGE INPUT

            with gr.Row():

                msg = gr.Textbox(
                    placeholder="Ask me about Kerala travel...",
                    show_label=False,
                    lines=1,
                    max_lines=4,
                    scale=8,
                    elem_id="msg-box"
                )

                send = gr.Button(
                    "Send ➤",
                    scale=2,
                    elem_classes="primary-btn"
                )

            # QUICK ACTIONS

            with gr.Row():

                packages_btn = gr.Button(
                    "Explore Packages",
                    size="sm",
                    elem_classes="secondary-btn"
                )

                price_btn = gr.Button(
                    "Calculate Price",
                    size="sm",
                    elem_classes="secondary-btn"
                )

            with gr.Row():

                booking_btn = gr.Button(
                    "Demo Booking Lookup",
                    size="sm",
                    elem_classes="secondary-btn"
                )

                policy_btn = gr.Button(
                    "Travel Policies",
                    size="sm",
                    elem_classes="secondary-btn"
                )

            clear_btn = gr.Button(
                "Clear Conversation",
                size="sm",
                variant="secondary"
            )

    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    gr.HTML("""
    <div id="footer-note">

        TripMateAI · Kerala Travel Assistance · Demonstration Project

        <br>

        Package information and booking lookups are for demonstration.
        No live booking or payment is processed.

    </div>
    """)

    # ========================================================
    # EVENT HANDLERS
    # ========================================================

    # Send button

    send.click(
        fn=respond,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    # Enter key

    msg.submit(
        fn=respond,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    # Clear conversation

    clear_btn.click(
        fn=clear_chat,
        outputs=[chatbot, msg]
    )

    # Quick actions

    packages_btn.click(
        fn=explore_packages,
        outputs=msg
    )

    price_btn.click(
        fn=calculate_price,
        outputs=msg
    )

    booking_btn.click(
        fn=booking_lookup,
        outputs=msg
    )

    policy_btn.click(
        fn=travel_policies,
        outputs=msg
    )


# ============================================================
# LAUNCH APPLICATION
# ============================================================

if __name__ == "__main__":

     demo.launch(
    theme=gr.themes.Soft(
        primary_hue="emerald",
        secondary_hue="green",
        neutral_hue="slate"
    ),
    css=CUSTOM_CSS,
    inbrowser=True
)
