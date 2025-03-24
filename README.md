# GradeWise - Student Performance Evaluation System

GradeWise is a web-based application built with Flask that streamlines the process of evaluating student performance. It allows teachers to input student details and scores, calculates average scores, assigns grades, and generates personalized feedback. The system also provides printable performance reports with a professional watermark for easy record-keeping.

## Features
- **Dynamic Grade Calculation:** Automatically calculates average scores and assigns grades based on performance.
- **Personalized Feedback:** Provides customized feedback according to the assigned grade.
- **Responsive Design:** Optimized for mobile and desktop devices, ensuring usability on all screen sizes.
- **Printable Reports:** Generates print-ready evaluation reports with a centered watermark.
- **Clean and Formal Interface:** Designed with a professional appearance suitable for educational settings.

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Styling:** Custom CSS with responsive design
- **Template Engine:** Jinja2

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gradewise.git
   cd gradewise
   ```
2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   flask run
   ```
5. Access the application at:
   ```http://127.0.0.1:5000/
   ```

## Usage
- Enter the student’s name, age, ID, and scores for each subject.
- Click **Evaluate** to view the performance report.
- Print the evaluation using the **Print** button on the results page.
- Start a new evaluation using the **New Evaluation** button.

## Project Structure
- `app.py`: Main Flask application file.
- `templates/`: HTML templates for the user interface.
- `static/`: Folder for images (including the logo) and CSS files.
- `requirements.txt`: Python package dependencies.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss improvements or fixes.

## License
This project is licensed under the MIT License.

