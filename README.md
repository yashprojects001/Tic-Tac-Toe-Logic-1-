# Tic-Tac-Toe-Logic-1-
Python-based intelligent Tic-Tac-Toe game using table-driven (Logic-1) AI with base-3 state encoding and a precomputed knowledge base.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🧠 Intelligent Tic-Tac-Toe Game (Logic-1)

## Design and Implementation of an Intelligent Tic-Tac-Toe Game using Python

---

## 📌 Overview

This project implements an **Intelligent Tic-Tac-Toe Game** using **Python**, based on a **table-driven Artificial Intelligence approach (Logic-1)**.  
The AI uses a **precomputed knowledge base (move table)** to make optimal decisions without performing real-time calculations during gameplay.

This project is aligned with **classical Artificial Intelligence concepts**, focusing on **symbolic AI, knowledge-based systems, and state-space representation**.

---

## 🎯 Objectives

- Implement a Tic-Tac-Toe game using Artificial Intelligence principles
- Represent the game board as a state space
- Encode board states into **base-3 numbers**
- Use a **move table (knowledge base)** for AI decision-making
- Demonstrate **Logic-1 (Table-Driven AI)** as described in AI textbooks

---

## 🧠 AI Technique Used

### Logic-1: Table-Driven / Knowledge-Based AI

- Each board position is represented as a 9-element vector
- Each vector is converted into a unique **base-3 number**
- This number is used as an index into a **predefined move table**
- The AI retrieves the best possible move directly from the table
- No learning or strategy computation occurs during gameplay

---

## 🛠️ Technologies Used

- **Programming Language:** Python
- **AI Approach:** Table-Driven / Knowledge-Based AI
- **Interface:** Console-based

---

## 🧩 Board Representation

| Value | Meaning |
|------|--------|
| 0 | Empty Cell |
| 1 | Human Player (X) |
| 2 | Computer Player (O) |

Total possible board states: 3⁹ = 19,683

---

## ▶️ How the Game Works

1. Initialize an empty Tic-Tac-Toe board
2. Display the board
3. Human player makes a move
4. Board state is encoded into a base-3 number
5. AI uses the number to index the move table
6. AI executes the retrieved optimal move
7. Check for win or draw
8. Repeat until the game ends

---

---

## ✅ Features

- Intelligent AI opponent
- Fast decision-making using table lookup
- Textbook-aligned AI logic
- Simple and readable Python implementation
- Suitable for AI & Data Science coursework

---

## ⚠️ Limitations

- Complete move table requires large memory
- Manual knowledge construction
- Not scalable to larger board sizes
- No learning or adaptability

---

## 🚀 Future Enhancements

- Implement **Logic-2 (Rule-Based AI Strategy)**
- Add **Minimax Algorithm**
- Create a **GUI using Tkinter**
- Introduce difficulty levels
- Extend to larger game boards

---

## 📚 Applications

- Educational AI demonstrations
- Game-playing AI systems
- Knowledge-based systems
- AI fundamentals and coursework projects

---

## 👤 Author

**Yash Pathrikar**  
Artificial Intelligence & Data Science (AIDS) Student  

---

## ⭐ Acknowledgment

This project is inspired by **classical Artificial Intelligence textbooks** and is designed for academic learning and demonstration of **foundational AI concepts**.

---

## 📄 License

This project is open for educational and academic use.



