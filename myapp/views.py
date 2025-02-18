from django.shortcuts import render

# Create your views here.
def cv_view(request):
    context = {
        "name": "Chetan Goel",
        "email": "cg4652@nyu.edu",
        "phone": "(617)-286-9114",
        "linkedin": "https://www.linkedin.com/in/goelchetan",
        "github": "https://github.com/chetangoel01",
        "education": {
            "nyu": {
                "degree": "Master of Science, Computer Science",
                "university": "New York University",
                "graduation": "May 2026",
                "coursework": "Algorithms, Principles of Database Systems, Foundations of Data Science",
            },
            "umass": {
                "degree": "Bachelor of Science, Computer Science",
                "university": "University of Massachusetts Amherst",
                "graduation": "May 2023",
                "gpa": "3.91",
                "distinctions": "Cum Laude, Dean’s List (All Semesters), Chancellor’s Award Scholarship",
                "coursework": "Algorithms, Artificial Intelligence, Machine Learning, Data Structures",
            },
        },
        "experience": [
            {
                "title": "Software Engineering Intern",
                "company": "Buhler Aeroglide",
                "location": "Cary, NC",
                "start_date": "August 2023",
                "end_date": "April 2024",
                "responsibilities": [
                    "Developed a web application using React and Java.",
                    "Contributed to the design and implementation of data management strategies.",
                ],
            },
            {
                "title": "Software Engineering Intern",
                "company": "Cisco Systems Inc.",
                "location": "San Jose, CA",
                "start_date": "May 2022",
                "end_date": "August 2022",
                "responsibilities": [
                    "Designed a framework for eliminating flaky tests in Jenkins pipelines.",
                    "Developed a Kibana dashboard to track test automation results in real time.",
                ],
            },
            {
                "title": "Software Engineering Intern",
                "company": "Cisco Systems Inc.",
                "location": "San Jose, CA",
                "start_date": "May 2022",
                "end_date": "August 2022",
            },
        ],
        "projects": [
            {
                "name": "UKG Employee Goal Manager",
                "year": "2023",
                "details": [
                    "Developed a full-stack web application using React and Flask.",
                    "Integrated MongoDB for efficient data management.",
                ],
            },
            {
                "name": "Emotion Detection Bot",
                "year": "2022",
                "details": [
                    "Built an emotion detection program using GANs and OpenCV.",
                    "Recommended music based on detected emotions.",
                ],
            },
        ],
        "skills": {
            "languages": "JavaScript/TypeScript, Java, C, C++, HTML/CSS, Python, C#, R, React.js, NodeJS, Unity, Flask",
            "tools": "Git, Jenkins, AWS, Confluence, Jira, Figma, Zsh, ElasticSearch, Kibana",
        },
    }
    
    return render(request, "cv_template.html", context)
