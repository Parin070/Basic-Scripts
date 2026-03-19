# Simple Password Strength Checker

A Python-based password strength checker that evaluates passwords across multiple criteria and returns a final strength score.

> ⚠️ Educational purposes only. This tool does not store or transmit passwords.

## How it Works

The checker evaluates your password across 5 criteria, each scored out of 10:

- **Length** — 8+ chars (5pts), 10+ (7pts), 16+ (10pts)
- **Uppercase letters** — at least 1 required
- **Lowercase letters** — at least 4 recommended
- **Special characters** — at least 1 required
- **Digits** — at least 1 required

Final score is the average of all 5 criteria.

| Score | Result |
|-------|--------|
| 8–10 | You are secure!! |
| 5–8 | Could be better! |
| 0–5 | You are cooked 🥀 |

## How to Run
```bash
python3 password.py
```

Then enter your password when prompted.

## Known Limitations

- ❌ No dictionary attack protection — common passwords like `Password123!` may score high despite being easily crackable
- ❌ No entropy calculation
- ❌ Score is based on character composition only, not actual strength against brute force
