# 🚀 KeboolaDoc Crew

[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green?logo=python)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Powered-orange)](https://crewai.com)

A powerful multi-agent AI system built with CrewAI that analyzes Keboola data integration and transformation projects. The crew consists of specialized agents that examine source systems, integrations, and transformations to provide comprehensive analysis and documentation.

## 🛠️ Setup

### Environment Configuration

Copy the environment template and configure your variables:

```bash
cp .env.dist .env
```

Edit the `.env` file and fill in the appropriate values for all required variables. Examples are provided in the `.env.dist` file.

## 🚀 Running the Project

Launch your crew of AI agents:

```bash
docker-compose run crew
```

This command initializes the KeboolaDoc Crew using Docker, assembling the agents and assigning them tasks as defined in your configuration.

## 📊 What the Crew Does

The KeboolaDoc Crew consists of two specialized AI agents:

- **Data Integration Expert**: Analyzes source systems and data integration patterns
- **Transformation Expert**: Examines data transformations and processing logic

The crew performs sequential analysis of your Keboola project and generates comprehensive reports.

## 📁 Output

All analysis results are saved to the `output/` folder:

- `output/integrations.txt` - Source system and integration analysis
- `output/transformations.txt` - Transformation analysis and documentation

Make sure the `output/` directory exists before running the crew.

## 📁 Project Structure

```
crewai-mcp/
├── src/keboola_doc/
│   ├── config/
│   │   ├── agents.yaml    # Agent definitions
│   │   └── tasks.yaml     # Task configurations
│   ├── crew.py           # Main crew logic
│   └── main.py           # Entry point
├── output/               # Analysis results
│   ├── integrations.txt  # Integration analysis
│   └── transformations.txt # Transformation analysis
├── docker-compose.yml    # Docker configuration
├── .env.dist            # Environment template
└── README.md            # This file
```

## 🤝 Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

---

**Happy AI Collaboration! 🤖✨**
