# GitHub Actions Setup Script (PowerShell)
# This script enables GitHub Actions and configures secrets for agent-system-2026

Write-Host "🚀 GitHub Actions Setup Script" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if GitHub CLI is installed
$ghExists = Get-Command gh -ErrorAction SilentlyContinue
if (-not $ghExists) {
    Write-Host "❌ GitHub CLI is not installed" -ForegroundColor Red
    Write-Host "Install from: https://cli.github.com/" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "After installing, run:" -ForegroundColor Yellow
    Write-Host "  gh auth login" -ForegroundColor White
    Write-Host "  Then run this script again" -ForegroundColor White
    exit 1
}

Write-Host "✅ GitHub CLI found" -ForegroundColor Green
Write-Host ""

# Check authentication
Write-Host "🔍 Checking GitHub authentication..." -ForegroundColor Cyan
gh auth status
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Not authenticated with GitHub" -ForegroundColor Red
    Write-Host ""
    Write-Host "Run: gh auth login" -ForegroundColor Yellow
    Write-Host "Then run this script again" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Authenticated with GitHub" -ForegroundColor Green
Write-Host ""

# Get GitHub token from user
Write-Host "🔑 GitHub Token Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To create a token:" -ForegroundColor Yellow
Write-Host "1. Go to: https://github.com/settings/tokens" -ForegroundColor White
Write-Host "2. Click 'Generate new token'" -ForegroundColor White
Write-Host "3. Name it: 'Agent-System-2026'" -ForegroundColor White
Write-Host "4. Select scopes: repo, workflow" -ForegroundColor White
Write-Host "5. Generate and copy the token" -ForegroundColor White
Write-Host ""

$token = Read-Host "Paste your GitHub token here (or press Enter to skip)"

if ($token) {
    Write-Host ""
    Write-Host "📝 Adding GITHUB_TOKEN secret..." -ForegroundColor Cyan
    
    $token | gh secret set GITHUB_TOKEN --repo Warrafeeq/agent-system-2026
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ GITHUB_TOKEN secret added successfully!" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Could not add secret via CLI" -ForegroundColor Yellow
        Write-Host "Add manually at: https://github.com/Warrafeeq/agent-system-2026/settings/secrets/actions" -ForegroundColor Yellow
    }
} else {
    Write-Host "⏭️  Skipping token setup" -ForegroundColor Yellow
    Write-Host "Add manually at: https://github.com/Warrafeeq/agent-system-2026/settings/secrets/actions" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "✅ Setup Complete!" -ForegroundColor Green
Write-Host ""

Write-Host "📋 Manual Steps (Web UI):" -ForegroundColor Cyan
Write-Host "1. Go to: https://github.com/Warrafeeq/agent-system-2026/settings/actions" -ForegroundColor White
Write-Host "2. Verify 'Allow all actions and reusable workflows' is enabled" -ForegroundColor White
Write-Host "3. Check for green checkmarks next to workflows" -ForegroundColor White
Write-Host ""

Write-Host "🚀 Your system will run tomorrow at:" -ForegroundColor Cyan
Write-Host "   9 AM UTC   - Repository Scan & Analysis" -ForegroundColor White
Write-Host "   10 AM UTC  - Project Generation" -ForegroundColor White
Write-Host ""

Write-Host "🔗 Quick Links:" -ForegroundColor Cyan
Write-Host "   Repo:     https://github.com/Warrafeeq/agent-system-2026" -ForegroundColor White
Write-Host "   Actions:  https://github.com/Warrafeeq/agent-system-2026/actions" -ForegroundColor White
Write-Host "   Settings: https://github.com/Warrafeeq/agent-system-2026/settings" -ForegroundColor White
Write-Host ""

Write-Host "✨ Your 2026 AI Agent System is ready to deploy!" -ForegroundColor Green
