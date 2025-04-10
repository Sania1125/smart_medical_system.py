# Smart Medical Appointment Booking System

class Patient:
    def __init__(self, name, age, problem):
        self.name = name
        self.age = age
        self.problem = problem


class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.available_slots = ["10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM"]
        self.booked = {}

    def book_slot(self, patient):
        if self.available_slots:
            slot = self.available_slots.pop(0)
            self.booked[slot] = patient
            print(f"\n✅ Appointment booked with Dr. {self.name} at {slot} for {patient.name}")
        else:
            print(f"\n❌ No available slots for Dr. {self.name}.")

    def show_slots(self):
        print(f"\nAvailable slots for Dr. {self.name}:")
        if self.available_slots:
            for slot in self.available_slots:
                print(f"  • {slot}")
        else:
            print("  (All slots booked)")


class AppointmentSystem:
    def __init__(self):
        self.doctors = []
        self.appointments = []

    def add_doctor(self, name, specialty):
        doctor = Doctor(name, specialty)
        self.doctors.append(doctor)
        print(f"👨‍⚕️ Added Dr. {name} - {specialty}")

    def show_doctors(self):
        if not self.doctors:
            print("\nNo doctors available.")
            return
        print("\nList of Doctors:")
        for i, doc in enumerate(self.doctors):
            print(f" {i+1}. Dr. {doc.name} ({doc.specialty})")

    def book_appointment(self):
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        problem = input("Enter problem: ")
        patient = Patient(name, age, problem)

        self.show_doctors()
        choice = int(input("Select doctor by number: ")) - 1

        if 0 <= choice < len(self.doctors):
            doctor = self.doctors[choice]
            doctor.show_slots()
            confirm = input("Do you want to book the earliest slot? (y/n): ").lower()
            if confirm == 'y':
                doctor.book_slot(patient)
                self.appointments.append((doctor.name, patient.name))
        else:
            print("❌ Invalid doctor selection.")

    def show_appointments(self):
        print("\n📋 Booked Appointments:")
        for doc in self.doctors:
            for time, pat in doc.booked.items():
                print(f" - {time} → Dr. {doc.name} with {pat.name} (Problem: {pat.problem})")


# ---------------- Main ----------------
system = AppointmentSystem()

# Predefined doctors
system.add_doctor("Ali", "General")
system.add_doctor("Kamran", "ENT")

while True:
    print("\n===== Smart Medical Appointment Booking System =====")
    print("1. Show Doctors")
    print("2. Book Appointment")
    print("3. Show All Appointments")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        system.show_doctors()
    elif choice == '2':
        system.book_appointment()
    elif choice == '3':
        system.show_appointments()
    elif choice == '4':
        print("👋 Exiting system. Goodbye!")
        break
    else:
        print("❌ Invalid input.")
