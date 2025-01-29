# Face attendance system with face for schools

## Features

* **Real-time Face Detection:** Detects faces in real-time from a camera or video feed.
* **Face Recognition:** Identifies students based on their pre-enrolled facial data.
* **Attendance Marking:** Automatically marks attendance for recognized students.
* **Attendance Records:** Stores attendance data, including date, time, student ID

## Usage
1. **Clone the repository:**

```bash
   git clone https://github.com/abel-source/face-recognition.git
   cd face-recognition
```

2. **Install required libraries:**

```bash
   pip install -r requirements.txt
```

3. **Encoding the images:**
   
      ● Add student images to the images folder. Images should ideally be 214x214 pixels and in PNG format.
   
      ● Run `Encoder.py`. This will generate a file named `EncodeFile.p` containing the face encodings.
   
5. **Firebase Configuration:**
   
      ● This project uses Firebase as a backend. You must replace the existing Firebase credentials in the code with your own. The credentials currently in the repository are for testing purposes only and will not work for you. Consult the Firebase documentation for instructions on setting up a project and obtaining your credentials.

6. **Database Setup:**
   
      ● Modify AddDatatoDatabase.py with the correct student information. The numerical part of the image filename should correspond to the student's ID in the database. Ensure the data in this script aligns with your Firebase database structure.
   
6. **Run the system:**

      ● Execute `main.py` to start the face recognition attendance system.
      
