import random

QUESTION_BANK = {
    "Python": {
        "Beginner": [
            {
                "question": "What is Python and what are its main features?",
                "keywords": ["interpreted", "readable", "high level"],
                "reference_answer": (
                    "Python is a high-level interpreted programming "
                    "language known for its simple syntax, readability "
                    "and large collection of libraries."
                )
            },
            {
                "question": "What is the difference between a list and a tuple?",
                "keywords": ["mutable", "immutable", "list", "tuple"],
                "reference_answer": (
                    "A list is mutable, meaning its elements can be "
                    "changed after creation. A tuple is immutable "
                    "and cannot be modified after creation."
                )
            }
        ],
        "Intermediate": [
            {
                "question": "Explain the difference between shallow copy and deep copy.",
                "keywords": ["shallow", "deep", "nested", "copy"],
                "reference_answer": (
                    "A shallow copy creates a new object but shares "
                    "references to nested objects. A deep copy creates "
                    "independent copies of nested objects as well."
                )
            },
            {
                "question": "What are decorators in Python?",
                "keywords": ["function", "wrapper", "decorator"],
                "reference_answer": (
                    "Decorators are functions that modify or extend "
                    "the behaviour of another function without "
                    "changing its original source code. They commonly "
                    "use wrapper functions."
                )
            }
        ],
        "Advanced": [
            {
                "question": "Explain Python generators and the yield keyword.",
                "keywords": ["generator", "yield", "iterator"],
                "reference_answer": (
                    "Generators are special iterators that produce "
                    "values one at a time. The yield keyword pauses "
                    "function execution and preserves its state."
                )
            }
        ]
    },

    "Java": {
        "Beginner": [
            {
                "question": "What is the JVM in Java?",
                "keywords": ["java", "virtual machine", "bytecode"],
                "reference_answer": (
                    "JVM stands for Java Virtual Machine. It executes "
                    "Java bytecode and helps Java programs run on "
                    "different platforms."
                )
            }
        ],
        "Intermediate": [
            {
                "question": "Explain method overloading and method overriding.",
                "keywords": ["overloading", "overriding", "polymorphism"],
                "reference_answer": (
                    "Method overloading means defining methods with "
                    "the same name but different parameters. Method "
                    "overriding occurs when a subclass provides its "
                    "own implementation of a parent class method."
                )
            }
        ],
        "Advanced": [
            {
                "question": "Explain multithreading in Java.",
                "keywords": ["thread", "concurrency", "parallel"],
                "reference_answer": (
                    "Multithreading allows multiple threads to execute "
                    "within one program. It supports concurrent tasks "
                    "and can improve application responsiveness."
                )
            }
        ]
    },

    "C++": {
        "Beginner": [
            {
                "question": "What is the difference between C and C++?",
                "keywords": ["object", "oriented", "procedural"],
                "reference_answer": (
                    "C is mainly a procedural programming language, "
                    "while C++ supports both procedural and "
                    "object-oriented programming."
                )
            }
        ],
        "Intermediate": [
            {
                "question": "Explain the four pillars of OOP.",
                "keywords": ["inheritance", "polymorphism", "encapsulation", "abstraction"],
                "reference_answer": (
                    "The four pillars of object-oriented programming "
                    "are inheritance, polymorphism, encapsulation "
                    "and abstraction. They support code reuse, "
                    "flexibility and data protection."
                )
            }
        ],
        "Advanced": [
            {
                "question": "What are virtual functions in C++?",
                "keywords": ["virtual", "override", "runtime", "polymorphism"],
                "reference_answer": (
                    "A virtual function is a member function declared "
                    "using the virtual keyword. It supports runtime "
                    "polymorphism by allowing overridden functions "
                    "to be selected dynamically."
                )
            }
        ]
    },

    "SQL": {
        "Beginner": [
            {
                "question": "What is SQL and what is a primary key?",
                "keywords": ["database", "query", "unique", "primary key"],
                "reference_answer": (
                    "SQL stands for Structured Query Language and is "
                    "used to manage relational databases. A primary "
                    "key uniquely identifies each record in a table."
                )
            }
        ],
        "Intermediate": [
            {
                "question": "Explain the difference between INNER JOIN and LEFT JOIN.",
                "keywords": ["inner join", "left join", "matching", "rows"],
                "reference_answer": (
                    "INNER JOIN returns rows with matching values "
                    "in both tables. LEFT JOIN returns all rows from "
                    "the left table and matching rows from the right "
                    "table, using NULL when there is no match."
                )
            }
        ],
        "Advanced": [
            {
                "question": "What are database indexes?",
                "keywords": ["index", "search", "performance"],
                "reference_answer": (
                    "A database index is a data structure that helps "
                    "retrieve records faster. It improves search "
                    "performance but can require extra storage "
                    "and slow down some write operations."
                )
            }
        ]
    },

    "HR": {
        "Beginner": [
            {
                "question": "Tell me about yourself.",
                "keywords": ["education", "skills", "projects", "goals"],
                "reference_answer": (
                    "I am a computer science student. I have learned "
                    "programming and developed projects to improve "
                    "my practical skills. My goal is to become a "
                    "software developer and contribute to real projects."
                )
            }
        ],
        "Intermediate": [
            {
                "question": "Why should we hire you?",
                "keywords": ["skills", "strengths", "contribute", "learn"],
                "reference_answer": (
                    "You should hire me because I have a strong "
                    "interest in learning, problem-solving skills "
                    "and programming knowledge. I am willing to "
                    "contribute to the team and improve continuously."
                )
            }
        ],
        "Advanced": [
            {
                "question": "Describe a challenging situation and how you handled it.",
                "keywords": ["challenge", "problem", "solution", "result"],
                "reference_answer": (
                    "I faced a challenging problem during a project. "
                    "I analysed the problem, divided it into smaller "
                    "tasks, tested possible solutions and completed "
                    "the task through consistent effort."
                )
            }
        ]
    }
}


def get_random_question(subject, difficulty):
    questions = QUESTION_BANK.get(subject, {}).get(difficulty, [])

    if not questions:
        return None

    return random.choice(questions)