# User Profile Management with Flask and MongoDB

## Project Description
This Flask-based web application allows users to register, log in, update their profile information (city, profession, and profile picture), change passwords, and log out. The application uses MongoDB as the database and supports secure password hashing with bcrypt.

## Features
- User authentication (registration, login, logout)
- Profile update (city, profession, and profile picture)
- Secure password storage using bcrypt
- Session-based authentication
- Flash messages for user feedback

## Installation and Setup

### Prerequisites
Ensure you have the following installed on your system:
- Python 3
- MongoDB
- pip (Python package manager)

### Clone the Repository
```bash
git clone https://github.com/Yessir11/yessir_hw2_itmo_wad.git
cd yessir_hw2_itmo_wad
```

### Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```
### Required Python Libraries
This project requires the following Python libraries:
```bash
Flask
pymongo
bcrypt
Werkzeug
```
To install manually, run:
```bash
pip install Flask pymongo bcrypt Werkzeug
```

### Setting Up MongoDB
1. Connect to MongoDB shell:
   ```bash
   mongo
   ```
2. Create the database and collection:
   ```js
   use itmo_wad_hw2
   db.createCollection("users")
   ```

### Running the Application
```bash
python3 app.py
```
The application will run on `http://localhost:5000/`

## Folder Structure
```
flask-profile-management/
│── static/
│   ├── styles.css
│   ├── uploads/  # Folder for user profile pictures
│── templates/
│   ├── login.html
│   ├── registration.html
│   ├── profile.html
│   ├── updateInfo.html
│── app.py
│── README.md
```

## Routes and Endpoints
<img width="591" alt="Capture d’écran 2025-02-17 à 02 44 47" src="https://github.com/user-attachments/assets/c4fb27a0-edc5-4caf-bafe-8fc7a1460386" />

## Additional Notes
- User passwords are securely hashed using bcrypt.
- Default profile pictures are used if users do not upload one.
- Users can update either one or both profile fields (city and profession) independently.
- The `UPLOAD_FOLDER` is set to `static/uploads` to store profile pictures.

## Screenshots 

Login page
<img width="1165" alt="Capture d’écran 2025-02-17 à 02 48 02" src="https://github.com/user-attachments/assets/4794f02c-5234-4ae4-bc6b-8c21e13cb9c0" />

Registration Page

<img width="588" alt="Capture d’écran 2025-02-17 à 02 48 46" src="https://github.com/user-attachments/assets/cd04f6c9-bbe1-4a14-8641-079ac4f4ce58" />

Authentication of the created user

<img width="560" alt="Capture d’écran 2025-02-17 à 02 49 37" src="https://github.com/user-attachments/assets/b790e4fd-a6e2-4469-8098-9985503aac68" />

Database

<img width="1429" alt="Capture d’écran 2025-02-17 à 02 50 31" src="https://github.com/user-attachments/assets/19ed5c60-f9bb-444c-a782-a60fea3a8f01" />

Profile Page

<img width="1027" alt="Capture d’écran 2025-02-17 à 02 51 21" src="https://github.com/user-attachments/assets/72d3a16d-7dee-49b0-841d-2a164ee54864" />

Edit User Information and upload photo

<img width="1059" alt="Capture d’écran 2025-02-17 à 02 53 12" src="https://github.com/user-attachments/assets/81a14e9f-7778-4301-8cc4-a0baa9bbb7cc" />

Information Updated

<img width="1036" alt="Capture d’écran 2025-02-17 à 02 53 45" src="https://github.com/user-attachments/assets/6eeda1c4-b85c-4ca5-9fff-32d850011115" />

Password Changed

<img width="1088" alt="Capture d’écran 2025-02-17 à 02 55 49" src="https://github.com/user-attachments/assets/9400618b-7e22-408f-b73c-303a2a230069" />

---
For any issues or improvements, feel free to contribute!

---
## Contributor
Yessir GOUTON

