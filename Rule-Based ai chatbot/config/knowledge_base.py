BOT_NAME    = "ARIA"
BOT_VERSION = "1.0.0"
BOT_BATCH   = "2026"
BOT_ORG     = "DecodeLabs"

EXIT_KEYWORDS = {"exit", "quit", "q"}

FALLBACK = "Hmm, I don't know that yet. Type 'help' to see what I can do!"

RESPONSES = {

    # ---- GREETINGS ----
    "hello"               : f"Hey there! I'm {BOT_NAME}, {BOT_ORG}'s AI Assistant. How can I help?",
    "hi"                  : "Hi! Great to see you. What would you like to know?",
    "hey"                 : "Hey! I'm online and ready. Ask me anything!",
    "good morning"        : "Good morning! Hope you're having a great day. How can I help?",
    "good evening"        : "Good evening! Ready to chat. What's on your mind?",

    # ---- BOT IDENTITY ----
    "who are you"         : f"I'm {BOT_NAME} — Automated Rule-based Intelligence Assistant, built at {BOT_ORG}.",
    "what is your name"   : f"My name is {BOT_NAME}. I was coded by a {BOT_ORG} AI Engineering Intern!",
    "who made you"        : f"I was built by an AI Engineer Intern at {BOT_ORG}, Batch {BOT_BATCH}.",
    "what are you"        : "I'm a Rule-Based AI Chatbot — I respond using logic and predefined rules, not machine learning.",
    "are you a bot"       : "Yes! I'm a bot. Specifically, a deterministic rule-based chatbot. No guessing — pure logic.",
    "are you human"       : "Nope! I'm a program. But I'm designed to have a helpful conversation.",
    "are you ai"          : "I'm a simple form of AI — rule-based intelligence. No neural networks, just pure logic!",

    # ---- AI KNOWLEDGE ----
    "what is ai"          : "AI (Artificial Intelligence) is the simulation of human intelligence by machines using logic, data, and algorithms.",
    "what is ml"          : "ML (Machine Learning) is a subset of AI where systems learn patterns from data automatically — unlike me, I use explicit rules!",
    "what is machine learning" : "Machine Learning lets computers learn from examples instead of being explicitly programmed. It's the next step after rule-based AI!",
    "what is deep learning"    : "Deep Learning uses multi-layered neural networks to learn complex patterns — used in image recognition, language models, etc.",
    "what is nlp"              : "NLP (Natural Language Processing) is AI's ability to understand and process human language — like what powers advanced chatbots!",
    "what is a chatbot"        : "A chatbot is a program that simulates conversation. I'm rule-based. Others (like ChatGPT) use large language models.",
    "difference between ai and ml" : "AI is the broad concept of smart machines. ML is one technique to achieve AI — where machines learn from data instead of rules.",
    "what is a neural network"     : "A neural network mimics the human brain — layers of nodes process input and learn patterns through training on data.",
    "what is an llm"               : "LLM (Large Language Model) is a type of AI trained on massive text data to understand and generate human language. Example: GPT-4.",

    # ---- DECODELABS INFO ----
    "what is decodelabs"  : f"{BOT_ORG} is a tech training organization that gives hands-on real-world AI & software engineering experience to interns.",
    "what is project 1"   : "Project 1 is the Rule-Based AI Chatbot — the foundation milestone of the DecodeLabs AI Engineering track.",
    "what is project 2"   : "Project 2 moves to Semantic Matching — instead of exact keywords, the bot understands meaning using word vectors!",

    # ---- HELP & NAVIGATION ----
    "help"                : "Ask me about: AI, ML, Deep Learning, NLP, LLMs, who I am, DecodeLabs, or just say hello! Type 'options' for full list.",
    "what can you do"     : f"I can answer questions about AI/ML concepts, tell you about {BOT_ORG}, crack a joke, and have a basic conversation!",
    "options"             : "Try: hello / what is ai / what is ml / what is nlp / who are you / what is decodelabs / joke / bye",
    "commands"            : "Commands: 'help' → guidance | 'options' → full list | 'joke' → humor | 'exit' or 'quit' → stop the bot",

    # ---- FUN ----
    "joke"                : "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "another joke"        : "Why did the AI go to school? To improve its learning rate! 😄",
    "tell me a joke"      : "A SQL query walks into a bar, walks up to two tables and asks... 'Can I JOIN you?' 😂",
    "are you smart"       : "I'm rule-based smart — I only know what I've been taught. Ask me about AI though!",
    "do you think"        : "I process inputs and return outputs. Whether that counts as thinking is a great philosophical question!",
    "what is your purpose": f"My purpose is to demonstrate rule-based AI logic — and to be a helpful assistant at {BOT_ORG}!",

    # ---- FAREWELLS ----
    "bye"                 : "Goodbye! It was great chatting with you. Come back anytime!",
    "goodbye"             : "See you later! Keep learning and building. 🚀",
    "see you"             : "See you soon! Remember — every rule you define brings you closer to mastering AI.",
    "thanks"              : "You're welcome! Always happy to help. 😊",
    "thank you"           : "Anytime! That's what I'm here for.",
    "ok"                  : "Alright! Anything else you'd like to know?",
    "okay"                : "Okay! Feel free to ask me anything else.",
}