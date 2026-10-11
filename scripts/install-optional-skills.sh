#!/usr/bin/env bash
set -euo pipefail

echo "Optional helpers for Anker Pilot. Run only if the exam environment permits third-party installs."
mkdir -p "$HOME/.claude/skills"

if command -v git >/dev/null 2>&1; then
  echo "Installing Humanizer-zh (MIT)..."
  rm -rf "$HOME/.claude/skills/humanizer-zh"
  git clone --depth 1 https://github.com/op7418/Humanizer-zh.git "$HOME/.claude/skills/humanizer-zh"

  echo "Cloning Superpowers (MIT) for optional use..."
  rm -rf "$HOME/.claude/superpowers"
  git clone --depth 1 https://github.com/obra/superpowers.git "$HOME/.claude/superpowers"
else
  echo "git unavailable; skip optional installs. Core Anker Pilot remains fully usable."
fi
