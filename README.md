
# 🌌 Luminous Tasks - A Cosmic To-Do List ✨

![App Screenshot](https://github.com/moeinnm-99/Todo-List/blob/main/Output.png)

A beautifully designed, interactive to-do list application with stellar visual effects and powerful task management features.

## ✨ Features

- **Cosmic UI Design**:
  - Animated particle background
  - Glass-morphism interface elements
  - Smooth transitions and hover effects

- **Task Management**:
  - Add, edit, and delete tasks
  - Set and track deadlines
  - Mark tasks as complete
  - Filter by status (All/Pending/Completed)

- **Smart Alerts**:
  - Urgent tasks pulse with golden glow
  - Visual feedback for all actions

- **Technical**:
  - Flask backend with SQLAlchemy
  - Responsive design (desktop/tablet/mobile)
  - Future Telegram notifications (coming soon)

## 🛠️ Technologies

**Backend**:
- Python 3.7+
- Flask
- SQLAlchemy

**Frontend**:
- HTML5
- CSS3 (animations/gradients)
- JavaScript (ES6)

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/moeinnm-99/Todo-List.git
cd Todo-List
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize database:
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Run the application:
```bash
# Windows
python app.py

# Linux/macOS
python3 app.py
```

6. Access the app:
```
http://localhost:5000
or
127.0.0.1:5000
```

## 🖥️ Usage Guide

1. **Adding Tasks**:
   - Enter task in the input field
   - (Optional) Set a deadline
   - Click "Add" or press Enter

2. **Managing Tasks**:
   - ○ Mark as complete → ✓
   - ✕ Delete task
   - Click text/deadline to edit

3. **Filtering**:
   - Use buttons to view:
     - All tasks
     - Pending only
     - Completed only

## ⚙️ Configuration

Create `.env` file:
```ini
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URI=sqlite:///instance/site.db
```

## 🌟 Development

Run in development mode:
```bash
export FLASK_ENV=development
flask run
```

Production deployment options:
- Gunicorn
- Waitress
- Docker

## 📜 License
</br></br>


## 👨‍💻 Author

**Moein Nouri**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/moein-nouri-62803731a/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/moeinnm_99)

Contributions welcome! Feel free to open issues or submit PRs.

## 🔮 Coming Soon
- Telegram notification integration
- User accounts system
- Dark/light mode toggle

---

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=moeinnm-99&show_icons=true&theme=radical)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=moeinnm-99&layout=compact&theme=radical)

Experience cosmic productivity! ✨🚀
```
