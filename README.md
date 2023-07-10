# Covid-19 Statistics Web Application (Proof of Concept)

## ``About``

This web application is designed to display Covid-19 statistics from around the world. It includes a user-friendly interface with a dropdown menu for countries, a data table, and a world map for data visualization. This project serves as a proof of concept and will be submitted to a company for testing and evaluation purposes. It is not currently open to contributions from the wider open source community. However, if you come across any bugs or issues, or if you have suggestions for improvement, please feel free to get in touch.

> **Important!**
> 
> This web application is a proof of concept to be tested in a local environment and is not intended for deployment as a production application. For example, we generally recommend using email services to send email requests from the server for better security, but we used a library for ease of integration and testing.
>

<br/>

## ``Table of Contents``

- [About](#about)
- [Prerequisites](#prerequisites)
- [Build Instructions Using Docker](#running-the-application-using-docker)
- [Manual Build Instructions](#manual-build-instructions)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [Contact Information](#contact-information)

<br/>

## ``Prerequisites``

Before you begin, ensure you have met the following requirements:

- **Operating System**: Compatible with the software used (Windows 10/ MacOS 10.14 Mojave or newer/ Ubuntu 18.04 or newer).
- **Hardware**: Adequate hardware capacity (check the requirements of Node.js, Python, Docker etc.).
- **Web Browser**: A modern web browser like Google Chrome (version 83 or newer), Mozilla Firefox (version 77 or newer), Safari (version 13 or newer), etc. The application has been tested on these browsers and we recommend using one of them for the best experience. 
- **Internet Connection**: Some dependencies might need to be downloaded from the internet during installation. Hence, a stable internet connection is required.
- **Terminal**: Required to run the commands for installing dependencies and starting the server.
- **Text Editor or IDE** (Preferred): For inspecting or modifying the code.

### **Application Tech Stack**

This application is built with the following technologies. It's recommended to have a basic understanding of these tools:

#### Frontend:

- **[TypeScript](https://www.typescriptlang.org/docs/)** (Programming Language)
- **[Vue.js](https://vuejs.org/v2/guide/)** (TypeScript Framework)
- **[Vite](https://vitejs.dev/guide/)** (Build Tool)
- **[Tailwind CSS](https://tailwindcss.com/docs)** (Low-level CSS Framework)

#### Backend: 

- **[Python](https://docs.python.org/3/)** (Programming Language)
- **[FastAPI](https://fastapi.tiangolo.com/)** (Python Framework)
- **[Uvicorn](https://www.uvicorn.org/)** (ASGI Web Server Implementation for Python)

#### Containerization:

- **[Docker](https://docs.docker.com/get-started/overview/)** (Software for Containerization)

Please refer to the individual resources linked for more detailed information.

### **Environment Variables**
> **Important!**
> 
> Make sure to populate `.env.local` file in both the `client` and `server` folder with appropriate values. The instructions are provided in the `.env.local` file in the respective directories. Never commit your `.env.local` files to the repository as they may contain sensitive information.
>
<br/>

## ``Build Instruction Using Docker``
### Requirements:
- Ensure you have Docker installed (Version 19.03 or newer). If not, follow the [Docker official installation guide](https://docs.docker.com/get-docker/).
- Populate `.env.local` file in both the `client` and `server` folder with appropriate values.

### To start the application using Docker:

1. Enable Docker on your system.

2. In the root folder, run the following command to start a development environment. This uses the `docker-compose.dev.yml` file.

```bash
docker-compose -f docker-compose.dev.yml up --build
```

3. Alternatively, for a production build, run the following command in the command line. This uses the `docker-compose.yml`

```bash
docker-compose up --build
```

4. The front-end application should be running at http://localhost:8080 and back-end application at http://localhost:8000

5. To stop the Docker containers, type the following command:

```bash
docker-compose down
```

<br/>

## ``Manual Build Instructions``
If Docker does not work, you can manually build and run the application:
### Requirements: 
- Populate `.env.local` file in both the `client` and `server` folder with appropriate values.
- Frontend:
  - [Node.js (v14 or newer)](https://nodejs.org/en/download/)
  - npm (comes with Node.js)
  - Vue.js, Vite, and Tailwind CSS (installed with the "npm install" command in the `client` directory)
- Backend:
  - [Python 3.8 or newer](https://www.python.org/downloads/)
  - pip (comes with Python 3.8 and newer)
  - FastAPI, Uvicorn and other Python packages (installed with the "pip install -r requirements.txt" command in the `server` directory)

### To start the application manually: 
For the frontend:
1. Navigate to the `client` directory.
2. Run the following command to install all the dependencies.

```bash
npm install
```

3. Run the following command to start the development server.

```bash
npm run dev
```

4. The front-end application should be running at http://localhost:5173. Please note that port 5173 is the default port used by Vite for its applications.

For the backend:
1. Navigate to the `server` directory.

2. Set up a new virtual environment and activate it:

```bash
# On macOS or Linux:
python3 -m venv myenv
source  myenv/bin/activate  

# On Windows: 
python -m venv myenv
myenv\Scripts\activate

# Important: Make sure you have the right access to execute the script
# Note: You can replace "myenv" to any desired name.
```

3. Once the virtual environment is activated, run the following command to install all the Python dependencies.

```bash
pip install -r requirements.txt
```

4. Run the following command to start the development server.

```bash
uvicorn main:app --reload
```

5. The back-end application should be running at http://localhost:8000

6. To stop the servers, you can press `Ctrl + C` in your terminal.

<br/>

## ``Troubleshooting``

1. If you encounter any errors, make sure that Node.js, npm, Python, and pip are correctly installed. 

2. If the application is not running correctly, ensure that the .env.local file exists and is correctly populated.

3. Firewall or port usage conflicts: The application is supposed to run on localhost:8080 (frontend) and localhost:8000 (backend). If you already have some services running on these ports, you would encounter issues. In such a scenario, you can change the ports in the Docker or manual start commands. Be aware that you will need to use the new ports to access the application.

4. If the application doesn't behave as expected on your browser, try a different browser or a newer version of markdown
your current one. Ensure you are using one of the recommended browsers (Google Chrome version 83 or newer, Mozilla Firefox version 77 or newer, or Safari version 13 or newer).

5. If you are using Python for the first time and aren't familiar with virtual environments, we highly recommend that you check out this [Python documentation](https://docs.python.org/3/tutorial/venv.html) which explains their use in detail. Alternatively, you could follow along with one of the many video tutorials available on platforms like YouTube.

6. Server shutdown: It's important to properly shut down your servers when you are finished working. For Docker, you can use the command `docker-compose down`. If you are running the servers manually, pressing `Ctrl + C` in the terminal where the servers are running will generally stop the process.

For more specific problems, please refer to the FAQ section or get in touch via the contact information provided below.

<br/>

## ``Contributors``

This project was created by:

- Kazuki Mori - Initial work, building proof of concept.

As this project is a proof of concept for a company, we are not currently accepting contributions from outside. However, your feedback is always appreciated.

## ``Contact Information``

For any additional questions or comments, you can reach out to [Kazuki Mori](mailto:kazukidesigner@gmail.com)

<br/>

> **_NOTE:_** Please make sure to follow all recommended practices while sharing sensitive information such as email addresses. Always try to use official and secure communication channels.