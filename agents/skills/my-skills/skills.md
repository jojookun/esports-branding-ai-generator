# Prompt Blueprint: AI-Powered eSports Branding & Visual Concept Generator

**Context for AI Assistant:**
I am participating in the "July Challenge: Reimagine Creative Industries with AI". My goal is to build an AI-powered tool that transforms how creative work is imagined and produced in the eSports industry. 

**Project Vision:**
An AI-powered creative assistant specifically designed for eSports teams, content creators, and competitive gamers (e.g., Honor of Kings, osu!mania). It takes a user's "vibe" or prompt and automatically generates a comprehensive visual identity concept.

**Core Requirements (Challenge Rules):**
- **Primary Development Tool:** IBM Bob.
- **Core Component:** Artificial Intelligence (using IBM Granite or similar via watsonx).
- **Deliverables to prepare for:** A working prototype, a public GitHub repo with a detailed README, and a 3-minute demo video.

**Technical Stack & Preferences:**
- **Backend:** Python.
- **AI Integration:** IBM Granite (via API / LangChain).
- **Design Elements:** Output should include recommendations for gradient color palettes, typography pairings (e.g., combining aggressive eSports headers with clean modern fonts like Quicksand), and text-masking layout concepts for stream overlays.

**Your Tasks (Execute sequentially):**

1.  **Project Initialization:** 
    - Generate the foundational Python project structure for this backend.
    - Create a `requirements.txt` including necessary libraries (e.g., `requests`, `langchain`, `flask` atau `fastapi` untuk API sederhana).

2.  **AI Prompt Engineering Logic:**
    - Write a Python function that constructs the system prompt for the AI model. The prompt must instruct the model to act as an expert eSports art director and output structured JSON containing:
      - `theme_name`: A catchy name for the branding concept.
      - `color_palette`: 4-5 hex codes (specifically tailored for gradient use).
      - `typography`: Font recommendations (e.g., Primary display font + Secondary font like Quicksand).
      - `layout_guidelines`: Specific concepts for streaming overlays and social media banners.

3.  **API Integration Mockup:**
    - Provide a sample Python script demonstrating how to send the constructed prompt to an LLM endpoint and parse the JSON response.

4.  **GitHub README Drafting:**
    - Draft a comprehensive `README.md` that fulfills the challenge submission requirements:
      - Problem statement.
      - Solution description.
      - AI approach and architecture.
      - Selected challenge theme ("Reimagine Creative Industries with AI").
      - How IBM Bob was/will be used in the development process.
