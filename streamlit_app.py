import streamlit as st
from sqlalchemy import create_engine, Column, Integer, Boolean, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up database
DATABASE_URL = "sqlite:///syllabus_tracker.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class UserProgress(Base):
    __tablename__ = 'user_progress'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    completed_topics = Column(String)  # Store completed topics as a comma-separated string

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Function to load user progress from the database
def load_progress(email):
    session = Session()
    user = session.query(UserProgress).filter_by(email=email).first()
    if user:
        completed = user.completed_topics.split(',') if user.completed_topics else []
        return {section: [topic in completed for topic in topics] for section, topics in syllabus.items()}
    return {section: [False] * len(topics) for section, topics in syllabus.items()}

# Function to save user progress to the database
def save_progress(email, completed_topics):
    session = Session()
    user = session.query(UserProgress).filter_by(email=email).first()
    if user:
        user.completed_topics = ','.join(completed_topics)
    else:
        user = UserProgress(email=email, completed_topics=','.join(completed_topics))
        session.add(user)
    session.commit()

# Syllabus structure with sections and sub-topics
syllabus = {
    "Probability and Statistics": [
        "Counting (permutation and combinations)", "Probability axioms", "Sample space, events",
        "Independent events", "Mutually exclusive events", "Marginal, conditional and joint probability",
        "Bayes Theorem", "Conditional expectation and variance", "Mean, median, mode, and standard deviation",
        "Correlation and covariance", "Random variables", "Discrete random variables and probability mass functions",
        "Uniform, Bernoulli, binomial distribution", "Continuous random variables and probability distribution function",
        "Uniform, exponential, Poisson", "Normal, standard normal", "t-distribution, chi-squared distributions",
        "Cumulative distribution function", "Conditional PDF", "Central limit theorem", "Confidence interval",
        "z-test, t-test, chi-squared test"
    ],
    "Linear Algebra": [
        "Vector space", "Subspaces", "Linear dependence and independence of vectors", "Matrices",
        "Projection matrix", "Orthogonal matrix", "Idempotent matrix", "Partition matrix and their properties",
        "Quadratic forms", "Systems of linear equations and solutions", "Gaussian elimination",
        "Eigenvalues and eigenvectors", "Determinant", "Rank", "Nullity", "Projections", "LU decomposition",
        "Singular value decomposition"
    ],
    "Calculus and Optimization": [
        "Functions of a single variable", "Limit", "Continuity and differentiability", "Taylor series",
        "Maxima and minima", "Optimization involving a single variable"
    ],
    "Programming, Data Structures and Algorithms": [
        "Programming in Python", "Stacks", "queues", "linked lists", " trees", "hash tables",
        "Linear search and binary search", "Selection sort", "Bubble sort ", "Insertion sort",
        "Divide and conquer: mergesort ", "Divide and conquer: quicksort", "Introduction to graph theory", "Graph algorithms: traversals, shortest path"
    ],
    "Database Management and Warehousing": [
        "ER-model", "Relational model: relational algebra, tuple calculus", "SQL", "Integrity constraints",
        "Normal form", "File organization", "Indexing", "Data types", "Data transformation: normalization, discretization, sampling, compression",
        "Data warehouse modelling: schema for multidimensional data models", "Concept hierarchies", "Measures: categorization and computations"
    ],
    "Machine Learning": [
        "Supervised Learning: Simple linear regression", "Multiple linear regression",
        "Ridge regression", "Classification: Logistic regression", "K-nearest neighbour", "Naive Bayes classifier",
        "Linear discriminant analysis", "Support vector machine", "Decision trees", "Bias-variance trade-off",
        "Cross-validation: leave-one-out, k-folds", "Multi-layer perceptron", "Feed-forward neural network",
        "Unsupervised Learning: clustering algorithms", "K-means/k-medoid", "Hierarchical clustering",
        "Dimensionality reduction: PCA"
    ],
    "Artificial Intelligence": [
        "Search: informed",
        "Search: uninformed",
        "Search: adversarial",
        "Logic: propositional",
        "Logic: predicate",
        "Reasoning under uncertainty: conditional independence representation",
        "Exact inference through variable elimination", "approximate inference through sampling. "
    ],
    "General Aptitude (GA)": [
        "VERBAL APTITUDE: 1.1 Basic English Grammar",
        "1.2 Basic Vocabulary",
        "1.3 Reading and Comprehension",
        "1.4 Narrative Sequencing",

        "QUANTITATIVE APTITUDE: 2.1 Data Interpretation",
        "2.1.1 Data Graphs (Bar Graphs, Pie Charts, etc.)",
        "2.1.2 2- and 3-Dimensional Plots",
        "2.1.3 Maps and Tables",
        "2.2 Numerical Computation and Estimation",
        "2.2.1 Ratios",
        "2.2.2 Percentages",
        "2.2.3 Powers and Exponents",
        "2.2.4 Logarithms",
        "2.2.5 Permutations and Combinations",
        "2.2.6 Series",
        "2.3 Mensuration and Geometry",
        "2.4 Elementary Statistics and Probability",

        "ANALYTICAL APTITUDE: 3.1 Logic",
        "3.1.1 Deduction and Induction",
        "3.2 Analogy",
        "3.3 Numerical Relations and Reasoning",

        "SPATIAL APTITUDE: 4.1 Transformation of Shapes",
        "4.1.1 Translation",
        "4.1.2 Rotation",
        "4.1.3 Scaling",
        "4.1.4 Mirroring",
        "4.1.5 Assembling and Grouping",
        "4.2 Paper Folding and Cutting",
        "4.3 Patterns in 2 and 3 Dimensions"
    ]
}

# Streamlit app
st.title("GATE Syllabus Tracker")
st.write("Mark the topics you completed on the check box and track your percentage of completion on the sidebar.")

# User email input
email = st.text_input("Enter your email to track your progress:")
if email:
    # Load user progress
    completed_topics = load_progress(email)

    # Track total topics and completed topics
    total_topics = sum(len(topics) for topics in syllabus.values())
    completed_count = 0

    # Sidebar progress
    with st.sidebar:
        st.header("Progress Tracker")
        progress = (completed_count / total_topics) * 100 if total_topics else 0
        st.write(f"Overall Progress: {progress:.2f}%")
        st.progress(progress / 100)

    # Render each section with collapsible topics
    for section, topics in syllabus.items():
        with st.expander(section):
            for i, topic in enumerate(topics):
                # Display checkbox and update state
                if st.checkbox(topic, key=f"{section}_{i}", value=completed_topics[section][i]):
                    completed_topics[section][i] = True

    # Save progress on button click
    if st.button("Save Progress"):
        save_progress(email, [topic for section, topics in completed_topics.items() for topic in topics if topic])
        st.success("Progress saved successfully!")

else:
    st.warning("Please enter your email to track progress.")
