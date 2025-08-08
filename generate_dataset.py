import pandas as pd
import random

# Complaint templates for each category
complaint_templates = {
    "IT Support": [
        "System in lab crashes during practicals.",
        "Wi-Fi disconnects every few minutes.",
        "College email login not working.",
        "LMS is inaccessible today.",
        "Printer is jammed in the lab."
    ],
    "Hostel": [
        "Water supply is off in the hostel.",
        "Room light is flickering constantly.",
        "Mess food is very oily and cold.",
        "Fan in my room isn’t working.",
        "Washrooms are not clean regularly."
    ],
    "Academic": [
        "Lecture cancelled without prior notice.",
        "Assignments not accepted on portal.",
        "Clash in exam schedule.",
        "Labs don’t have required equipment.",
        "Syllabus was incomplete before exam."
    ],
    "Finance": [
        "Fee shows unpaid despite payment.",
        "Scholarship status not updated.",
        "Wrong fee breakdown shown online.",
        "Refund pending for over a month.",
        "No invoice received after payment."
    ],
    "Library": [
        "Books for ML course are missing.",
        "No seats available in reading area.",
        "Library catalog not working.",
        "Staff refused to issue available book.",
        "Wi-Fi weak in library hall."
    ],
    "Admin/HR": [
        "No update on bonafide request.",
        "Admin office closed during hours.",
        "Internship form not processed.",
        "No one available for form help.",
        "ID card not issued after 2 weeks."
    ]
}

# Generate 20 samples per category
data = {"Complaint": [], "Category": []}
for category, examples in complaint_templates.items():
    for _ in range(20):
        data["Complaint"].append(random.choice(examples))
        data["Category"].append(category)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("complaints_dataset.csv", index=False)

print("✅ Dataset created and saved as 'complaints_dataset.csv'")
