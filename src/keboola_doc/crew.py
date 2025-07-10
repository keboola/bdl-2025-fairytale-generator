from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tools import BaseTool
from typing import List
from mcp import StdioServerParameters 
from crewai_tools import MCPServerAdapter
import os
import json

@CrewBase
class KeboolaDoc():
    """KeboolaDoc crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    def __init__(self):
        super().__init__()
        self.keboola_mcp_tools = None

    @agent
    def data_integration_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['data_integration_expert'],
            tools=self.get_keboola_mcp_tools(),
            verbose=True,
        )

    @agent
    def transformation_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['transfromation_expert'],
            tools=self.get_keboola_mcp_tools(),
            verbose=True,
        )


    @task
    def source_system_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['source_system_analysis'],
            output_file="output/integrations.txt",
            agent=self.data_integration_expert()
        )
        
    @task
    def transformation_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['transformation_analysis'], 
            output_file="output/transformations.txt",
            agent=self.transformation_expert()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the KeboolaDoc crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
    
    def get_keboola_mcp_tools(self, include_write_tools: bool = False) -> List[BaseTool]:
        if self.keboola_mcp_tools is None:
            params = StdioServerParameters(
                command="uvx",
                args=[
                                'keboola_mcp_server',
                                '--transport', 'stdio',
                                '--log-level', 'INFO',
                                '--api-url', os.getenv('KBC_STORAGE_API_URL')
                            ],
                env={"UV_PYTHON": "3.12", **os.environ},
            )
            mcp_server_adapter = MCPServerAdapter(params)
            self.keboola_mcp_tools = mcp_server_adapter.tools
        
        if include_write_tools:
            return self.keboola_mcp_tools
        else:
        # Filter tools by name starting with "list" or "get"
            filtered_tools = []
            for tool in self.keboola_mcp_tools:
                tool_name = getattr(tool, 'name', '')
                if tool_name.startswith('list') or tool_name.startswith('get'):
                    filtered_tools.append(tool)
            
            return filtered_tools
        
        
        
    
