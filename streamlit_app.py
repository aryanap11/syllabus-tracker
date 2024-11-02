import streamlit as st

# Title and introductory text
st.title("GATE DA Syllabus Tracker")
st.write("Mark the topics you completed on the checkbox and track your percentage of completion in the sidebar.")



# Syllabus structure with collapsible sections
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
        "Programming in Python", "Stacks", "queues", "linked lists", "trees", "hash tables",
        "Linear search and binary search", "Selection sort", "Bubble sort", "Insertion sort",
        "Divide and conquer: mergesort", "Divide and conquer: quicksort", "Introduction to graph theory", "Graph algorithms: traversals, shortest path"
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

# Initialize a session state to store completed topics
if "completed_topics" not in st.session_state:
    st.session_state.completed_topics = {
        section: [False] * len(topics) for section, topics in syllabus.items()}

# Track total topics and completed topics
total_topics = sum(len(topics) for topics in syllabus.values())
completed_topics = 0

# Sidebar for progress and subjects
with st.sidebar:
    # Calculate completed topics
    for section, topics in syllabus.items():
        for i in range(len(topics)):
            if st.session_state.completed_topics[section][i]:
                completed_topics += 1

    # Calculate and display progress
    progress = (completed_topics / total_topics) * 100
    st.write(f"**Overall Progress: {progress:.2f}% completed**")
    st.progress(progress / 100)


# Main display area
selected_section = st.session_state.get("selected_section", None)
st.header("GATE DA Syllabus")
for section, topics in syllabus.items():
    with st.expander(section):
        for i, topic in enumerate(topics):
            # Display checkbox and update state
            if st.checkbox(topic, key=f"{section}_{i}"):
                st.session_state.completed_topics[section][i] = True
