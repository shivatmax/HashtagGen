<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" width="100" />
</p>
<p align="center">
    <h1 align="center">HASHTAGGEN</h1>
</p>
<p align="center">
    <em>HashtagGen: Spark Your Content with AI-Powered Tags!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/shivatmax/HashtagGen?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/shivatmax/HashtagGen?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/shivatmax/HashtagGen?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/shivatmax/HashtagGen?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
<hr>

# Google colab link - https://colab.research.google.com/drive/17EnVT2702LGwPDUZuAC3RziAXF2lAr5d?authuser=3#scrollTo=ay5aekVLwa3E

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running HashtagGen](#-running-HashtagGen)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

HashtagGen is an AI-driven web application designed to generate relevant hashtags for images by utilizing advanced generative AI, language processing techniques, and vision APIs. It streamlines the process of creating engaging tags for social media content, leveraging the power of AI tools like Langchain and CrewAI to interpret visuals and suggest optimal hashtags that resonate with the target audience, thus enhancing online visibility and interaction. With its easy-to-use interface and the integration of environmental management and web search capabilities, HashtagGen serves as a valuable tool for marketers, social media managers, and content creators seeking to maximize their digital presence.

---

##  Features

|    | Feature           | Description                                                          |
|----|-------------------|----------------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project showcases a blend of AI and web technologies, primarily intended as a Streamlit application leveraging generative AI to produce hashtags. |
| 🔩 | **Code Quality**  | Code style and quality metrics cannot be directly assessed without specific benchmarks or code analysis outputs. Assuming best practices given the description. |
| 📄 | **Documentation** | The repository includes a requirements.txt and inline documentation, which are the bare minimum; comprehensive documentation may not be present. |
| 🔌 | **Integrations**  | Integrations include AI & vision APIs for keyword generation and Streamlit for the web interface, indicating a web-based AI application. |
| 🧩 | **Modularity**    | With separate configuration (`requirements.txt`) and execution (`app.py`) files, the project suggests a degree of modularity, potentially allowing for reuse and expansion. |
| 🧪 | **Testing**       | No explicit mention of testing frameworks or tools; project may lack formalized testing. |
| ⚡️  | **Performance**   | Performance metrics are not described; efficiency will depend on underlying APIs' response times and the optimization of the app itself. |
| 🛡️ | **Security**      | Without explicit security measures detailed, the project may rely on the inherent security features of the integrated APIs and frameworks. |
| 📦 | **Dependencies**  | Key dependencies include `google-generativeai`, `duckduckgo_search`, `langchain-google-genai`, `langchain_community`, `crewai`, and `streamlit`, providing a mix of AI, search, and web app capabilities. |
| 🚀 | **Scalability**   | The scalability largely relies on the performance of the infrastructures like Google AI services and how well Streamlit handles concurrent users; not assessed directly. |


---

##  Repository Structure

```sh
└── HashtagGen/
    ├── README.md
    ├── app.py
    └── requirements.txt
```

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Installation

1. Clone the HashtagGen repository:

```sh
git clone https://github.com/shivatmax/HashtagGen
```

2. Change to the project directory:

```sh
cd HashtagGen
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running HashtagGen

Use the following command to run HashtagGen:

```sh
streamlit run app.py
```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/shivatmax/HashtagGen/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/shivatmax/HashtagGen/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/shivatmax/HashtagGen/issues)**: Submit bugs found or log feature requests for Hashtaggen.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/shivatmax/HashtagGen
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

---
