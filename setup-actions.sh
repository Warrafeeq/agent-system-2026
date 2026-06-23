#!/bin/bash
# Enable GitHub Actions for agent-system-2026 repository
# This script uses GitHub CLI to automate the process

echo "🚀 GitHub Actions Setup Script"
echo "================================"
echo ""

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI is not installed"
    echo "Install from: https://cli.github.com/"
    echo ""
    echo "After installing, run:"
    echo "  gh auth login"
    echo "  Then run this script again"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub"
    echo ""
    echo "Run: gh auth login"
    echo "Then run this script again"
    exit 1
fi

echo "✅ GitHub CLI authenticated"
echo ""

# Enable Actions
echo "📋 Enabling GitHub Actions..."

gh repo edit Warrafeeq/agent-system-2026 \
    --enable-actions

if [ $? -eq 0 ]; then
    echo "✅ GitHub Actions enabled!"
else
    echo "⚠️  Could not enable via CLI (try web UI)"
fi

echo ""
echo "================================"
echo "✅ Setup Complete!"
echo ""
echo "Next steps:"
echo "1. Go to: https://github.com/Warrafeeq/agent-system-2026/settings/actions"
echo "2. Verify 'Allow all actions and reusable workflows' is enabled"
echo "3. Go to: https://github.com/Warrafeeq/agent-system-2026/settings/secrets/actions"
echo "4. Add secret: GITHUB_TOKEN"
echo ""
echo "Your agent will run tomorrow at 9 AM UTC! 🚀"
