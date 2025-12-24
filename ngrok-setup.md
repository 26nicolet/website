# Using ngrok to Make Your Website Available Online

## Step 1: Install ngrok
1. Go to https://ngrok.com/download
2. Download the macOS version
3. Unzip the file
4. Move ngrok to a location in your PATH:
   ```bash
   sudo mv ngrok /usr/local/bin/
   ```
   Or you can run it from wherever you unzipped it.

## Step 2: Sign up for a free ngrok account (optional but recommended)
1. Go to https://dashboard.ngrok.com/signup
2. Sign up for a free account
3. Get your authtoken from the dashboard
4. Configure ngrok:
   ```bash
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```

## Step 3: Start your Flask app
In one terminal, run:
```bash
cd /Users/22nicolet/Documents/website
source venv/bin/activate
python app.py
```

## Step 4: Start ngrok
In another terminal, run:
```bash
ngrok http 8000
```

This will give you a public URL like `https://abc123.ngrok.io` that anyone can access!

## Notes:
- The free version gives you a random URL each time you start ngrok
- For a permanent URL, you'll need a paid plan
- Make sure your Flask app is running on port 8000 (as configured in app.py)

