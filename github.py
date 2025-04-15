# In-memory data storage
patients = {}
appointments = {}

# Add a new patient
def add_patient():
    patient_id = input("Enter patient ID: ")
    name = input("Enter patient's name: ")
    patients[patient_id] = {"name": name}
    print(f"Patient {name} added successfully!")

# View all patients
def view_patients():
    if not patients:
        print("No patients found.")
    for patient_id, details in patients.items():
        print(f"ID: {patient_id}, Name: {details['name']}")

# Schedule an appointment
def schedule_appointment():
    patient_id = input("Enter patient ID: ")
    if patient_id not in patients:
        print("Patient not found.")
        return
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM): ")
    appointment_id = f"{patient_id}_{date}_{time}"
    appointments[appointment_id] = {"patient_id": patient_id, "date": date, "time": time}
    print(f"Appointment scheduled for {patients[patient_id]['name']} on {date} at {time}.")

# View all appointments
def view_appointments():
    if not appointments:
        print("No appointments scheduled.")
    for appointment_id, details in appointments.items():
        patient_name = patients[details['patient_id']]['name']
        print(f"Appointment ID: {appointment_id}, Patient: {patient_name}, Date: {details['date']}, Time: {details['time']}")

# Cancel an appointment
def cancel_appointment():
    appointment_id = input("Enter appointment ID to cancel: ")
    if appointment_id in appointments:
        del appointments[appointment_id]
        print("Appointment cancelled successfully.")
    else:
        print("Appointment not found.")

# Main menu
def main():
    while True:
        print("\nDental Clinic Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Schedule Appointment")
        print("4. View Appointments")
        print("5. Cancel Appointment")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            schedule_appointment()
        elif choice == '4':
            view_appointments()
        elif choice == '5':
            cancel_appointment()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
