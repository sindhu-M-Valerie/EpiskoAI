#!/bin/bash

echo "🚀 EpiskoAI Deployment Script"
echo "=============================="
echo ""

# Generate icons
echo "📱 Generating app icons..."
python3 generate_icons.py

# Check if icons were generated
if [ ! -d "icons" ]; then
    echo "❌ Failed to generate icons"
    exit 1
fi

echo ""
echo "✓ Icons generated successfully"
echo ""

# Start a simple HTTP server
echo "🌐 Starting local server..."
echo "The app will be available at:"
echo "  → http://localhost:8000/app.html"
echo ""
echo "To install the app:"
echo "  1. Open the URL in Chrome, Edge, or Safari"
echo "  2. Look for the install button in the address bar"
echo "  3. Click 'Install' to add it to your home screen"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start Python HTTP server
python3 -m http.server 8000
