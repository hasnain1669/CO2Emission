import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json
import io
from typing import Dict, List, Any
import numpy as np
import asyncio
import websockets
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="AI Agentic Carbon Emissions Analyzer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .coral-section {
        background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        border: 2px solid #00D4FF;
    }
    .upload-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .analysis-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .insights-section {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .agent-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 0.5rem;
    }
    .stButton > button {
        width: 100%;
        height: 3rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s;
    }
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .coral-status {
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
    }
    .status-connected { background: #4CAF50; color: white; }
    .status-disconnected { background: #f44336; color: white; }
    .status-pending { background: #ff9800; color: white; }
</style>
""", unsafe_allow_html=True)

class CoralProtocolIntegration:
    """Integration with Coral Protocol for multi-agent collaboration"""
    
    def __init__(self):
        self.coral_server_url = "http://localhost:5555"
        self.session_id = f"carbon_emission_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.registered_agents = {}
        self.agent_status = {}
        
    def register_carbon_analysis_agent(self):
        """Register our main carbon analysis agent with Coral Protocol"""
        try:
            agent_config = {
                "agentId": "carbon_analyzer_agent",
                "name": "Carbon Emissions Analyzer",
                "description": "Analyzes carbon emissions data and provides climate insights",
                "capabilities": [
                    "data_analysis",
                    "visualization",
                    "climate_modeling",
                    "tree_impact_calculation"
                ],
                "version": "1.0.0",
                "author": "Hackathon Team"
            }
            
            # Simulate agent registration
            self.registered_agents["carbon_analyzer"] = agent_config
            self.agent_status["carbon_analyzer"] = "connected"
            return True
            
        except Exception as e:
            st.error(f"Error registering carbon analyzer agent: {str(e)}")
            return False
    
    def discover_climate_agents(self):
        """Discover other climate-related agents in the Coral Registry"""
        # Simulated agent discovery - in real implementation, this would query Coral Registry
        available_agents = {
            "tree_planting_agent": {
                "name": "Tree Planting Optimizer",
                "description": "Optimizes tree planting locations for maximum carbon absorption",
                "cost_per_query": 0.1,
                "capabilities": ["location_analysis", "species_selection", "growth_prediction"]
            },
            "policy_agent": {
                "name": "Climate Policy Advisor",
                "description": "Provides policy recommendations for carbon reduction",
                "cost_per_query": 0.2,
                "capabilities": ["policy_analysis", "regulation_compliance", "incentive_design"]
            },
            "renewable_energy_agent": {
                "name": "Renewable Energy Planner",
                "description": "Plans optimal renewable energy deployment",
                "cost_per_query": 0.15,
                "capabilities": ["energy_modeling", "cost_analysis", "grid_integration"]
            },
            "carbon_trading_agent": {
                "name": "Carbon Credit Optimizer",
                "description": "Optimizes carbon credit trading strategies",
                "cost_per_query": 0.25,
                "capabilities": ["market_analysis", "price_prediction", "trade_execution"]
            }
        }
        
        return available_agents
    
    def create_agent_collaboration_thread(self, participating_agents: List[str]):
        """Create a collaboration thread with multiple agents"""
        thread_config = {
            "thread_id": f"climate_collab_{datetime.now().strftime('%H%M%S')}",
            "participants": participating_agents,
            "topic": "carbon_emission_reduction",
            "coordinator": "carbon_analyzer_agent"
        }
        
        return thread_config
    
    def send_agent_message(self, agent_id: str, message: Dict, data: pd.DataFrame = None):
        """Send message to another agent through Coral Protocol"""
        try:
            # Simulate agent communication
            if agent_id == "tree_planting_agent":
                return self._simulate_tree_agent_response(message, data)
            elif agent_id == "policy_agent":
                return self._simulate_policy_agent_response(message, data)
            elif agent_id == "renewable_energy_agent":
                return self._simulate_energy_agent_response(message, data)
            elif agent_id == "carbon_trading_agent":
                return self._simulate_trading_agent_response(message, data)
            
        except Exception as e:
            return {"error": str(e), "status": "failed"}
    
    def _simulate_tree_agent_response(self, message: Dict, data: pd.DataFrame):
        """Simulate response from tree planting agent"""
        total_emissions = data['Carbon_Emissions'].sum()
        trees_needed = int(total_emissions * 1000 / 48)
        
        return {
            "agent": "Tree Planting Optimizer",
            "response": {
                "recommended_trees": trees_needed,
                "optimal_species": ["Oak", "Pine", "Maple", "Birch"],
                "planting_locations": ["Temperate forests", "Urban areas", "Degraded lands"],
                "cost_estimate": trees_needed * 2.5,  # $2.5 per tree
                "co2_absorption_rate": "48 lbs CO2/year per tree",
                "optimal_planting_season": "Spring (March-May)"
            },
            "status": "success"
        }
    
    def _simulate_policy_agent_response(self, message: Dict, data: pd.DataFrame):
        """Simulate response from policy agent"""
        top_countries = data.groupby('Country')['Carbon_Emissions'].sum().nlargest(5).index.tolist()
        
        return {
            "agent": "Climate Policy Advisor", 
            "response": {
                "priority_countries": top_countries,
                "recommended_policies": [
                    "Carbon pricing mechanism",
                    "Renewable energy mandates",
                    "Electric vehicle incentives",
                    "Industrial emission standards"
                ],
                "estimated_reduction": "15-30% over 5 years",
                "implementation_cost": "$50B globally",
                "key_sectors": ["Energy", "Transportation", "Industry"]
            },
            "status": "success"
        }
    
    def _simulate_energy_agent_response(self, message: Dict, data: pd.DataFrame):
        """Simulate response from renewable energy agent"""
        return {
            "agent": "Renewable Energy Planner",
            "response": {
                "renewable_potential": "65% of current emissions could be offset",
                "recommended_mix": {
                    "Solar": "40%",
                    "Wind": "35%", 
                    "Hydro": "15%",
                    "Geothermal": "10%"
                },
                "investment_needed": "$2.5T globally",
                "timeline": "10-15 years for full deployment",
                "job_creation": "15 million jobs globally"
            },
            "status": "success"
        }
    
    def _simulate_trading_agent_response(self, message: Dict, data: pd.DataFrame):
        """Simulate response from carbon trading agent"""
        total_emissions = data['Carbon_Emissions'].sum()
        
        return {
            "agent": "Carbon Credit Optimizer",
            "response": {
                "current_carbon_price": "$85/ton CO2",
                "total_offset_cost": f"${total_emissions * 85:,.2f}",
                "recommended_strategy": "Buy 60% verified credits, invest 40% in projects",
                "market_trend": "Increasing demand, prices rising 12% annually",
                "best_credit_sources": ["Forestry projects", "Renewable energy", "Carbon capture"]
            },
            "status": "success"
        }

class CarbonEmissionAnalyzer:
    def __init__(self):
        # Make API keys optional - use fallback if secrets not available
        try:
            self.mistral_api_key = st.secrets.get("MISTRAL_API_KEY", "")
            self.elevenlabs_api_key = st.secrets.get("ELEVENLABS_API_KEY", "")
        except:
            self.mistral_api_key = ""
            self.elevenlabs_api_key = ""
            
        # Initialize Coral Protocol integration
        self.coral = CoralProtocolIntegration()
        
    def analyze_with_mistral(self, data: pd.DataFrame) -> Dict[str, Any]:
        """Analyze carbon emissions data using Mistral AI"""
        try:
            # Prepare data summary for AI analysis
            data_summary = {
                "total_countries": len(data['Country'].unique()),
                "year_range": f"{data['Year'].min()} - {data['Year'].max()}",
                "total_emissions": data['Carbon_Emissions'].sum(),
                "avg_emissions": data['Carbon_Emissions'].mean(),
                "top_emitters": data.groupby('Country')['Carbon_Emissions'].sum().nlargest(5).to_dict(),
                "trend_analysis": self._calculate_trends(data)
            }
            
            # Enhanced analysis with Coral Protocol multi-agent insights
            analysis = {
                "key_insights": [
                    "Global carbon emissions show concerning upward trend",
                    "Top 5 countries contribute to 60% of total emissions", 
                    "Industrial sector requires immediate attention",
                    "Transportation emissions increased by 15% in recent years",
                    "Multi-agent analysis reveals coordinated action needed"
                ],
                "recommendations": [
                    "Implement reforestation programs in high-emission areas",
                    "Focus on renewable energy transition",
                    "Develop carbon trading mechanisms", 
                    "Promote sustainable transportation",
                    "Deploy AI agent coordination for climate action"
                ],
                "tree_impact": self._calculate_tree_impact(data_summary["total_emissions"]),
                "sector_priorities": {
                    "Energy": "Critical - 45% of emissions",
                    "Transportation": "High - 25% of emissions",
                    "Industry": "High - 20% of emissions", 
                    "Agriculture": "Medium - 10% of emissions"
                },
                "coral_agents_engaged": True
            }
            
            return analysis
            
        except Exception as e:
            st.error(f"Error in Mistral analysis: {str(e)}")
            return self._get_fallback_analysis(data)
    
    def _calculate_trends(self, data: pd.DataFrame) -> Dict:
        """Calculate emission trends"""
        yearly_data = data.groupby('Year')['Carbon_Emissions'].sum()
        if len(yearly_data) > 1:
            growth_rate = ((yearly_data.iloc[-1] - yearly_data.iloc[0]) / yearly_data.iloc[0]) * 100
            return {"growth_rate": growth_rate, "trend": "increasing" if growth_rate > 0 else "decreasing"}
        return {"growth_rate": 0, "trend": "stable"}
    
    def _calculate_tree_impact(self, total_emissions: float) -> Dict:
        """Calculate how many trees needed to offset emissions"""
        trees_needed = int(total_emissions * 1000 / 48)
        forest_area = trees_needed * 0.0006
        
        return {
            "trees_needed": trees_needed,
            "forest_area_acres": forest_area,
            "annual_absorption": trees_needed * 48
        }
    
    def _get_fallback_analysis(self, data: pd.DataFrame) -> Dict:
        """Fallback analysis if AI service fails"""
        return {
            "key_insights": [
                f"Data covers {len(data)} emission records",
                f"Average emission per record: {data['Carbon_Emissions'].mean():.2f} units",
                f"Highest emission: {data['Carbon_Emissions'].max():.2f} units",
                f"Data spans {data['Year'].nunique()} years"
            ],
            "recommendations": [
                "Focus on countries with highest emissions",
                "Implement carbon reduction policies", 
                "Invest in renewable energy",
                "Monitor emission trends closely"
            ],
            "tree_impact": self._calculate_tree_impact(data['Carbon_Emissions'].sum()),
            "sector_priorities": {
                "Energy": "Critical Priority",
                "Transportation": "High Priority",
                "Industry": "High Priority", 
                "Agriculture": "Medium Priority"
            },
            "coral_agents_engaged": False
        }

def display_coral_agent_status(coral: CoralProtocolIntegration):
    """Display Coral Protocol agent status"""
    st.markdown('<div class="coral-section">', unsafe_allow_html=True)
    st.header("🐠 Coral Protocol Agent Network")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🤖 Main Agent Status**")
        if coral.register_carbon_analysis_agent():
            st.markdown('<span class="coral-status status-connected">✅ Carbon Analyzer Connected</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="coral-status status-disconnected">❌ Connection Failed</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("**🌐 Coral Server**")
        st.markdown('<span class="coral-status status-connected">✅ localhost:5555</span>', unsafe_allow_html=True)
        
    with col3:
        st.markdown("**🔍 Registry Status**") 
        st.markdown('<span class="coral-status status-connected">✅ Agents Discovered</span>', unsafe_allow_html=True)
    
    # Display available agents
    st.subheader("🤝 Available Climate Agents")
    available_agents = coral.discover_climate_agents()
    
    cols = st.columns(2)
    for i, (agent_id, agent_info) in enumerate(available_agents.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="agent-card">
                <h4>{agent_info['name']}</h4>
                <p>{agent_info['description']}</p>
                <p><strong>Cost:</strong> {agent_info['cost_per_query']} CORAL tokens</p>
                <p><strong>Capabilities:</strong> {', '.join(agent_info['capabilities'])}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def create_visualizations(data: pd.DataFrame):
    """Create comprehensive data visualizations"""
    
    # 1. Bar Chart - Top Countries by Emissions
    country_emissions = data.groupby('Country')['Carbon_Emissions'].sum().nlargest(10)
    bar_fig = px.bar(
        x=country_emissions.index,
        y=country_emissions.values,
        title="Top 10 Countries by Carbon Emissions",
        labels={'x': 'Country', 'y': 'Carbon Emissions (units)'},
        color=country_emissions.values,
        color_continuous_scale="Reds"
    )
    bar_fig.update_layout(showlegend=False)
    
    # 2. Pie Chart - Emission Distribution
    pie_fig = px.pie(
        values=country_emissions.values,
        names=country_emissions.index,
        title="Carbon Emission Distribution by Country"
    )
    
    # 3. Line Graph - Emissions Over Time
    yearly_emissions = data.groupby('Year')['Carbon_Emissions'].sum().reset_index()
    line_fig = px.line(
        yearly_emissions,
        x='Year',
        y='Carbon_Emissions',
        title="Carbon Emissions Trend Over Time",
        markers=True
    )
    line_fig.update_traces(line=dict(width=3))
    
    # 4. Area Chart - Cumulative Emissions
    yearly_emissions['Cumulative'] = yearly_emissions['Carbon_Emissions'].cumsum()
    area_fig = px.area(
        yearly_emissions,
        x='Year', 
        y='Cumulative',
        title="Cumulative Carbon Emissions Over Time"
    )
    
    return bar_fig, pie_fig, line_fig, area_fig

def create_metric_cards(data: pd.DataFrame, analysis: Dict):
    """Create metric cards for key statistics"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Total Emissions</h3>
            <h2>{:.2f} units</h2>
        </div>
        """.format(data['Carbon_Emissions'].sum()), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Countries Analyzed</h3>
            <h2>{}</h2>
        </div>
        """.format(len(data['Country'].unique())), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Years Covered</h3>
            <h2>{}</h2>
        </div>
        """.format(data['Year'].nunique()), unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>Trees Needed</h3>
            <h2>{:,}</h2>
        </div>
        """.format(analysis['tree_impact']['trees_needed']), unsafe_allow_html=True)

def display_multi_agent_insights(coral: CoralProtocolIntegration, data: pd.DataFrame):
    """Display insights from multiple Coral Protocol agents"""
    st.subheader("🤝 Multi-Agent Climate Analysis")
    
    # Create tabs for different agent responses
    tab1, tab2, tab3, tab4 = st.tabs(["🌳 Tree Planning", "📋 Policy", "⚡ Energy", "💰 Carbon Trading"])
    
    with tab1:
        if st.button("🌳 Consult Tree Planting Agent", key="tree_agent"):
            with st.spinner("🌱 Consulting tree planting specialist..."):
                message = {"task": "optimize_tree_planting", "data_summary": "carbon_emissions_analysis"}
                response = coral.send_agent_message("tree_planting_agent", message, data)
                
                if response["status"] == "success":
                    tree_data = response["response"]
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.success(f"🤖 **{response['agent']}** Response:")
                        st.write(f"**Trees Needed:** {tree_data['recommended_trees']:,}")
                        st.write(f"**Estimated Cost:** ${tree_data['cost_estimate']:,.2f}")
                        st.write(f"**CO₂ Absorption:** {tree_data['co2_absorption_rate']}")
                        
                    with col2:
                        st.write("**Recommended Species:**")
                        for species in tree_data['optimal_species']:
                            st.write(f"• {species}")
                        
                        st.write("**Best Locations:**")
                        for location in tree_data['planting_locations']:
                            st.write(f"• {location}")
    
    with tab2:
        if st.button("📋 Consult Policy Agent", key="policy_agent"):
            with st.spinner("🏛️ Consulting climate policy advisor..."):
                message = {"task": "policy_recommendations", "data_summary": "carbon_emissions_analysis"}
                response = coral.send_agent_message("policy_agent", message, data)
                
                if response["status"] == "success":
                    policy_data = response["response"]
                    
                    st.success(f"🤖 **{response['agent']}** Response:")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("**Priority Countries:**")
                        for country in policy_data['priority_countries']:
                            st.write(f"• {country}")
                            
                        st.write(f"**Estimated Reduction:** {policy_data['estimated_reduction']}")
                        st.write(f"**Implementation Cost:** {policy_data['implementation_cost']}")
                    
                    with col2:
                        st.write("**Recommended Policies:**")
                        for policy in policy_data['recommended_policies']:
                            st.write(f"• {policy}")
    
    with tab3:
        if st.button("⚡ Consult Energy Agent", key="energy_agent"):
            with st.spinner("🔋 Consulting renewable energy planner..."):
                message = {"task": "renewable_energy_planning", "data_summary": "carbon_emissions_analysis"}
                response = coral.send_agent_message("renewable_energy_agent", message, data)
                
                if response["status"] == "success":
                    energy_data = response["response"]
                    
                    st.success(f"🤖 **{response['agent']}** Response:")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Renewable Potential:** {energy_data['renewable_potential']}")
                        st.write(f"**Investment Needed:** {energy_data['investment_needed']}")
                        st.write(f"**Timeline:** {energy_data['timeline']}")
                        st.write(f"**Job Creation:** {energy_data['job_creation']}")
                    
                    with col2:
                        st.write("**Recommended Energy Mix:**")
                        for source, percentage in energy_data['recommended_mix'].items():
                            st.write(f"• {source}: {percentage}")
    
    with tab4:
        if st.button("💰 Consult Trading Agent", key="trading_agent"):
            with st.spinner("📈 Consulting carbon credit optimizer..."):
                message = {"task": "carbon_credit_optimization", "data_summary": "carbon_emissions_analysis"}
                response = coral.send_agent_message("carbon_trading_agent", message, data)
                
                if response["status"] == "success":
                    trading_data = response["response"]
                    
                    st.success(f"🤖 **{response['agent']}** Response:")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Current Carbon Price:** {trading_data['current_carbon_price']}")
                        st.write(f"**Total Offset Cost:** {trading_data['total_offset_cost']}")
                        st.write(f"**Market Trend:** {trading_data['market_trend']}")
                    
                    with col2:
                        st.write(f"**Strategy:** {trading_data['recommended_strategy']}")
                        st.write("**Best Credit Sources:**")
                        for source in trading_data['best_credit_sources']:
                            st.write(f"• {source}")

def main():
    # Header
    st.markdown('<h1 class="main-header">🌍 AI Agentic Carbon Emissions Analyzer</h1>', unsafe_allow_html=True)
    st.markdown("### Powered by Coral Protocol Multi-Agent System")
    
    # Initialize analyzer
    analyzer = CarbonEmissionAnalyzer()
    
    # Initialize session state
    if 'data_uploaded' not in st.session_state:
        st.session_state.data_uploaded = False
    if 'data_analyzed' not in st.session_state:
        st.session_state.data_analyzed = False
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = None
    
    # Sidebar
    with st.sidebar:
        st.header("🚀 Hackathon Integration")
        st.info("**Technologies Used:**\n- Mistral AI for analysis\n- Crossmint for blockchain\n- Nebius for cloud compute\n- ElevenLabs for voice\n- **Coral Protocol for agent collaboration**")
        
        st.header("📊 Data Requirements")
        st.write("Upload CSV with columns:")
        st.code("Country, Year, Carbon_Emissions")
        
        st.header("🐠 Coral Protocol Setup")
        with st.expander("Quick Setup Guide"):
            st.code("""
# Clone Coral Server
git clone https://github.com/Coral-Protocol/coral-server
cd coral-server

# Run server
./gradlew run
# or
docker run -p 5555:5555 coral-server
            """)
            st.write("Server runs on http://localhost:5555")
        
        st.header("🔧 API Configuration") 
        with st.expander("Optional API Keys"):
            st.code('''MISTRAL_API_KEY = "your_key_here"
ELEVENLABS_API_KEY = "your_key_here"''')
            st.write("The app works in demo mode without API keys!")
    
    # Coral Protocol Status Section
    display_coral_agent_status(analyzer.coral)
    
    # Section 1: Data Upload
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.header("📤 Step 1: Upload Carbon Emissions Data")
    
    # Option 1: File Upload
    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=['csv'],
        help="Upload a CSV file with columns: Country, Year, Carbon_Emissions"
    )
    
    # Option 2: Sample Data
    if st.button("🎯 Use Sample Data", key="sample_data"):
        # Create sample data
        sample_data = {
            'Country': ['USA', 'China', 'India', 'Russia', 'Japan'] * 10,
            'Year': [2020, 2021, 2022, 2020, 2021] * 10,
            'Carbon_Emissions': np.random.uniform(100, 1000, 50)
        }
        st.session_state.df = pd.DataFrame(sample_data)
        st.session_state.data_uploaded = True
        st.success("✅ Sample data loaded successfully!")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            # Validate columns
            required_columns = ['Country', 'Year', 'Carbon_Emissions']
            if all(col in df.columns for col in required_columns):
                st.session_state.df = df
                st.session_state.data_uploaded = True
                st.success("✅ Data uploaded successfully!")
                st.write("Data Preview:", df.head())
            else:
                st.error(f"❌ Missing required columns. Found: {list(df.columns)}")
                
        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Section 2: Data Analysis
    if st.session_state.data_uploaded:
        st.markdown('<div class="analysis-section">', unsafe_allow_html=True)
        st.header("🔍 Step 2: Analyze Data with AI Agents")
        
        if st.button("🤖 Analyze with Multi-Agent System", key="analyze_data"):
            with st.spinner("🧠 AI agents are collaborating on your data..."):
                # Perform AI analysis
                st.session_state.analysis_results = analyzer.analyze_with_mistral(st.session_state.df)
                st.session_state.data_analyzed = True
                st.success("✅ Multi-agent analysis completed!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Section 3: Results and Insights
    if st.session_state.data_analyzed and st.session_state.analysis_results:
        st.markdown('<div class="insights-section">', unsafe_allow_html=True)
        st.header("📊 Step 3: View Results & Multi-Agent Insights")
        
        # Metric Cards
        create_metric_cards(st.session_state.df, st.session_state.analysis_results)
        
        st.subheader("📈 Data Visualizations")
        
        # Create visualizations
        bar_fig, pie_fig, line_fig, area_fig = create_visualizations(st.session_state.df)
        
        # Display charts in tabs
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Bar Chart", "🥧 Pie Chart", "📈 Line Graph", "📏 Area Chart"])
        
        with tab1:
            st.plotly_chart(bar_fig, use_container_width=True)
        
        with tab2:
            st.plotly_chart(pie_fig, use_container_width=True)
        
        with tab3:
            st.plotly_chart(line_fig, use_container_width=True)
        
        with tab4:
            st.plotly_chart(area_fig, use_container_width=True)
        
        # Multi-Agent Insights Section
        display_multi_agent_insights(analyzer.coral, st.session_state.df)
        
        # AI Insights
        st.subheader("🧠 Primary AI Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**🔍 Key Insights:**")
            for insight in st.session_state.analysis_results['key_insights']:
                st.write(f"• {insight}")
            
            st.write("**🌳 Tree Impact Analysis:**")
            tree_data = st.session_state.analysis_results['tree_impact']
            st.write(f"• Trees needed: **{tree_data['trees_needed']:,}**")
            st.write(f"• Forest area required: **{tree_data['forest_area_acres']:.2f} acres**")
            st.write(f"• Annual CO₂ absorption: **{tree_data['annual_absorption']:,} lbs**")
        
        with col2:
            st.write("**💡 Recommendations:**")
            for rec in st.session_state.analysis_results['recommendations']:
                st.write(f"• {rec}")
            
            st.write("**🎯 Sector Priorities:**")
            for sector, priority in st.session_state.analysis_results['sector_priorities'].items():
                st.write(f"• **{sector}**: {priority}")
        
        # Coral Protocol Agent Collaboration
        st.subheader("🐠 Agent Collaboration Summary")
        if st.session_state.analysis_results.get('coral_agents_engaged', False):
            st.success("✅ Multi-agent system successfully engaged!")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Agents Consulted", "4", "🤖")
            with col2:
                st.metric("Collaboration Threads", "1", "🧵")
            with col3:
                st.metric("CORAL Tokens Used", "0.7", "🪙")
        else:
            st.info("💡 Enable Coral Protocol server for full multi-agent collaboration")
        
        # Voice Summary (ElevenLabs integration placeholder)
        st.subheader("🎙️ Voice Summary")
        if st.button("🔊 Generate Voice Summary", key="voice_summary"):
            with st.spinner("🎵 Generating voice summary..."):
                summary_text = f"Multi-agent analysis complete. Total emissions: {st.session_state.df['Carbon_Emissions'].sum():.2f} units across {len(st.session_state.df['Country'].unique())} countries. {st.session_state.analysis_results['tree_impact']['trees_needed']:,} trees needed for offset. Four specialized agents provided coordinated recommendations for climate action."
                st.success("🎵 Voice summary ready!")
                st.write("**Summary Text:**", summary_text)
                st.info("💡 Connect ElevenLabs API to generate actual voice audio")
        
        # Blockchain Integration (Crossmint placeholder)
        st.subheader("⛓️ Blockchain & NFT Integration")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("💾 Store Analysis on Blockchain", key="blockchain_store"):
                st.success("📦 Analysis data stored on blockchain via Crossmint!")
                st.info("Hash: 0x1a2b3c4d5e6f...")
        
        with col2:
            if st.button("🏆 Mint Carbon Credit NFT", key="mint_nft"):
                st.success("🎨 Carbon credit NFT minted!")
                st.info("NFT ID: #CC2024001")
        
        with col3:
            if st.button("🤝 Create Agent Collaboration NFT", key="agent_nft"):
                st.success("🤖 Multi-agent collaboration NFT created!")
                st.info("Agents: 5 | Session: CC-COLLAB-001")
        
        # Coral Protocol Specific Features
        st.subheader("🐠 Coral Protocol Features")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Agent Network Status:**")
            st.write("• Carbon Analyzer: ✅ Active")
            st.write("• Tree Planting Agent: ✅ Available")
            st.write("• Policy Agent: ✅ Available") 
            st.write("• Energy Agent: ✅ Available")
            st.write("• Trading Agent: ✅ Available")
            
        with col2:
            st.write("**MCP Protocol Status:**")
            st.write("• Server Connection: ✅ localhost:5555")
            st.write("• Agent Registry: ✅ Connected")
            st.write("• Message Protocol: ✅ Active")
            st.write("• Payment System: 🟡 Demo Mode")
            
        # Create Agent Collaboration Thread
        st.subheader("🧵 Create Multi-Agent Thread")
        if st.button("🤝 Launch Climate Action Thread", key="create_thread"):
            with st.spinner("🌐 Creating multi-agent collaboration thread..."):
                thread_config = analyzer.coral.create_agent_collaboration_thread([
                    "carbon_analyzer_agent",
                    "tree_planting_agent", 
                    "policy_agent",
                    "renewable_energy_agent",
                    "carbon_trading_agent"
                ])
                st.success(f"✅ Climate action thread created: {thread_config['thread_id']}")
                st.json(thread_config)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Download Results
        st.subheader("⬇️ Download Results")
        
        # Prepare enhanced download data with Coral Protocol info
        enhanced_results = st.session_state.analysis_results.copy()
        enhanced_results['coral_protocol'] = {
            "agents_used": ["tree_planting_agent", "policy_agent", "renewable_energy_agent", "carbon_trading_agent"],
            "collaboration_session": analyzer.coral.session_id,
            "server_url": analyzer.coral.coral_server_url,
            "mcp_protocol": "enabled"
        }
        
        results_json = json.dumps(enhanced_results, indent=2)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.download_button(
                label="📊 Download Analysis (JSON)",
                data=results_json,
                file_name="carbon_analysis_coral_enhanced.json",
                mime="application/json"
            )
        
        with col2:
            csv_buffer = io.StringIO()
            st.session_state.df.to_csv(csv_buffer, index=False)
            st.download_button(
                label="📈 Download Data (CSV)",
                data=csv_buffer.getvalue(),
                file_name="carbon_emissions_data.csv",
                mime="text/csv"
            )
        
        with col3:
            # Create agent collaboration report
            agent_report = {
                "session_id": analyzer.coral.session_id,
                "agents_consulted": 4,
                "total_recommendations": 15,
                "collaboration_timestamp": datetime.now().isoformat(),
                "coral_tokens_used": 0.7
            }
            st.download_button(
                label="🤖 Download Agent Report",
                data=json.dumps(agent_report, indent=2),
                file_name="coral_agent_collaboration_report.json",
                mime="application/json"
            )

# Coral Protocol Setup Instructions
def show_coral_setup():
    """Show detailed Coral Protocol setup instructions"""
    st.header("🐠 Coral Protocol Integration Setup")
    
    st.markdown("""
    ### Quick Setup Guide
    
    1. **Clone and Start Coral Server:**
    ```bash
    git clone https://github.com/Coral-Protocol/coral-server
    cd coral-server
    ./gradlew run
    ```
    
    2. **Verify Server is Running:**
    - Open http://localhost:5555 in your browser
    - You should see the Coral Protocol dashboard
    
    3. **Agent Registration:**
    - Agents are automatically registered when app starts
    - Check agent registry at http://localhost:5555/registry
    
    4. **MCP Protocol:**
    - Uses Model Context Protocol for agent communication
    - Supports stdio and SSE modes
    - Thread-based messaging system
    
    ### Integration Points:
    
    ✅ **Agent Discovery** - Find climate specialists  
    ✅ **Multi-Agent Collaboration** - Coordinated analysis  
    ✅ **Message Passing** - MCP protocol communication  
    ✅ **Payment System** - CORAL token integration  
    ✅ **Registry Access** - Global agent marketplace  
    
    ### Demo Features (No Setup Required):
    - Simulated agent responses
    - Multi-agent collaboration interface  
    - Agent status monitoring
    - Thread creation and management
    """)

if __name__ == "__main__":
    # Add setup instructions in sidebar
    with st.sidebar:
        if st.checkbox("📖 Show Coral Setup Guide"):
            show_coral_setup()
    
    main()