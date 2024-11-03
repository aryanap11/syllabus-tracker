import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from streamlit_option_menu import option_menu


# Configure Streamlit page
st.set_page_config(
    page_title="Syllabus Tracker",
    page_icon="📝",
    layout="wide",
)


def show_feedback():
    st.write("🔗 Connect with me on:")
    st.markdown(
        "[LinkedIn](https://www.linkedin.com/in/aryanpatel11) | [GitHub](https://github.com/aryanap11)")

    st.title("Thank Me Here 😁")
    st.write("🎉 Hey there, I'm Aryan! I made this app just for you all! If you enjoyed it, feel free to thank me or share your thoughts below! 😊💬")

    # Embed Google Form using Markdown
    st.markdown(
        """<style>
    /* Container */
    .form-container {
        max-width: 400px;
        margin: 0;
    }

    /* Labels */
    label {
        display: block;
        margin-bottom: 5px;
        font-weight: bold;
    }

    /* Input fields and textarea */
    input[type="text"],
    input[type="email"],
    textarea {
        width: 100%;
        padding: 8px;
        margin-bottom: 15px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }

    /* Button */
    button[type="submit"] {
        background-color: #4caf50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    button[type="submit"]:hover {
        background-color: #45a049;
    }
</style>

<div class="form-container">
<form action="https://submit-form.com/IzNJLEA6n">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" placeholder="Name" required="" />
        <label for="message">Your Message</label>
        <textarea
            id="message"
            name="message"
            placeholder="Message"
            required=""
        ></textarea>
        <button type="submit">Send</button>
    </form>
</div>

        """, unsafe_allow_html=True)


# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///syllabus_tracker.db')
Session = sessionmaker(bind=engine)


class UserProgress(Base):
    __tablename__ = 'user_progress'
    email = Column(String, primary_key=True)
    completed_topics = Column(String)


Base.metadata.create_all(engine)

# Sample syllabus data (replace with your actual syllabus)
syllabus = {
    "Probability and Statistics": [
        "Counting (permutation and combinations)", "Probability axioms", "Sample space-events",
        "Independent events", "Mutually exclusive events", "Marginal-conditional and joint probability",
        "Bayes Theorem", "Conditional expectation and variance", "Mean-median-mode and standard deviation",
        "Correlation and covariance", "Random variables", "Discrete random variables and probability mass functions",
        "Uniform-Bernoulli-binomial distribution", "Continuous random variables and probability distribution function",
        "Uniform-exponential-Poisson", "Normal-standard normal", "t-distribution-chi-squared distributions",
        "Cumulative distribution function", "Conditional PDF", "Central limit theorem", "Confidence interval",
        "z-test-t-test-chi-squared test"
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
        "Programming in Python", "Stacks", "queues", "linked lists", "trees", "hash tables",
        "Linear search and binary search", "Selection sort", "Bubble sort", "Insertion sort",
        "Divide and conquer: mergesort", "Divide and conquer: quicksort", "Introduction to graph theory", "Graph algorithms: traversals-shortest path"
    ],
    "Database Management and Warehousing": [
        "ER-model", "Relational model: relational algebra-tuple calculus", "SQL", "Integrity constraints",
        "Normal form", "File organization", "Indexing", "Data types", "Data transformation: normalization-discretization-sampling-compression",
        "Data warehouse modelling: schema for multidimensional data models", "Concept hierarchies", "Measures: categorization and computations"
    ],
    "Machine Learning": [
        "Supervised Learning: Simple linear regression", "Multiple linear regression",
        "Ridge regression", "Classification: Logistic regression", "K-nearest neighbour", "Naive Bayes classifier",
        "Linear discriminant analysis", "Support vector machine", "Decision trees", "Bias-variance trade-off",
        "Cross-validation: leave-one-out-k-folds", "Multi-layer perceptron", "Feed-forward neural network",
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
        "Exact inference through variable elimination", "approximate inference through sampling."
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


def save_progress(email, completed_topics):
    session = Session()
    try:
        user = session.query(UserProgress).filter_by(email=email).first()

        # Flatten completed_topics dictionary into a list of completed topic names
        completed_topics_list = [
            syllabus[section][i]  # Get the full topic name as a single string
            for section, topics in completed_topics.items()
            for i, completed in enumerate(topics)
            if completed
        ]

        # Join topics as single strings, not character by character
        if user:
            # Save as comma-separated string of full topic names
            user.completed_topics = ','.join(completed_topics_list)
        else:
            user = UserProgress(
                email=email, completed_topics=','.join(completed_topics_list))
            session.add(user)

        session.commit()
    except Exception as e:
        st.error(f"Error saving progress: {str(e)}")


def load_progress(email):
    session = Session()
    user = session.query(UserProgress).filter_by(email=email).first()
    if user:
        completed_topics = user.completed_topics.split(
            ',')  # Split into a list
        completed_dict = {
            section: [False] * len(topics) for section, topics in syllabus.items()}

        for topic in completed_topics:
            for section, topics in syllabus.items():
                if topic in topics:
                    index = topics.index(topic)
                    completed_dict[section][index] = True

        return completed_dict
    else:
        return {section: [False] * len(topics) for section, topics in syllabus.items()}


# Streamlit app
# Main app function
def main_app():
    # Streamlit app
    st.title("GATE Syllabus Tracker")
    st.write("Mark the topics you completed on the check box and track your percentage of completion on the sidebar.")

    # User email input
    email = st.text_input("Enter your email to track your progress:").strip()
    if email:
        completed_topics = load_progress(email)

        total_topics = sum(len(topics) for topics in syllabus.values())
        completed_count = sum(
            sum(completed_topics[section]) for section in completed_topics)

        progress = (completed_count / total_topics) * \
            100 if total_topics else 0
        st.write(f"Overall Progress: {progress:.2f}%")
        st.progress(progress / 100)

        for section, topics in syllabus.items():
            with st.expander(section):
                for i, topic in enumerate(topics):
                    # Initialize checkboxes with current completion state
                    if section in completed_topics and len(completed_topics[section]) > i:
                        completed_state = completed_topics[section][i]
                    else:
                        completed_state = False

                    if st.checkbox(topic, key=f"{section}_{i}", value=completed_state):
                        completed_topics[section][i] = True

        if st.button("Save Progress"):
            save_progress(email, completed_topics)
            st.success("Progress saved successfully!")
    else:
        st.warning("Please enter your email to track progress.")

def main():
    with st.sidebar:
        selected_page = option_menu("Navigation", ["Syllabus Tracker", "Thank Me here"],
                                icons=['list-task', 'chat-left-text'],
                                menu_icon="cast", default_index=0, orientation="vertical")
        selected_page

# Navigation logic
    if selected_page == "Syllabus Tracker":
        main_app()
    elif selected_page == "Thank Me here":
        show_feedback()

if __name__ == "__main__":
    main()
