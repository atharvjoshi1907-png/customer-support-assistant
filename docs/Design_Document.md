Project: Sentiment-Aware Customer Support Assistant1. 
1.System Architecture Overview
->The application follows a decoupled, monolithic full-stack architecture optimized for local deployment. The frontend handles user interaction and metrics visualization, while the backend manages model selection and inference execution.  
            ┌────────────────────────────────────────────────────────┐
            │                   Streamlit Frontend                   │
            │  ┌───────────────────┐ ┌────────────────────────────┐  │
            │  │  Inference Views  │ │     Plotly Dashboard       │  │
            │  └─────────┬─────────┘ └──────────────▲─────────────┘  │
            └────────────│──────────────────────────│────────────────┘
                        │ HTTP POST (Payload)      │ HTTP GET (JSON)
                        ▼                          │
            ┌────────────│──────────────────────────│────────────────┐
            │            ▼      Flask API Backend   │                │
            │   ┌─────────────────┐        ┌────────┴─────────┐      │
            │   │ /generate Route │        │  /metrics Route  │      │
            │   └────────┬────────┘        └────────▲─────────┘      │
            │            ▼                          │                │
            │   ┌─────────────────┐                 │                │
            │   │ ModelController │                 │                │
            │   └────────┬────────┘                 │                │
            └────────────│──────────────────────────│────────────────┘
                        ▼                          │
            ┌────────────▼──────────────────────────┴────────────────┐
            │                    Storage & Models                    │
            │   ┌───────────────────────────────────────────────┐    │
            │   │ saved_models/ (Weights: Baseline, LoRA, etc.) │    │
            │   └───────────────────────────────────────────────┘    │
            │   ┌───────────────────────────────────────────────┐    │
            │   │ metrics/metrics.json                          │    │
            │   └───────────────────────────────────────────────┘    │
            └────────────────────────────────────────────────────────┘
2. Backend API Design (Flask)
->The backend service runs a local web server (defaulting to http://127.0.0.1:5000) and provides two primary operational endpoints.  
->2.1 Endpoint: Generate Response
    ->URL: /generate
    ->Method: POST
    ->Headers: Content-Type: application/json
    ->Request Body:
    {
    "message": "The text containing the customer's issue or complaint.",
    "technique": "Baseline | LoRA | QLoRA | Prompt Tuning"
    }
Success Response (200 OK):JSON{
  "customer_message": "The text containing the customer's issue or complaint.",
  "technique_used": "LoRA",
  "generated_reply": "The fine-tuned model draft response text."
}
2.2 Endpoint: Fetch MetricsURL: /metricsMethod: GETSuccess Response (200 OK): Reads directly from metrics/metrics.json.  JSON{
  "techniques": [
    {
      "name": "LoRA",
      "trainable_parameters": 4200000,
      "training_time_mins": 18,
      "peak_memory_gb": 7.4,
      "final_val_loss": 1.15,
      "bleu_score": 0.45
    }
  ]
}
3. Frontend Multi-Page Layout (Streamlit)The web client uses Streamlit's multi-page setup to separate operations into modular interfaces.  Home / Dashboard (dashboard.py): The main entry hub explaining the project scope, model choices (e.g., Qwen2.5-0.5B or TinyLlama-1.1B), and instructions.  Page 1: 📊 Metrics Dashboard (01_Metrics_Dashboard.py): * Parses data from /metrics.  Renders grouped bar charts using Plotly to compare training parameters, time, VRAM limits, and BLEU scores across methods.  Page 2: 📨 Reply Generator (02_Reply_Generator.py):Provides a st.text_area for inputting customer text.  Features a dropdown selector (st.selectbox) to switch the fine-tuning architecture technique.Sends a request to /generate and outputs the single drafted reply inside a clean callout box.  Page 3: 🔍 Comparison View (03_Comparison_View.py):Takes a single customer text input.  Programmatically hits the backend iteratively for all techniques.  Renders responses side-by-side using layout columns (st.columns) for direct manual comparison.  4. Model & Data Management4.1 Model Execution StrategyCloud Training Workspace: Training notebooks (notebooks/) leverage free-tier instances (Google Colab/Kaggle) to run Parameter-Efficient Fine-Tuning (PEFT) configurations via Hugging Face libraries.  Local Inference Drop: Only weights, adapters, or model artifacts are saved and transferred to the backend/saved_models/ directory.CPU Execution: backend/model.py initializes the base model using local resources, dynamically swapping tiny adapter heads (PEFT/LoRA matrices) based on client request parameters.  4.2 Local Storage Configurationmetrics/metrics.json: Serves as the single source of truth for downstream analysis graphs. Data is structured manually or script-dumped exactly once after all cloud training runs conclude. 