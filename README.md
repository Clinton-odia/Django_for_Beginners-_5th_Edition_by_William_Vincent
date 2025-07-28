# 🧰 Django for Beginners – 5th Edition by William S. Vincent

This repository contains my completed work from the book **_Django for Beginners (5th Edition)_** by [William S. Vincent](https://wsvincent.com/). It includes hands-on projects that build core Django skills from scratch — ideal for anyone starting their journey into backend web development with Python.

> ✅ **Repo:** [Clinton-odia/Django_for_Beginners-_5th_Edition_by_William_Vincent](https://github.com/Clinton-odia/Django_for_Beginners-_5th_Edition_by_William_Vincent)

---

## 📚 What This Covers

Each chapter builds on the last, progressing from the basics to real-world patterns:

| Chapter | Project or Concept              | Highlights                                                 |
|---------|----------------------------------|-------------------------------------------------------------|
| 1–3     | Hello World & Pages App         | Django project setup, views, URL routing, templates         |
| 4–6     | Static Pages & Templates        | Template inheritance, base layouts                         |
| 7–9     | Blog App                        | Models, migrations, CRUD with class-based views            |
| 10–12   | Authentication System           | Signup, login/logout, user permissions                     |
| 13–14   | Comments & Authorization        | Custom forms, comment model, view-level access control     |
| 15      | Styling & Static Files          | Bootstrap, CSS, static and media file configuration         |
| 16      | Deployment                      | Environment variables, Heroku deployment, `environs` setup  |

---

## 🚀 How to Run a Project Locally

```bash
# Clone the repository
git clone https://github.com/Clinton-odia/Django_for_Beginners-_5th_Edition_by_William_Vincent.git
cd Django_for_Beginners-_5th_Edition_by_William_Vincent

# Navigate to a chapter/project folder
cd ch14_permissions_and_authorization

# Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\activate      # On Windows
# source .venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver
