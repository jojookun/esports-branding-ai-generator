# 🚀 Setup and Testing Guide

Complete step-by-step instructions for running and testing the AI-Powered eSports Branding Generator locally.

---

## 📋 Prerequisites

Before starting, ensure you have:
- ✅ Python 3.9 or higher installed
- ✅ Git installed (for cloning/version control)
- ✅ IBM watsonx.ai account with API credentials
- ✅ Terminal/Command Prompt access

---

## 🔧 Step 1: Create Python Virtual Environment

### Windows (PowerShell)
```powershell
# Navigate to project directory
cd "Reimagine Creative Industries with AI - AI-Powered eSports Branding & Visual Concept Generator"

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Windows (Command Prompt)
```cmd
cd "Reimagine Creative Industries with AI - AI-Powered eSports Branding & Visual Concept Generator"
python -m venv venv
venv\Scripts\activate.bat
```

### macOS/Linux
```bash
cd "Reimagine Creative Industries with AI - AI-Powered eSports Branding & Visual Concept Generator"
python3 -m venv venv
source venv/bin/activate
```

**Verification**: Your terminal prompt should now show `(venv)` at the beginning.

---

## 📦 Step 2: Install Dependencies

With the virtual environment activated:

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

**Expected output**: Installation of ~20 packages including FastAPI, LangChain, IBM watsonx-ai, etc.

**Troubleshooting**:
- If installation fails, try: `pip install -r requirements.txt --no-cache-dir`
- For Windows SSL errors: `pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt`

---

## 🔑 Step 3: Configure Environment Variables

### 3.1 Create .env File

Copy the template and create your configuration file:

**Windows (PowerShell)**:
```powershell
Copy-Item .env.template .env
```

**Windows (Command Prompt)**:
```cmd
copy .env.template .env
```

**macOS/Linux**:
```bash
cp .env.template .env
```

### 3.2 Get IBM watsonx Credentials

1. **Log in to IBM Cloud**: https://cloud.ibm.com/
2. **Navigate to watsonx.ai**: https://dataplatform.cloud.ibm.com/wx/home
3. **Get API Key**:
   - Go to "Manage" → "Access (IAM)" → "API keys"
   - Click "Create" to generate a new API key
   - Copy the key immediately (you won't see it again)
4. **Get Project ID**:
   - In watsonx.ai, go to your project
   - Click on "Manage" tab
   - Copy the "Project ID" from the project details

### 3.3 Edit .env File

Open `.env` in your text editor and add your credentials:

```env
# IBM watsonx.ai Configuration
WATSONX_API_KEY=your_actual_api_key_here
WATSONX_PROJECT_ID=your_actual_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com

# IBM Granite Model Configuration
MODEL_ID=ibm/granite-13b-chat-v2
MODEL_TEMPERATURE=0.7
MODEL_MAX_TOKENS=2000

# Application Configuration
APP_NAME=eSports Branding Generator
APP_VERSION=1.0.0
DEBUG_MODE=false

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
```

**Important**: 
- Replace `your_actual_api_key_here` with your IBM Cloud API key
- Replace `your_actual_project_id_here` with your watsonx project ID
- Keep the quotes if your values contain spaces

---

## 🎮 Step 4: Run the Interactive Demo

### 4.1 Basic Demo Run

```bash
python examples/api_integration_demo.py
```

**What happens**:
1. Loads configuration from `.env`
2. Checks if watsonx credentials are valid
3. Offers two modes: Live API or Mock Data
4. Displays formatted branding concepts

### 4.2 Demo with Mock Data (No API Required)

If you want to test without API credentials:

```bash
# The demo will automatically use mock data if credentials are missing
python examples/api_integration_demo.py
# Select option 2 when prompted
```

**Expected Output**:
```
================================================================================
  eSports Branding Generator - API Integration Demo
================================================================================

Configuration:
  Model: ibm/granite-13b-chat-v2
  Temperature: 0.7
  Max Tokens: 2000
  watsonx URL: https://us-south.ml.cloud.ibm.com
  API Status: ✓ Configured

Options:
  1. Run with live API (requires IBM watsonx credentials)
  2. Run with mock data (demonstration mode)

Select option (1 or 2, default=2): 2

================================================================================
  DEMO MODE: Using Mock Data
================================================================================
⚠️  watsonx credentials not configured. Showing example output.

================================================================================
  BRANDING CONCEPT: Cyber Samurai
================================================================================

Color Palette:
  1. #FF0080 ██████████
  2. #00D9FF ██████████
  3. #9D00FF ██████████
  4. #FFD700 ██████████
  5. #1A1A2E ██████████

Typography:
  Primary Display: Rajdhani Bold (Sharp, angular, tech-inspired)
  Secondary Body:  Quicksand Regular (Smooth, modern, highly readable)

  Rationale:
  Rajdhani's geometric precision evokes cyberpunk aesthetics...
```

### 4.3 Test with Custom Prompts

For **osu!mania** streamer:
```bash
# Edit the demo script or use the API directly
# Example vibe: "Pastel kawaii aesthetic with soft gradients and playful energy"
# Game context: "osu!mania"
```

For **Honor of Kings** team:
```bash
# Example vibe: "Epic fantasy with mystical purple and gold accents"
# Game context: "Honor of Kings"
```

---

## 🌐 Step 5: Start the FastAPI Server

### 5.1 Start Development Server

```bash
# Start with auto-reload (recommended for development)
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output**:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 5.2 Access the API Documentation

Open your web browser and navigate to:

**Swagger UI (Interactive API Docs)**:
```
http://localhost:8000/docs
```

**ReDoc (Alternative Documentation)**:
```
http://localhost:8000/redoc
```

**Health Check Endpoint**:
```
http://localhost:8000/health
```

### 5.3 Test API Endpoints via Swagger UI

1. **Open**: http://localhost:8000/docs
2. **Expand** the `POST /generate` endpoint
3. **Click** "Try it out"
4. **Enter** request body:
```json
{
  "vibe": "Futuristic cyberpunk with neon accents for a competitive FPS team",
  "game_context": "Valorant"
}
```
5. **Click** "Execute"
6. **View** the generated branding concept in the response

---

## 🧪 Step 6: Test with cURL or Python

### Using cURL

**Windows (PowerShell)**:
```powershell
$body = @{
    vibe = "Dark fantasy aesthetic with gold highlights"
    game_context = "Honor of Kings"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/generate" -Method Post -Body $body -ContentType "application/json"
```

**macOS/Linux**:
```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "vibe": "Dark fantasy aesthetic with gold highlights",
    "game_context": "Honor of Kings"
  }'
```

### Using Python

Create a test script `test_api.py`:

```python
import requests
import json

# Test the API
response = requests.post(
    "http://localhost:8000/generate",
    json={
        "vibe": "Clean minimalist design with bold typography",
        "game_context": "osu!mania"
    }
)

result = response.json()

if result["success"]:
    concept = result["concept"]
    print(f"Theme: {concept['theme_name']}")
    print(f"Colors: {concept['color_palette']}")
    print(f"Primary Font: {concept['typography']['primary_display']}")
else:
    print(f"Error: {result['error']}")
```

Run it:
```bash
python test_api.py
```

---

## 🎯 Example Test Cases

### Test Case 1: Competitive FPS Team (Valorant)

**Vibe**: "Aggressive military tactical with red and black color scheme"  
**Game Context**: "Valorant"

**Expected Output**:
- Theme with tactical/military naming
- Red/black dominant color palette
- Bold, condensed fonts
- Overlay recommendations for competitive gameplay

### Test Case 2: Rhythm Game Streamer (osu!mania)

**Vibe**: "Pastel kawaii aesthetic with soft gradients and playful energy"  
**Game Context**: "osu!mania"

**Expected Output**:
- Playful, energetic theme name
- Pastel color palette (pinks, blues, purples)
- Rounded, friendly fonts
- Overlay recommendations for rhythm game streaming

### Test Case 3: MOBA Team (Honor of Kings)

**Vibe**: "Epic fantasy with mystical purple and gold accents"  
**Game Context**: "Honor of Kings"

**Expected Output**:
- Fantasy-inspired theme name
- Purple/gold color palette
- Elegant, regal fonts
- Overlay recommendations for MOBA gameplay

---

## 🔍 Verification Checklist

After setup, verify everything works:

- [ ] Virtual environment activated (shows `(venv)` in terminal)
- [ ] All dependencies installed without errors
- [ ] `.env` file created with valid credentials
- [ ] Demo script runs successfully
- [ ] FastAPI server starts without errors
- [ ] Swagger UI accessible at http://localhost:8000/docs
- [ ] Health check returns `{"status": "healthy"}`
- [ ] Can generate branding concepts via API

---

## 🐛 Troubleshooting

### Issue: "Module not found" errors
**Solution**: Ensure virtual environment is activated and dependencies are installed
```bash
pip list  # Check installed packages
pip install -r requirements.txt  # Reinstall if needed
```

### Issue: "watsonx configuration is incomplete"
**Solution**: Check your `.env` file has valid credentials
```bash
# Verify .env exists and has correct format
cat .env  # macOS/Linux
type .env  # Windows
```

### Issue: Port 8000 already in use
**Solution**: Use a different port
```bash
uvicorn src.main:app --reload --port 8001
```

### Issue: SSL/Certificate errors
**Solution**: Update certificates or use `--no-verify` (development only)
```bash
pip install --upgrade certifi
```

### Issue: Import errors with relative imports
**Solution**: Run from project root directory
```bash
# Make sure you're in the project root
cd "Reimagine Creative Industries with AI - AI-Powered eSports Branding & Visual Concept Generator"
python examples/api_integration_demo.py
```

---

## 📊 Performance Notes

- **First Request**: May take 10-15 seconds (model initialization)
- **Subsequent Requests**: 5-10 seconds (generation time)
- **Concurrent Requests**: FastAPI handles async operations efficiently
- **Rate Limiting**: Consider implementing for production use

---

## 🎓 Next Steps

After successful testing:

1. **Experiment** with different vibes and game contexts
2. **Customize** the prompt engineering in `src/services/prompt_engineer.py`
3. **Extend** the API with additional endpoints
4. **Add** unit tests in the `tests/` directory
5. **Deploy** to a cloud platform (Heroku, AWS, Azure, etc.)

---

## 📞 Support

If you encounter issues:
1. Check this guide's troubleshooting section
2. Review the main README.md
3. Check the IMPLEMENTATION_PLAN.md for technical details
4. Open an issue on GitHub

---

**Happy Testing! 🚀**

*Last Updated: June 20, 2026*