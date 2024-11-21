# Dungeon Adventure 🏰

A Python-based dungeon crawler game where heroes must collect the four Pillars of Object-Oriented Programming while navigating through a randomly generated dungeon filled with challenges and opportunities.

## 🎮 Game Overview

In Dungeon Adventure, players take on the role of a hero randomly placed in a procedurally generated dungeon. The main objective is to:
- Collect all four Pillars of OO (Abstraction, Encapsulation, Inheritance, and Polymorphism)
- Navigate through the dungeon while avoiding hazards
- Use special items strategically
- Find the exit with all pillars to win

## 🌟 Features

- **Procedural Dungeon Generation**: Every playthrough features a unique dungeon layout
- **Multiple Game Elements**:
  - Hero character with health management
  - Four collectible Pillars of OO
  - Hazards (pits)
  - Support items (healing and vision potions)
  - Random placement of all elements
- **Object-Oriented Design**: Utilizes OOP principles for clean, maintainable code
- **Optional GUI Interface**: Visual representation of the dungeon and game state

## 🛠️ Technical Implementation

### Prerequisites
- Python 3.x
- Additional dependencies (if any) listed in `requirements.txt`

### Installation
```bash
git clone https://github.com/yourusername/dungeon-adventure.git
cd dungeon-adventure
pip install -r requirements.txt
```

### Running the Game
```bash
python main.py
```

## 🏗️ Architecture

The project follows object-oriented principles and includes:
- Abstract classes and interfaces for game entities
- Design patterns for improved maintainability
- Unit tests for core functionality
- Modular, extensible codebase

### Key Components
- `DungeonGenerator`: Handles maze generation algorithms
- `GameEntity`: Base class for all game objects
- `Hero`: Player character implementation
- `Item`: Abstract base class for collectible items
- `GUI`: Optional graphical interface implementation

## 🧪 Testing

The project includes comprehensive unit tests to ensure reliability:
```bash
python -m unittest discover tests
```

## 👥 Team

This project was developed as part of TCSS 502 - Object-Oriented Programming, demonstrating proficiency in:
- Object-oriented design principles
- Team collaboration
- Code versioning
- Testing methodologies
- Documentation

## 📄 License

This project is available under the MIT License. See LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 Course Objectives Met

This project satisfies all course objectives including:
- Implementation of OOP concepts
- Application of design patterns
- Systematic testing and debugging
- Code refactoring
- Data structure implementation
- Algorithm optimization
- GUI development
- Unit testing
- Modern software engineering tools usage
- API documentation interpretation

---

*Note: This project was created as part of the TCSS 502 course curriculum.*