1. Introduction
->1.1 Purpose
    This document outlines the software requirements for the Sentiment-Aware Customer Support Assistant. The system acts as an internal tool for customer support teams to automatically draft high-quality, appropriately toned responses to customer inquiries, complaints, and requests.

->1.2 ScopeThe application includes:
    ->A localized backend API that runs a collection of small language models (SLMs) optimized through various fine-tuning methods.
    ->A multi-page web UI serving as the agent workspace and comparative analytics dashboard.

2. General Description
->2.1 Product Perspective
    The system operates as a lightweight, full-stack application. Model training is executed externally on cloud tiers (Google Colab/Kaggle), while the finalized model configurations and application endpoints run within a decoupled local Python environment.
            [ Streamlit Frontend ] 
                │      ▲
        requests │      │ JSON
                ▼      │
            [ Flask Backend ] ◄───► [ metrics.json ]
                │
                ▼
        [ Fine-Tuned SLM Adapters ]
        (Baseline / LoRA / QLoRA)

->2.2 User Class and CharacteristicsCustomer Support Agent: 
    ->The primary user who inputs customer messages to receive optimized, fast response drafts.  
    ->Engineering Reviewers / Stakeholders: Users who view the metrics dashboard to evaluate training efficiency and system validity.

3. Functional Requirements
->3.1 Core Inference Engine
    FR-1.1: The system must accept user text input simulating a customer query.
    FR-1.2: The backend must support switching between a baseline model and multiple fine-tuning adapters (LoRA, QLoRA, Prompt Tuning) to generate replies.
    FR-1.3: The system must display generated text outputs side-by-side in a dedicated comparison view. 

->3.2 Evaluation & Analytics Dashboard
    FR-2.1: The system must read statistical data directly from a static metrics.json file.  
    FR-2.2: The UI must visually chart performance differences, specifically:
        Number of Trainable Parameters   
        Training Time (Minutes)   
        Peak VRAM Memory Used   
        Evaluation Metrics (Validation Loss, BLEU score)

4. Non-Functional Requirements
->4.1 Performance & Hardware Constraints
    ->The application inference must be lightweight enough to run entirely on a standard consumer CPU without specialized institutional    GPU dependencies.  
    ->The backend API response time for generating replies should ideally stay within a reasonable, interactive window for smooth web dashboard rendering.

->4.2 Design Constraints
    ->Backend Framework: Flask.  
    ->Frontend UI Framework: Streamlit.  
    ->Data Transmission: HTTP requests using JSON payloads.  