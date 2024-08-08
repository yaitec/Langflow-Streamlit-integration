<div align="center" style="padding: 10px; border: 1px solid #ccc; background-color: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">
    <h2 style="margin: 0; font-size: 24px; color: #333;">Langflow Integration with Streamlit</h2>
    <p style="margin: 5px 0 0 0; font-size: 16px; color: #666;">Seamlessly integrate Streamlit components within Langflow</p>
</div>


<p align="center"><strong>
    Integrate Streamlit for interactive web applications with Langflow
</strong></p>
<p align="center" style="font-size: 12px;">
    Open-source, Python-powered, fully customizable integration for a seamless user experience
</p>


<p align="center">
    <a href="https://github.com/yaitec/Langflow-Streamlit">
        <img src="https://img.shields.io/github/stars/yaitec/Langflow-Streamlit">
    </a>
</p>



# 📝 Content

- [Running Langflow from a Cloned Repository](#running-langflow-with-streamlit-integration-from-a-cloned-repository)
- [How to get Streamlit's Flows from the store](#how-to-get-streamlits-flows-from-store)
- [Using Streamlit Components in Langflow](#using-streamlit-components-in-langflow)
- [Streamlit's Components](#streamlits-components)
- [👋 Contribute](#-contribute)
- [🌟 Contributors](#-contributors)
- [📄 License](#-license)

# Running Langflow with Streamlit integration from a cloned repository

If you prefer to run Langflow from a cloned repository rather than installing it via pip, follow these steps:

1. **Clone the Repository**

First, clone the Langflow repository from GitHub:

```shell
git clone https://github.com/yaitec/Langflow-Streamlit.git
```

Navigate into the cloned directory:

```shell
cd Langflow-Streamlit
```

2. **Install Dependencies and run**

To install the frontend and backend dependencies and run both, use the following commands:

```shell
make run
```

# How to get Streamlit's Flows from the store
The gif below shows how to search, download, and run Streamlit's flow:
<p align="center">
  <img src="./docs/static/img/streamlit/streamlit_how_to_get_flows.gif" alt="Your GIF" style="border: 3px solid #211C43;">
</p>

# Using Streamlit Components in Langflow
The gif below shows how to use `Listen` and `Send` components:
<p align="center">
  <img src="./docs/static/img/streamlit/streamlit_how_to_connect_components.gif" alt="Your GIF" style="border: 3px solid #211C43;">
</p>

# Streamlit's Components

Langflow provides the following Streamlit components:

- **[Send](./send.md)**: Send messages to a Streamlit chat session.
- **[Listen](./listen.md)**: Listen for incoming messages in a Streamlit chat, altering the layout of the Streamlit application.

# 👋 Contribute

We welcome contributions from developers of all levels to our open-source project on GitHub. If you'd like to contribute, please check our [contributing guidelines](./CONTRIBUTING.md) and help make Langflow more accessible.

---

[![Star History Chart](https://api.star-history.com/svg?repos=yaitec/Langflow-Streamlit&type=Timeline)](https://star-history.com/#yaitec/Langflow-Streamlit&Date)

# 🌟 Contributors

[![langflow streamlit contributors](https://contrib.rocks/image?repo=yaitec/Langflow-Streamlit)](https://github.com/yaitec/Langflow-Streamlit/graphs/contributors)

# 📄 License

Langflow is released under the MIT License. See the [LICENSE](LICENSE) file for details.
