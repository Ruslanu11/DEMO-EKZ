CREATE TABLE Patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Patronymic VARCHAR(50),
    Passport_number VARCHAR(20),
    Date_of_birth DATE,
    Gender CHAR,
    Address VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(50),
    Medical_card_number VARCHAR(20),
    Date_of_issue_medical_card DATE,
    Date_of_last_visit DATE,
    Date_of_next_visit DATE,
    Insurance_policy_number VARCHAR(20),
    Policy_expiry_date DATE
);

CREATE TABLE Medical_Diagnostic_Procedures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES Patients(id),
    Patient_full_name VARCHAR(150),
    Procedure_date DATE,
    Doctor VARCHAR(100),
    Procedure_type VARCHAR(50),
    Procedure_name VARCHAR(100),
    Results TEXT
);

CREATE TABLE Services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100),
    Price DECIMAL(8,2)
);

CREATE TABLE Patients_Services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES Patients(id),
    service_id INT,
    FOREIGN KEY (service_id) REFERENCES Services(id)
);

CREATE TABLE Doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Full_name VARCHAR(100),
    Specialization VARCHAR(50)
);

CREATE TABLE Medical_Center_Doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INT,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(id),
    medical_center_id INT,
    FOREIGN KEY (medical_center_id) REFERENCES Medical_Centers(id)
);

CREATE TABLE Medical_Centers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100),
    Address VARCHAR(100),
    Phone VARCHAR(15)
);

CREATE TABLE Medical_Center_Departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medical_center_id INT,
    FOREIGN KEY (medical_center_id) REFERENCES Medical_Centers(id),
    Name VARCHAR(100),
    Room_number INT
);

CREATE TABLE Prescriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES Patients(id),
    doctor_id INT,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(id),
    Drug_name VARCHAR(100),
    Dosage VARCHAR(50),
    Note TEXT
);

CREATE TABLE Tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES Patients(id),
    Test_type VARCHAR(50),
    Date_conducted DATE,
    Results TEXT
);
