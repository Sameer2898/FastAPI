This project i'm created while learning FastAPI. This will contain all of the content which i'm learnt in FastAPI course.

Steps to create virtual env and run the project:-
1. Create a virtual env by the command(assuming that virtual env. library is already installed in your system):-
   python -m venv env
2. Activate the virtual env:-
   For git/linux:-
   Source env/Scripts/activate
   For cmd/powershell:-
   .env/Scripts/activate
3. Install the requirements, by using below command:-
   pip install -r requirements.txt
4. Run the main file, by using below command:-
   python main.py
   uvicorn main:app --reload
