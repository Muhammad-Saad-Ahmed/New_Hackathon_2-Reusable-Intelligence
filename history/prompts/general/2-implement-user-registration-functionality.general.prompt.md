---
ID: 2
TITLE: Implement user registration functionality
STAGE: general
DATE_ISO: 2026-01-02
SURFACE: agent
MODEL: gemini-1.5-pro-a
FEATURE: none
BRANCH: /
USER: 
COMMAND: Tum kya dekh rahe ho?
LABELS: ["frontend", "registration", "bug-fix"]
LINKS: 
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
FILES_YAML:
  - frontend/src/app/signup/page.tsx
TESTS_YAML:
  - 
PROMPT_TEXT: |
  Tum kya dekh rahe ho?
  Browser / Frontend error:
  Failed to load resource: 401 (Unauthorized)

  Lekin root API hit karne par:
  {"message":"Todo Application API","version":"1.0.0"}


  👉 Iska matlab:

  ✅ FastAPI server chal raha hai

  ✅ API reachable hai

  ❌ Protected route bina token ke call ho rahi hai

  🔐 401 Unauthorized ka real matlab

  Server keh raha hai:
  “Tum ho kaun? Token dikhao.”

  401 ka matlab API band nahi,
  balke authentication missing / invalid hai.

  🧠 Root endpoint vs Protected endpoint
  ✅ Public endpoint (no auth)
   @app.get("/")
  def root():
      return {"message": "Todo Application API", "version": "1.0.0"}


  ✔ Ye hamesha kaam karega
  ✔ Token nahi chahiye

  🔒 Protected endpoint (auth required)
   @app.get("/tasks")
  def get_tasks(user=Depends(get_current_user)):
      return []


  ❌ Agar token nahi bheja → 401

  🔥 Sab se common mistake (99% cases)
  ❌ Frontend se API call without token
  fetch("http://localhost:8000/tasks")


  ➡️ Result: 401 Unauthorized

  ✅ Sahi tareeqa (Token ke sath call)
  Step 1: BetterAuth se session lo
  const session = await auth.getSession();

  Step 2: Token extract karo
  const token = session?.accessToken;

  Step 3: API call with Authorization header
  fetch("http://localhost:8000/tasks", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });


  ✔ Ab 401 nahi aayega
RESPONSE_TEXT: |
  The project new users ko register karnay kay liye `frontend/src/app/signup/page.tsx` pay aik form provide karta hai. Jab user apna `name`, `email`, aur `password` enter karkay "Sign up" button par click karta hai, to `handleSubmit` function call hota hai.

  Currently, `handleSubmit` function backend API ko call nahi kar raha hai. Isko theek karne ke liye, `handleSubmit` function ko `apiClient.registerUser` ko call karna chahiye, jo backend ke `/auth/register` endpoint ko user data bhej kar new user create karega.

  Abhi, main isko theek kar raha hoon.
OUTCOME: Implemented the missing user registration logic in the signup form.
EVALUATION: The user registration form now correctly calls the backend API to create a new user.
