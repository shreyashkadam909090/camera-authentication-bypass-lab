# Camera-authentication-bypass-lab
This project simulates a camera streaming system with login authentication. User logs in, session is created, camera captures frames, sends them to the server, and displays live on viewer page. It demonstrates client-server flow and basic security weaknesses.

---

## How It Works

1. User opens the application in browser  
2. Redirected to login page  
3. User enters credentials  
4. Server verifies login and creates session  
5. Camera access is requested from browser  
6. Frames are captured continuously  
7. Frames are sent to server using POST request  
8. Server saves image as frame.jpg  
9. Viewer page refreshes and shows live stream  

---

##  How to Run

1. Start server: python server.py
2. Open browser: http://localhost:8000

3. Login:
- Username: admin  
- Password: 1234  

---

## Security Issues (Learning Purpose)

- Hardcoded credentials  
- No HTTPS encryption  
- Weak session handling  
- Open upload endpoint  
- No input validation  

## Purpose

This project is built for educational purposes to understand:
- Client-server communication  
- Camera data handling  
- Basic web security weaknesses  
