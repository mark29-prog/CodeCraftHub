from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# JSON file used for storage
COURSES_FILE = "courses.json"

# Valid course status values
VALID_STATUSES = [
    "Not Started",
    "In Progress",
    "Completed"
]


# --------------------------------------------------
# Create courses.json automatically if it doesn't exist
# --------------------------------------------------
def initialize_file():
    if not os.path.exists(COURSES_FILE):
        try:
            with open(COURSES_FILE, "w") as file:
                json.dump([], file)
        except Exception as e:
            print(f"Error creating file: {e}")


# --------------------------------------------------
# Read all courses from JSON file
# --------------------------------------------------
def load_courses():
    try:
        with open(COURSES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        initialize_file()
        return []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")


# --------------------------------------------------
# Save courses to JSON file
# --------------------------------------------------
def save_courses(courses):
    try:
        with open(COURSES_FILE, "w") as file:
            json.dump(courses, file, indent=4)
    except Exception as e:
        raise Exception(f"Error writing file: {str(e)}")


# --------------------------------------------------
# Validate course data
# --------------------------------------------------
def validate_course_data(data):
    required_fields = [
        "name",
        "description",
        "target_date",
        "status"
    ]

    # Check required fields
    for field in required_fields:
        if field not in data or not data[field]:
            return f"'{field}' is required"

    # Validate status
    if data["status"] not in VALID_STATUSES:
        return (
            f"Invalid status. Must be one of: "
            f"{', '.join(VALID_STATUSES)}"
        )

    # Validate date format
    try:
        datetime.strptime(data["target_date"], "%Y-%m-%d")
    except ValueError:
        return "target_date must be in YYYY-MM-DD format"

    return None


# --------------------------------------------------
# Generate next course ID
# --------------------------------------------------
def generate_next_id(courses):
    if not courses:
        return 1

    return max(course["id"] for course in courses) + 1


# --------------------------------------------------
# POST /api/courses
# Add a new course
# --------------------------------------------------
@app.route("/api/courses", methods=["POST"])
def create_course():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is required"
            }), 400

        validation_error = validate_course_data(data)

        if validation_error:
            return jsonify({
                "error": validation_error
            }), 400

        courses = load_courses()

        new_course = {
            "id": generate_next_id(courses),
            "name": data["name"],
            "description": data["description"],
            "target_date": data["target_date"],
            "status": data["status"],
            "created_at": datetime.now().isoformat()
        }

        courses.append(new_course)
        save_courses(courses)

        return jsonify({
            "message": "Course created successfully",
            "course": new_course
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# --------------------------------------------------
# GET /api/courses
# Get all courses
# --------------------------------------------------
@app.route("/api/courses", methods=["GET"])
def get_courses():
    try:
        courses = load_courses()

        return jsonify({
            "count": len(courses),
            "courses": courses
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# --------------------------------------------------
# GET /api/courses/<id>
# Get a specific course
# --------------------------------------------------
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    try:
        courses = load_courses()

        course = next(
            (c for c in courses if c["id"] == course_id),
            None
        )

        if not course:
            return jsonify({
                "error": "Course not found"
            }), 404

        return jsonify(course), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# --------------------------------------------------
# PUT /api/courses/<id>
# Update a course
# --------------------------------------------------
@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is required"
            }), 400

        validation_error = validate_course_data(data)

        if validation_error:
            return jsonify({
                "error": validation_error
            }), 400

        courses = load_courses()

        course = next(
            (c for c in courses if c["id"] == course_id),
            None
        )

        if not course:
            return jsonify({
                "error": "Course not found"
            }), 404

        course["name"] = data["name"]
        course["description"] = data["description"]
        course["target_date"] = data["target_date"]
        course["status"] = data["status"]

        save_courses(courses)

        return jsonify({
            "message": "Course updated successfully",
            "course": course
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# --------------------------------------------------
# DELETE /api/courses/<id>
# Delete a course
# --------------------------------------------------
@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    try:
        courses = load_courses()

        course = next(
            (c for c in courses if c["id"] == course_id),
            None
        )

        if not course:
            return jsonify({
                "error": "Course not found"
            }), 404

        courses.remove(course)
        save_courses(courses)

        return jsonify({
            "message": "Course deleted successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# --------------------------------------------------
# Application Entry Point
# --------------------------------------------------
if __name__ == "__main__":
    initialize_file()

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )