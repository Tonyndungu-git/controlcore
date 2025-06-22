# 🚀 ControlCore Forge — Industrial Automation Challenges with CODESYS

Welcome to **ControlCore Forge**, a hub for automation engineers, students, and tinkerers! This project features a series of **weekly CODESYS challenges** that focus on practical industrial logic implementation — beyond just simulations.

> 🔧 Whether you're learning automation or sharpening your PLC skills, this repo gives you real-world logic challenges, organized, version-controlled, and presented with visuals and code.

---

## 🎬 Featured Video Presentation

<p>📽️ <strong>Watch the Elevator Position Challenge demo:</strong></p>
<a href="https://us05web.zoom.us/clips/share/RANvFqZRRreSOpNKkUXsow" target="_blank">
  <img src="{% static 'img/elevator_thumb.png' %}" alt="Watch Elevator Challenge" class="img-fluid" style="max-width: 500px; border-radius: 10px;">
</a>



---

## 📦 First Challenge – Elevator Position Increment (State Machine + Tab Memory)

In this challenge, we simulate a **4-floor elevator** system with the following logic:

- ✅ Floor call buttons with direction logic (Up/Down)
- ✅ Internal floor selection buttons
- ✅ Door animations and interlocks
- ✅ Elevator does **not move when doors are open**
- ✅ Tab memory saves floor request states across cycles
- ✅ Queue-based priority logic (up/down direction strategy)
- ✅ State machine controlling elevator behavior: `IDLE`, `MOVING`, `DOOR_OPEN`, `DOOR_CLOSE`

> 🧠 Ideal for understanding PLC state logic, interlocks, memory retention, and visualization.

### 🧠 CODESYS Features Used

- Structured Text (ST)
- Tab Memory
- Visualization with animated doors and elevator car
- State Machine design
- Debug-friendly Boolean flags and indicators

---

## 🌐 GitHub Pages Documentation

📄 View the interactive documentation & challenge previews:  
🔗 https://tonyndungu-git.github.io/controlcore/

---

## 🗂️ Weekly Challenges Roadmap

| Challenge | Description | Status | Code |
|----------|-------------|--------|------|
| 1. Elevator Position Control | Tab memory, state machine, direction logic | ✅ Finished | [View](./challenges/elevator-position) |
| 2. Conveyor Sorting with Vision Sensor | Mock color/size data, timers, diverter control | 🔜 Coming Soon | - |
| 3. PID-Controlled Thermal Chamber | Auto-tune simulation, data logging | 🔜 Coming Soon | - |
| 4. SCADA Water Distribution | Leak detection, pressure control, valves | 🔜 Coming Soon | - |
| 5. 3-Axis Robotic Arm | Jog + Auto mode, limit switches, safety | 🔜 Coming Soon | - |
| ... | (10 Total) |  |  |

> ✅ Status key: `✅ Finished` | `🔜 Coming Soon`

---

## 🛠️ Requirements

- [CODESYS V3.5 SPxx](https://www.codesys.com/)
- Optional: Windows OS for native simulation
- GitHub Pages (for optional docs)
- Python & Django for managing the challenge website

---

## 📢 Stay Updated

📅 New challenges published weekly!  
🔔 Follow the website: [https://controlcore.onrender.com](https://controlcore.onrender.com)

---

## 🤝 Contributing

Have an idea for a challenge or want to feature your project?  
Open an issue or email us from the [Contact page](https://controlcore.onrender.com/contact).

---

## 📜 License

This project is licensed under the MIT License.

---

🧠 _ControlCore Forge – where control logic meets creativity._
