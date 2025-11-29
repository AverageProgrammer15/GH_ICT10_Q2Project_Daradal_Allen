from pyscript import *

school_data = {
    "school_name": "Springfield High School",
    "school_address": "123 Main St, Springfield, USA",
    "desc_id": "Springfield High School is committed to providing quality education and fostering a supportive learning environment for all students.",
    "mission_id": "To empower students to become lifelong learners and responsible citizens through academic excellence and character development.",
    "vision_id": "To be a leading educational institution recognized for innovation, inclusivity, and student success.",
    "principal_id": "Dr. Jane Smith",
    "school_type": "Public Secondary School",
    "established_id": "1985"
}

for x in school_data:
    display(school_data[x], target=x)

display(school_data["school_name"], target="footer_sname")