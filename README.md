# 🌍 Multi-Model AI Travel Agent

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![LangChain](https://img.shields.io/badge/FrameWork-LangChain-green.svg)
![Chainlit](https://img.shields.io/badge/UI-Chainlit-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A professional-grade, agentic system designed to plan high-fidelity travel itineraries. This project utilizes a **Sandwich Architecture**—a strategic design pattern that combines structured planning with dynamic tool execution to provide reliable, grounded, and enthusiastic travel advice.

---


## 🛠️ Tech Stack & Layers

| Component | Technology | Role in Project |
|:---|:---|:---|
| **Frontend/UI** | **Chainlit** | Handles real-time task streaming, CoT display, and user session management. |
| **Orchestration** | **LangChain** | [cite_start]Manages `PromptTemplates` and structures LLM outputs into official `ChatResult` objects[cite: 1, 2]. |
| **Routing** | **LiteLLM** | [cite_start]Implements a `simple-shuffle` strategy with `num_retries=3` for high availability[cite: 2]. |
| **Search Engine** | **Tavily AI** | [cite_start]A specialized search engine optimized for LLMs to get clean travel data[cite: 1, 4]. |
| **Smart Model** | **Gemini 2.5 Flash** | [cite_start]Used for the "Brain" (Planner) and "Synthesis" (Refiner) layers[cite: 1, 2]. |
| **Fast Model** | **Llama-3.3-70b** | [cite_start]Utilized for rapid processing and classification tasks[cite: 1, 2]. |

---

## 🥪 The Sandwich Architecture
This agent operates using a three-layered logic to ensure every response is researched and synthesized professionally.

### 1. The Top Layer: Planner (The Brain)
* [cite_start]**Action**: Analyzes the user's intent and generates a structured search strategy[cite: 3].
* [cite_start]**Logic**: It breaks down the request into specific goals: finding flights, sourcing hotels within budget, and identifying local attractions[cite: 4].
* [cite_start]**Model**: Powered by the **Smart Tier** (Gemini)[cite: 1, 2].

### 2. The Filling: Executor (The Muscle)
* [cite_start]**Action**: Performs the heavy lifting by interacting with the `search_travel` tool[cite: 3].
* [cite_start]**Logic**: Fetches live flight names, prices, hotel ratings, and the top 3 local attractions[cite: 1].
* [cite_start]**Function**: Acts as the bridge between the AI's plan and real-time travel data[cite: 3].

### 3. The Bottom Layer: Refiner (The Consultant)
* [cite_start]**Action**: Synthesizes the raw research into a polished, day-by-day itinerary[cite: 3].
* [cite_start]**Persona**: Operates under the **"Global Wanderer"** identity[cite: 5].
* [cite_start]**Constraint**: Explicitly identifies as a multi-model travel system rather than a general-purpose AI[cite: 6, 7].

---

## 🔗 Key Technical Implementation
* [cite_start]**Custom LLM Integration**: The project extends LangChain’s `BaseChatModel` to create a custom `TravelLLM` class, allowing LiteLLM to behave as a native LangChain object[cite: 2].
* [cite_start]**Prompt Engineering**: Specialized system prompts (`planner.txt`, `executor.txt`, `refiner.txt`) ensure high-quality, grounded outputs[cite: 1, 3].
* [cite_start]**UI Customization**: Uses `cl.author_rename` to ensure all system steps are branded under the "Multi-Modal Travel Agent" name[cite: 3].

---


## 📸 Screenshots

<img width="1470" height="801" alt="Screenshot 2026-02-08 at 6 03 08 PM" src="https://github.com/user-attachments/assets/982446e4-c3ad-44bf-bd93-6d7fd9b46f80" />
<img width="1470" height="799" alt="Screenshot 2026-02-08 at 6 03 32 PM" src="https://github.com/user-attachments/assets/2d29e1ec-1000-4e59-bbb9-bb44fc34a730" />
<img width="1466" height="798" alt="Screenshot 2026-02-08 at 6 03 43 PM" src="https://github.com/user-attachments/assets/391eeb44-2cde-4e39-aeb9-e144cfa9e922" />
<img width="1469" height="796" alt="Screenshot 2026-02-08 at 6 03 57 PM" src="https://github.com/user-attachments/assets/72c2341d-4420-4332-9d4c-9d2b0df35e49" />
<img width="1470" height="800" alt="Screenshot 2026-02-08 at 6 04 07 PM" src="https://github.com/user-attachments/assets/91f19cd3-573a-4bca-85fa-242af6238c2d" />
<img width="1470" height="800" alt="Screenshot 2026-02-08 at 6 04 30 PM" src="https://github.com/user-attachments/assets/b7d59818-8b7f-4b2c-b2b0-77b87cd7ed78" />
<img width="1470" height="798" alt="Screenshot 2026-02-08 at 6 04 47 PM" src="https://github.com/user-attachments/assets/d7aff5ef-64d4-429c-b521-ce7050dbb729" />
<img width="1470" height="801" alt="Screenshot 2026-02-08 at 6 04 57 PM" src="https://github.com/user-attachments/assets/f3705a60-a2b6-497c-9642-49217be77383" />
<img width="1468" height="802" alt="Screenshot 2026-02-08 at 6 05 07 PM" src="https://github.com/user-attachments/assets/8810f557-b3cc-4409-90c0-b5f562034650" />
<img width="1470" height="802" alt="Screenshot 2026-02-08 at 6 05 19 PM" src="https://github.com/user-attachments/assets/b53366e1-8f16-485a-b16d-12c6681e9782" />










---

## 🚀 Getting Started

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/your-username/multi-model-travel-agent.git](https://github.com/your-username/multi-model-travel-agent.git)
    cd multi-model-travel-agent
    ```

2.  **Set Up Environment**:
    Create a `.env` file and add your keys:
    ```env
    GEMINI_KEY_1=your_key
    GROQ_KEY_1=your_key
    TAVILY_API_KEY=your_key
    ```

3.  **Launch**:
    ```bash
    chainlit run main.py -w
    ```


