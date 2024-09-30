# 🧠 Personal Assistant AI - Jarvis

![License](https://img.shields.io/github/license/fishylow/Project-Jarvis) ![Python](https://img.shields.io/badge/python-3.x-blue) ![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

Your very own AI-powered personal assistant to help manage tasks, schedule reminders, and provide real-time information. Designed to simplify daily activities with voice commands, smart recommendations, and much more!

---

## 🚀 Features

- **Task Management**: Add, edit, and track your tasks effortlessly. (TODO)
- **Voice Commands**: Control the assistant using natural language voice inputs.
- **Smart Reminders**: Set reminders for important tasks and events. (TODO)
- **Integration with APIs**: Retrieve real-time data from external services (e.g., weather, news, etc.).
- **Customizable Responses**: Modify how the AI responds and interacts. (TODO)
- **Expandability**: Add custom plugins to enhance functionality.

---

## 🛠️ Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Clone the repository

```bash
git clone https://github.com/fishylow/Project-Jarvis.git
cd Project-Jarvis
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the AI Assistant

```bash
python Project-Jarvis.py
```

---

## 📖 Usage

Once the assistant is running, you can interact with it via the terminal or through voice commands. Here's an example of how you might interact:

```bash
> Hey Jarvis, open Google Chrome and search for Github.
```

---

## 🧩 Customization

### Add a New Feature

1. Navigate to the `modules/` directory.
2. Create a new Python file with your custom logic.
3. Import your new feature in `tools.py`.

---

## 📝 To Do list

- switch to Llama 3.2
- add calendar support
- add git support
- add typing prompting
- ~~add program opening support~~ Done
- add shutter control support
- add light control support
- extend notes.json
- ~~add file creation support~~ Done
- give full access to file system (after llama switch)
- give screenshot permission (after llama switch)
- add colors to the terminal
- add discord api support
- add reminder support
- add adaptive learning (after llama switch)
- move to Linux server computer (after llama switch)
- make it usable through the internet for arduino access (after computer switch)

## 🖥️ API Integrations

Your AI can integrate with various third-party services. Make sure to add your API keys in the `.env` file:

```bash
  SPOTIPY_CLIENT_ID = 'YOUR-SPOTIFY-CLIENT-ID-HERE'
  SPOTIPY_CLIENT_SECRET = 'YOUR-SPOTIFY-CLIENT-SECRET-HERE'
  OPENAI_API_KEY = "YOUR-OPENAI-API-KEY-HERE"
```

---

## 🛡️ Security

Make sure to avoid committing sensitive information such as API keys or personal data. You can add the `.env` file to your `.gitignore`.

---

## 🧑‍💻 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for improving the project.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
