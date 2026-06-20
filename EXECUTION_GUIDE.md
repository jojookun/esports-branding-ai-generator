# ⚡ Execution Guide - Run Locally

Complete step-by-step guide to run the AI-Powered eSports Branding Generator on your local machine.

---

## 🎯 Prerequisites

- ✅ Python 3.9 or higher
- ✅ pip (Python package manager)
- ✅ IBM watsonx.ai account with API credentials
- ✅ Terminal/Command Prompt

---

## 🚀 Quick Start (5 Steps)

### Step 1: Create Virtual Environment

**Windows (PowerShell)**:
```powershell
cd "Reimagine Creative Industries with AI - AI-Powered eSports Branding & Visual Concept Generator"
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**:
```cmd
cd "Reimagine Creative Industries with AI - AI-Powered eSports Branding & Visual Concept Generator"
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux**:
```bash
cd "Reimagine Creative Industries with AI - AI-Powered eSports Branding & Visual Concept Generator"
python3 -m venv venv
source venv/bin/activate
```

**Verify**: Your prompt should show `(venv)` at the beginning.

---

### Step 2: Install Dependencies

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

**Expected**: Installation of ~20 packages (FastAPI, LangChain, IBM watsonx-ai, etc.)

**Time**: ~2-3 minutes depending on internet speed

---

### Step 3: Configure Environment

#### 3.1 Create .env File

**Windows (PowerShell)**:
```powershell
Copy-Item .env.template .env
```

**macOS/Linux**:
```bash
cp .env.template .env
```

#### 3.2 Get IBM watsonx Credentials

1. **Login**: https://cloud.ibm.com/
2. **Navigate to watsonx.ai**: https://dataplatform.cloud.ibm.com/wx/home
3. **Get API Key**:
   - Go to "Manage" → "Access (IAM)" → "API keys"
   - Click "Create" → Copy the key
4. **Get Project ID**:
   - In watsonx.ai, go to your project
   - Click "Manage" tab → Copy "Project ID"

#### 3.3 Edit .env File

Open `.env` in any text editor and update:

```env
WATSONX_API_KEY=your_actual_api_key_here
WATSONX_PROJECT_ID=your_actual_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com

MODEL_ID=ibm/granite-13b-chat-v2
MODEL_TEMPERATURE=0.7
MODEL_MAX_TOKENS=2000
```

**Important**: Replace the placeholder values with your actual credentials!

---

### Step 4: Run Interactive Demo

```bash
python examples/api_integration_demo.py
```

#### What Happens:
1. Loads configuration from `.env`
2. Validates watsonx credentials
3. Offers two modes:
   - **Option 1**: Live API (uses IBM Granite)
   - **Option 2**: Mock data (no API required)

#### Test with Mock Data (No API Credits Used):

```
Select option (1 or 2, default=2): 2
```

**Output**: Displays a complete branding concept with colors, typography, and layouts.

#### Test with Live API:

```
Select option (1 or 2, default=2): 1
```

**Output**: Generates a real branding concept using IBM Granite (uses API credits).

---

### Step 5: Start FastAPI Server

```bash
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

#### Access the API:

- **Swagger UI (Interactive Docs)**: http://localhost:8000/docs
- **ReDoc (Alternative Docs)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **API Root**: http://localhost:8000/

---

## 🎮 Testing Examples

### Example 1: osu!mania Streamer

**Vibe**: "Pastel kawaii aesthetic with soft gradients and playful energy"  
**Game Context**: "osu!mania"

**Via Demo Script**:
```bash
python examples/api_integration_demo.py
# Select option 1 for live API
```

**Via API (Swagger UI)**:
1. Go to http://localhost:8000/docs
2. Expand `POST /generate`
3. Click "Try it out"
4. Enter:
```json
{
  "vibe": "Pastel kawaii aesthetic with soft gradients and playful energy",
  "game_context": "osu!mania"
}
```
5. Click "Execute"

**Expected Output**:
- Theme: Playful, energetic name
- Colors: Pastel pinks, blues, purples
- Fonts: Rounded, friendly typography
- Layouts: Rhythm game streaming recommendations

---

### Example 2: Honor of Kings Team

**Vibe**: "Epic fantasy with mystical purple and gold accents"  
**Game Context**: "Honor of Kings"

**Via cURL (Windows PowerShell)**:
```powershell
$body = @{
    vibe = "Epic fantasy with mystical purple and gold accents"
    game_context = "Honor of Kings"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/generate" -Method Post -Body $body -ContentType "application/json"
```

**Via cURL (macOS/Linux)**:
```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "vibe": "Epic fantasy with mystical purple and gold accents",
    "game_context": "Honor of Kings"
  }'
```

**Expected Output**:
- Theme: Fantasy-inspired name
- Colors: Purple, gold, dark backgrounds
- Fonts: Elegant, regal typography
- Layouts: MOBA streaming recommendations

---

### Example 3: Valorant Team

**Vibe**: "Futuristic cyberpunk with neon accents for competitive FPS"  
**Game Context**: "Valorant"

**Via Python Script**:

Create `test_api.py`:
```python
import requests
import json

response = requests.post(
    "http://localhost:8000/generate",
    json={
        "vibe": "Futuristic cyberpunk with neon accents for competitive FPS",
        "game_context": "Valorant"
    }
)

result = response.json()

if result["success"]:
    concept = result["concept"]
    print(f"Theme: {concept['theme_name']}")
    print(f"Colors: {', '.join(concept['color_palette'])}")
    print(f"Primary Font: {concept['typography']['primary_display']}")
else:
    print(f"Error: {result['error']}")
```

Run:
```bash
python test_api.py
```

**Expected Output**:
- Theme: Cyberpunk/tech-inspired name
- Colors: Neon colors with dark backgrounds
- Fonts: Futuristic, geometric typography
- Layouts: FPS competitive streaming recommendations

---

## 📊 API Endpoints Reference

### POST /generate
Generate a branding concept.

**Request**:
```json
{
  "vibe": "string (10-500 characters)",
  "game_context": "string (optional)"
}
```

**Response**:
```json
{
  "success": true,
  "concept": {
    "theme_name": "string",
    "color_palette": ["#HEX1", "#HEX2", "#HEX3", "#HEX4", "#HEX5"],
    "typography": {
      "primary_display": "string",
      "secondary_body": "string",
      "pairing_rationale": "string"
    },
    "layout_guidelines": {
      "streaming_overlay": "string",
      "social_media_banner": "string",
      "text_masking_concepts": "string"
    }
  },
  "error": null,
  "metadata": {}
}
```

### GET /health
Check service health.

**Response**:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "service": "eSports Branding Generator"
}
```

### GET /schema
Get JSON schema for output format.

### GET /config
Get current configuration (non-sensitive).

---

## 🔍 Verification Checklist

After setup, verify:

- [ ] Virtual environment activated (`(venv)` in prompt)
- [ ] All dependencies installed (no errors)
- [ ] `.env` file created with valid credentials
- [ ] Demo script runs successfully
- [ ] FastAPI server starts without errors
- [ ] Swagger UI accessible at http://localhost:8000/docs
- [ ] Health check returns `{"status": "healthy"}`
- [ ] Can generate concepts via API

---

## 🐛 Troubleshooting

### Issue: "Module not found"
**Solution**: Ensure virtual environment is activated
```bash
# Check if venv is active (should see (venv) in prompt)
# If not, activate it:
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # macOS/Linux
```

### Issue: "watsonx configuration is incomplete"
**Solution**: Check `.env` file
```bash
# Verify .env exists
ls .env  # macOS/Linux
dir .env  # Windows

# Check contents (should have API key and project ID)
cat .env  # macOS/Linux
type .env  # Windows
```

### Issue: Port 8000 already in use
**Solution**: Use different port
```bash
uvicorn src.main:app --reload --port 8001
```

### Issue: Import errors
**Solution**: Run from project root
```bash
# Make sure you're in the correct directory
pwd  # macOS/Linux
cd  # Windows

# Should show: .../Reimagine Creative Industries with AI - AI-Powered eSports Branding & Visual Concept Generator
```

### Issue: SSL certificate errors
**Solution**: Update certificates
```bash
pip install --upgrade certifi
```

---

## 📈 Performance Notes

- **First Request**: 10-15 seconds (model initialization)
- **Subsequent Requests**: 5-10 seconds (generation time)
- **Concurrent Requests**: FastAPI handles async efficiently
- **API Credits**: Each generation uses IBM watsonx credits

---

## 🎯 Next Steps

After successful local testing:

1. ✅ Test with different vibes and game contexts
2. ✅ Experiment with temperature settings in `.env`
3. ✅ Try the mock data mode to understand output format
4. ✅ Use Swagger UI for interactive testing
5. ✅ Record demo video showing the system in action
6. ✅ Deploy to cloud platform (optional)
7. ✅ Submit to challenge

---

## 📚 Additional Resources

- **Full Documentation**: See README.md
- **Setup Details**: See SETUP_AND_TESTING_GUIDE.md
- **GitHub Upload**: See DEPLOY_TO_GITHUB.md
- **Technical Details**: See IMPLEMENTATION_PLAN.md

---

**Ready to Run! 🚀**

Follow the 5 steps above to get your eSports Branding Generator running locally!

*Execution time: ~10 minutes from start to finish*